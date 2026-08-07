from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from datetime import datetime
from elasticsearch import Elasticsearch
from typing import List, Optional
import os
from fastapi.middleware.cors import CORSMiddleware

from arquivos_py.RAG.RAG_origin import rag

cloud_id = os.getenv("cloud_id")
api_key = os.getenv("api_elastic")

client = Elasticsearch(cloud_id=cloud_id, api_key=api_key)

index = "historico_chat"

app = FastAPI()

origens_permitidas = [
    "http://localhost:8501",
    "http://localhost:8000/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origens_permitidas, # Quem pode acessar?
    allow_credentials=True,           # Permite envio de cookies/tokens de autenticação
    allow_methods=["*"],              # Permite todos os métodos HTTP (GET, POST, PUT, DELETE)
    allow_headers=["*"],              # Permite todos os cabeçalhos (headers) na requisição
)

class FonteModel(BaseModel):
    origem: str
    score: float
    conteudo: str

class MensagemModel(BaseModel):
    title: str
    chat_id: str
    role: str
    date: datetime
    text_content: str
    fontes: Optional[List[FonteModel]] = [] # Opcional, pois mensagens do usuário não terão fontes


class QuestionRequest(BaseModel):
    pergunta : str
    
    
    
# 2. Criando a rota POST para salvar no Elasticsearch
@app.post("/api/chat/history")
async def salvar_mensagem(mensagem: MensagemModel):
    try:
        # Transformamos o modelo Pydantic em um dicionário que o Elasticsearch entende
        documento = mensagem.model_dump()
        
        # Injetamos o documento no index
        resposta = client.index(index=index, document=documento)
        
        return {"status": "sucesso", "mensagem_salva": resposta["_id"]}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao salvar no banco: {str(e)}")
    
    
@app.get("/api/chat/sessions")
async def listar_sessoes():
    try:
        # Agregação para buscar os chat_ids únicos
        query = {
                    "size": 0,
                    "aggs": {
                        "sessoes_unicas": {
                            "terms": {
                                "field": "chat_id", # Exatamente como você fez, sem o .keyword!
                                "size": 100,
                                # Ordena pela data da mensagem mais recente daquela sessão
                                "order": { "ultima_mensagem": "desc" } 
                            },
                            "aggs": {
                                # 1. Pega a maior data (mais recente) dentro dessa conversa
                                "ultima_mensagem": {
                                    "max": { "field": "date" }
                                },
                                # 2. Puxa o título para podermos desenhar na interface
                                "titulo": {
                                    "terms": {
                                        "field": "title.keyword", # Aqui usa .keyword por causa do multi-field
                                        "size": 1
                                    }
                                }
                            }
                        }
                    }
                }
    
        resposta = client.search(index=index, body=query)
        
        # Extrai apenas os nomes dos IDs da resposta complexa do Elastic
        sessoes = [bucket["key"] for bucket in resposta["aggregations"]["sessoes_unicas"]["buckets"]]
        
        return {"status": "sucesso", "sessoes": sessoes}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao buscar sessões: {str(e)}")    
    
@app.get("/api/chat/history")
async def buscar_historico(chat_id: str):
    try:
        # Montamos a query de busca no Elasticsearch
        query = {
            "query": {
                "match": {
                    "chat_id": chat_id
                }
            },
            "sort": [
                {"date": {"order": "asc"}} # Traz da mais antiga para a mais nova
            ]
        }
        
        # Fazemos a busca (size=1000 garante que trazemos o chat inteiro)
        resposta = client.search(index=index, body=query, size=1000)
        
        # Extraímos apenas a parte que importa (o _source de cada documento)
        mensagens = []
        for hit in resposta["hits"]["hits"]:
            fonte = hit["_source"]
            mensagens.append({
                "role": fonte.get("role"),
                "content": fonte.get("text_content"),
                "fontes": fonte.get("fontes", [])
            })            
        return {"status": "sucesso", "mensagens": mensagens}
        
    except Exception as e:
        print(f"Erro ao carregar histórico: {e}")
        return {"mensagens": []}


@app.post("/api/chat")
async def chat_endpoint(request: QuestionRequest):
    """
    Recebe a pergunta do front
    """
    
    pergunta_do_usuario = request.pergunta.strip()
    
    if not pergunta_do_usuario:
        raise HTTPException(
            status_code=400, 
            detail="A pergunta não pode estar vazia."
        )
        
    resposta_da_ia = await rag(user_query=pergunta_do_usuario)
    
    return{
        "resposta": resposta_da_ia
    }