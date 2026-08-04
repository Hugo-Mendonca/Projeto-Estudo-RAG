import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_elasticsearch import ElasticsearchStore
from langchain_huggingface import HuggingFaceEmbeddings

# 1. Carregamento de variáveis no escopo global (Executado apenas 1x)
load_dotenv()
api_chat_key = os.getenv("api_gemi")
cloud_id = os.getenv("cloud_id")
api_key = os.getenv("api_elastic")

# 2. Configuração do Embedding (Crucial para a busca vetorial)
# O RAG precisa transformar a pergunta do usuário em vetor usando o mesmo modelo que criou os chunks
embeddings = HuggingFaceEmbeddings(
    model_name="intfloat/multilingual-e5-small",
    model_kwargs={'device': 'cpu'}, 
    encode_kwargs={'normalize_embeddings': True}
)

# 3. Inicialização do VectorStore (Abstração do LangChain para o Elastic)
vector_store = ElasticsearchStore(
    es_cloud_id=cloud_id,
    es_api_key=api_key,
    index_name="projeto_rag_chunks",
    embedding=embeddings
)

# 4. Inicialização do LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-flash-latest",
    temperature=0,
    google_api_key=api_chat_key
)

# 5. Definição do Prompt (Corrigido o typo 'pegunta' -> 'pergunta')
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
        source = doc.metadata.get("source", "Fonte Desconhecida")
        formatted.append(f"## Documento {k}\n{doc.page_content}\nSource: {source}")
    return "\n\n".join(formatted)

def rag(user_query: str) -> str:
    """
    Executa o pipeline RAG completo: Busca -> Formatação -> Geração.
    """
    # Realiza a busca vetorial (KNN) já retornando objetos 'Document' do LangChain
    # Opcional: Adicionar k=5 para limitar a quantidade de chunks trazidos
    resultados = vector_store.similarity_search(user_query)
    
    # Validação rigorosa: Cláusula de guarda
    if not resultados:
        return "Eu não encontrei informações no relatório sobre essa pergunta..."
    
    # Formata os documentos para serem injetados no prompt
    context_str = format_docs(resultados)
    
    # Invoca a cadeia com as chaves exatas do PromptTemplate
    resposta = rag_pipeline.invoke({
        "contexto": context_str, 
        "pergunta": user_query
    })
    
    return resposta

# Teste de execução
if __name__ == "__main__":
    teste = rag("Como foram os resultados dos algoritmos de árvore?")
    print(teste)