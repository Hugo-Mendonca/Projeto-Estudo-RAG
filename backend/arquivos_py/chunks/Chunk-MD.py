from langchain_classic.text_splitter import MarkdownHeaderTextSplitter
import os
import re

arquivo_md = "/home/hugo/Downloads/projeto-Rag_SI5/Projeto-Estudo-RAG/backend/arquivo-md/Relatório Covertype.md"
caminho_final = "/home/hugo/Downloads/projeto-Rag_SI5/Projeto-Estudo-RAG/backend/arquivos-py/chunks/chunk.md"

with open(arquivo_md, "r", encoding="utf-8") as f:
    conteudo = f.read()

conteudo_limpo = re.sub(r'## (\d+\.)', r'### \1', conteudo)

with open(arquivo_md, "w", encoding="utf-8") as f:
    f.write(conteudo_limpo)

hearders = [
    ("#", "Header 1"),
    ("##", "Header 2"),
    ("###", "Header 3"),
    ("####", "Header 4")
]

md_splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on = hearders,
    strip_headers = False,
)

chunks = md_splitter.split_text(conteudo_limpo)

with open(caminho_final, "w", encoding="utf-8") as f:
    for i, chunks in enumerate(chunks):
        f.write(f"--- CHUNK {i+1} ---\n")
        f.write(chunks.page_content)
        f.write("\n\n")