from docling.document_converter import DocumentConverter
import os

arquivo_pdf = "/home/hugo/Downloads/projeto-Rag_SI5/Projeto-Estudo-RAG/backend/Relatório Covertype.pdf"
output_complete= "/home/hugo/Downloads/projeto-Rag_SI5/Projeto-Estudo-RAG/backend/Relatório Covertype.md"

converter = DocumentConverter()
documento = converter.convert(arquivo_pdf).document


arquivo_md = documento.export_to_markdown()

with open(output_complete, "w", encoding="utf-8") as f:
    f.write(arquivo_md)

