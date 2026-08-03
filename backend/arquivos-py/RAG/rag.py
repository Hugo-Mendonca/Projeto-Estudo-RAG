import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI

# 1. IMPORTAÇÕES CORRIGIDAS: Trazendo o modelo local do HuggingFace
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_elasticsearch import ElasticsearchStore

# 1. Carregamento de variáveis no escopo global (Executado apenas 1x)
load_dotenv()
api_chat_key = os.getenv("api_gemi")
cloud_id = os.getenv("cloud_id")
api_key = os.getenv("api_elastic")

# 2. Configuração do Embedding (CLIENT-SIDE)
# Aqui geramos os vetores na sua máquina, sem depender do servidor do Elastic
embeddings = HuggingFaceEmbeddings(
    model_name="intfloat/multilingual-e5-small",
    model_kwargs={'device': 'cpu'}, 
    encode_kwargs={'normalize_embeddings': True}
)

# 3. Inicialização do VectorStore (Abstração do LangChain para o Elastic)
vector_store = ElasticsearchStore(
    es_cloud_id=cloud_id,
    es_api_key=api_key,
    index_name="projeto_rag_chunks_v2",
    embedding=embeddings,
    strategy=ElasticsearchStore.ApproxRetrievalStrategy() # Adicionado para garantir busca K-NN otimizada
)

# 4. Inicialização do LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-flash-latest",
    temperature=0,
    google_api_key=api_chat_key
)

# 5. Definição do Prompt 
template = PromptTemplate.from_template("""    
Answer the user query based on context. If you don't know the answer or the context does not have the answer, say that you don't know.
ALWAYS answer in pt-BR. You are going to answer questions about a DataScience report project. Answer the questions starting with "No estudo..." or "Os autores chegaram a conclusão que..."
ALWAYS answer with the source of your knowledge. I want the answer with a chunk definition.

## CONTEXT
{contexto}

## USER QUERY
{pergunta}
""")

# 6. Criação do Pipeline (LCEL)
rag_pipeline = template | llm | StrOutputParser()

def format_docs(docs: list) -> str:
    """Função auxiliar para formatar a lista de Documentos em uma string."""
    formatted = []
    for k, doc in enumerate(docs, start=1):
        source = doc.metadata.get("origem", "Fonte Desconhecida") # Alterado 'source' para 'origem' com base na nossa ingestão
        formatted.append(f"## Documento {k}\n{doc.page_content}\nSource: {source}")
    return "\n\n".join(formatted)

def rag(user_query: str) -> str:
    """
    Executa o pipeline RAG completo: Busca -> Formatação -> Geração.
    """
    # Adicionado k=3 para limitar a busca e não estourar os tokens do Gemini
    resultados = vector_store.similarity_search(user_query, k=3)
    
    if not resultados:
        return "Eu não encontrei informações no relatório sobre essa pergunta..."
    
    context_str = format_docs(resultados)
    
    resposta = rag_pipeline.invoke({
        "contexto": context_str, 
        "pergunta": user_query
    })
    
    return resposta

# Teste de execução
if __name__ == "__main__":
    teste = rag("Quais foram os algoritmos utilizados para classificar o tipo de solo?")
    print(teste)