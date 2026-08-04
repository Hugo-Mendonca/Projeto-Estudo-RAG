import os
from pathlib import Path
from dotenv import load_dotenv
from elasticsearch import Elasticsearch
from elasticsearch.helpers import BulkIndexError # <-- Importação adicionada aqui

# Novas importações da arquitetura Client-Side (LangChain)
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_elasticsearch import ElasticsearchStore

# ==========================================
# 1. CARREGAMENTO DE VARIÁVEIS DE AMBIENTE
# ==========================================
diretorio_ataul = Path(__file__).resolve().parent
caminho_env = diretorio_ataul.parent.parent.parent / '.env'

print(f"Caminho do .env montado: {caminho_env}")
print(f"O arquivo .env realmente existe neste caminho? {caminho_env.exists()}")

load_dotenv(dotenv_path=caminho_env)

cloud_id = os.getenv("cloud_id")
api_key = os.getenv("api_elastic")

if not cloud_id or not api_key:
    raise ValueError(
        "\n❌ ERRO CRÍTICO: cloud_id ou api_elastic estão vazios!\n"
        "Verifique o .env e os nomes das variáveis."
    )
print("✅ Variáveis de ambiente carregadas com sucesso!")

# ==========================================
# 2. CONEXÃO COM O BANCO DE DADOS
# ==========================================
client = Elasticsearch(cloud_id=cloud_id, api_key=api_key)

if client.ping():
    print("✅ Conectado ao Elasticsearch com sucesso!")
else:
    raise ConnectionError("❌ Falha na conexão com o Elasticsearch.")

# ==========================================
# 3. EXTRAÇÃO E CHUNKING
# ==========================================
caminho_arquivo_chunks = "/home/hugo/Downloads/projeto-Rag_SI5/Projeto-Estudo-RAG/backend/arquivo-dados/arquivo-md/chunk.md"

with open(caminho_arquivo_chunks, "r", encoding="utf-8") as f:
    conteudo = f.read()

lista_chunks_cru = conteudo.split("\n\n")
lista_chunks = [chunk.strip() for chunk in lista_chunks_cru if chunk.strip()]
print(f"Total de textos encontrados: {len(lista_chunks)}")

# Transformando strings puras em objetos Document do LangChain
docs = [
    Document(page_content=texto, metadata={"chunk_id": i, "origem": "chunk.md"}) 
    for i, texto in enumerate(lista_chunks, start=1)
]

# ==========================================
# 4. PIPELINE DE EMBEDDINGS (Client-Side)
# ==========================================
print("\n--- Carregando o modelo de IA na memória (Isso pode levar alguns segundos na 1ª vez)... ---")
modelo_embedding = HuggingFaceEmbeddings(
    model_name="intfloat/multilingual-e5-small",
    model_kwargs={'device': 'cpu'}, 
    encode_kwargs={'normalize_embeddings': True}
)

# ==========================================
# 5. INGESTÃO NO ELASTICSEARCH
# ==========================================
# IMPORTANTE: Mudamos o nome do índice para evitar conflitos com os testes anteriores
index_name = "projeto_rag_chunks" 

print(f"Iniciando a geração de vetores e a ingestão no índice '{index_name}'...")

try:
    vetor_store = ElasticsearchStore.from_documents(
        documents=docs,
        embedding=modelo_embedding,
        es_cloud_id=cloud_id,
        es_api_key=api_key,
        index_name=index_name,
        strategy=ElasticsearchStore.ApproxRetrievalStrategy() # Prepara o ES para buscas k-NN
    )
    print("🚀 Ingestão concluída com sucesso! Vetores gerados e armazenados.")

except BulkIndexError as e:
    print("\n❌ O Elasticsearch rejeitou os documentos. Veja o motivo exato (Mostrando o 1º erro):")
    # Imprime os detalhes do erro do primeiro documento rejeitado
    print(e.errors[0])
    
except Exception as e:
    print(f"\n❌ Erro inesperado durante a ingestão: {e}")