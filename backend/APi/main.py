from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from arquivos_py.RAG.RAG_origin import rag

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

class QuestionRequest(BaseModel):
    pergunta : str
    
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