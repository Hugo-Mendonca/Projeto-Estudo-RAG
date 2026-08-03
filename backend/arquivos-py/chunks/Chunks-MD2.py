from langchain_classic.text_splitter import RecursiveCharacterTextSplitter
import os
import re

arquivo_md = r"C:\Users\hugo.bastos\Desktop\Projeto-RAG-SI5\Projeto-Estudo-RAG\backend\arquivo-dados\arquivo-md\Relatório Covertype.md"
caminho_final = r"C:\Users\hugo.bastos\Desktop\Projeto-RAG-SI5\Projeto-Estudo-RAG\backend\arquivo-dados\arquivo-md\chunk copy.md"

with open(arquivo_md, "r", encoding="utf-8") as f:
    conteudo = f.read()

conteudo_limpo = re.sub(r'## (\d+\.)', r'### \1', conteudo)

with open(arquivo_md, "w", encoding="utf-8") as f:
    f.write(conteudo_limpo)


md_splitter = RecursiveCharacterTextSplitter(
    chunk_size=512,        # tokens por chunk
    chunk_overlap=64,      # overlap entre chunks adjacentes
    length_function=len,
    separators=["\n\n", "\n", ". ", " ", ""]
)


docs = md_splitter.create_documents([conteudo_limpo])

with open(caminho_final, "w", encoding="utf-8") as f:
    # Novamente, usando singular para o item iterado
    for i, chunk in enumerate(docs):
        f.write(f"--- CHUNK {i+1} ---\n")
        # Agora sim, 'chunk' é um objeto Document e possui 'page_content'
        f.write(chunk.page_content)
        f.write("\n\n")