import os
from pathlib import Path
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_elasticsearch import ElasticsearchStore

# ==========================================
# 1. CARREGAR VARIÁVEIS DE AMBIENTE
# ==========================================
diretorio_ataul = Path(__file__).resolve().parent
caminho_env = diretorio_ataul.parent.parent.parent / '.env'
load_dotenv(dotenv_path=caminho_env)

cloud_id = os.getenv("cloud_id")
api_key = os.getenv("api_elastic")

if not cloud_id or not api_key:
    raise ValueError("❌ ERRO CRÍTICO: cloud_id ou api_elastic estão vazios!")

# ==========================================
# 2. CARREGAR O MODELO DE IA (O MESMO DA INGESTÃO)
# ==========================================
print("--- Inicializando o modelo de Embeddings (Client-Side) ---")
modelo_embedding = HuggingFaceEmbeddings(
    model_name="intfloat/multilingual-e5-small",
    model_kwargs={'device': 'cpu'}, 
    encode_kwargs={'normalize_embeddings': True}
)

# ==========================================
# 3. CONECTAR AO ÍNDICE EXISTENTE
# ==========================================
index_name = "projeto_rag_chunks_v2"
print(f"--- Conectando ao índice '{index_name}' no Elastic Cloud ---")

# Diferente da ingestão (from_documents), aqui nós instanciamos 
# o ElasticsearchStore puro, apenas apontando para o índice que já existe.
vetor_store = ElasticsearchStore(
    embedding=modelo_embedding,
    index_name=index_name,
    es_cloud_id=cloud_id,
    es_api_key=api_key,
    strategy=ElasticsearchStore.ApproxRetrievalStrategy()
)

# ==========================================
# 4. EXECUTAR A BUSCA SEMÂNTICA (A PROVA REAL)
# ==========================================
# Vi na sua imagem anterior que os textos falam sobre Mineração de Dados / CRISP-DM.
# Você pode alterar essa pergunta para qualquer coisa que exista no seu texto!
pergunta = "Quais são as etapas do projeto de Mineração de Dados e CRISP-DM?"

print(f"\n🔍 Buscando no banco de dados por: '{pergunta}'\n")

try:
    # O k=3 significa que queremos que ele traga os 3 chunks mais relevantes
    resultados = vetor_store.similarity_search(pergunta, k=3)
    
    print(f"✅ Sucesso! O Elasticsearch retornou {len(resultados)} chunks relevantes.\n")
    
    for i, doc in enumerate(resultados, 1):
        print(f"--- RESULTADO {i} ---")
        print(f"Metadados: {doc.metadata}")
        # Imprimindo os primeiros 250 caracteres de cada chunk para verificarmos o conteúdo
        print(f"Conteúdo: {doc.page_content[:250]}...\n")

except Exception as e:
    print(f"❌ Ocorreu um erro durante a busca: {e}")