from elasticsearch import Elasticsearch,helpers
from transformers import AutoTokenizer
import os
from dotenv import load_dotenv

load_dotenv()

cloud_id= os.getenv("cloud_id")
api_key = os.getenv("api_elastic")

caminho_arquivo_chunks = r"C:\Users\hugo.bastos\Desktop\Projeto-RAG-SI5\Projeto-Estudo-RAG\backend\arquivo-md\chunk.md"

with open(caminho_arquivo_chunks, "r", encoding="utf-8") as f:
   conteudo = f.read()


lista_chunks_cru =  conteudo.split("\n\n")

lista_chunks = [chunk.strip() for chunk in lista_chunks_cru if chunk.strip()]
print(f"Total de chunks encontrados: {len(lista_chunks)}")

#Credenciais em produção, use variáveis de ambiente!
client = Elasticsearch(
    cloud_id= cloud_id,
    api_key= api_key
    )


# Testa se a conexão foi bem-sucedida
if client.ping():
    print("Conectado ao Elasticsearch com sucesso!")
else:
    print("Falha na conexão.")

print("--- Carregando Tokenizer para Chunking/Estimativa de tokens... ---")
CHUNK_TOKENIZER = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")

def estimate_token_count(text: str) -> int:
    """Estimativa simples de tokens usando o tokenizer carregado."""
    if not text:
        return 0
    # encode() retorna ids; len(ids) é uma boa aproximação para controle e métricas
    return len(CHUNK_TOKENIZER.encode(text, add_special_tokens=False))


index_name = "projeto_rag_chunks"

if not client.indices.exists(index = index_name):
    client.indices.create(index = index_name)
    print(f"Índice: {index_name} criado")
else:
    print(f"Índice {index_name} já existe, add novos docs")
    

print("Preparando pacotes Bulk")

bulk_actions = []

for i,chunks_text in enumerate(lista_chunks, start=1):
    token_count = estimate_token_count(chunks_text)
    
    doc_body = {
        "chunk_id" : str(i),
        "text_content": chunks_text,
        "token_count": token_count
    }
    
    bulk_actions.append({
        "_op_type": "index",
        "_index": index_name,
        "_source": doc_body
    })
    

print(f"Enviando {len(bulk_actions)} chunks pro elastic...")
try:
    success, errors = helpers.bulk(client, bulk_actions)
    print(f"✅ Sucesso! {success} chunks foram salvos no Elastic.")
    if errors:
        print("⚠️ Houve alguns erros:", errors)
except Exception as e:
    print(f"❌ Erro ao enviar os dados: {e}")