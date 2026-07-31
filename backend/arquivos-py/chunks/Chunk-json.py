import chromadb
from langchain_classic.retrievers import ParentDocumentRetriever
from langchain_classic.storage import InMemoryStore
from langchain_classic.text_splitter import RecursiveCharacterTextSplitter



arquivo_json = r"C:\Users\hugo.bastos\Desktop\Projeto-RAG-SI5\Projeto-Estudo-RAG\backend\arquivo-json\Relatório Covertype.json"
caminho_saida = r"C:\Users\hugo.bastos\Desktop\Projeto-RAG-SI5\Projeto-Estudo-RAG\backend\arquivo-json\chunk.json"

with open( arquivo_json, "r", encoding="utf-8") as f:
    conteudo = f.read()
    
clid_splitter = RecursiveCharacterTextSplitter(chunk_size=250)

parent_splitter = RecursiveCharacterTextSplitter(chunk_size = 2500)

store = InMemoryStore()

retrivier = ParentDocumentRetriever(
    vectorstore= chromadb,
    docstore = store,
    child_splitter = clid_splitter,
    parent_splitter = parent_splitter,
    
)

chunks = retrivier.add_documents(conteudo)

with open(caminho_saida, "w", encoding="utf-8") as f:
    for i,chunk in enumerate(chunks):
        f.write(f"--- CHUNK {i+1} ---\n")
        f.write(chunk.page_content)
        f.write("\n\n")