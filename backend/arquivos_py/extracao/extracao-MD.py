from docling.document_converter import DocumentConverter
import os

arquivo_pdf = r"C:\Users\hugo.bastos\Desktop\Projeto-RAG-SI5\Projeto-Estudo-RAG\backend\arquivo-dados\arquivo-pdf\Relatório Covertype.pdf"
output_complete= r"C:\Users\hugo.bastos\Desktop\Projeto-RAG-SI5\Projeto-Estudo-RAG\backend\arquivo-dados\arquivo-md\Relatório Covertype.md"

converter = DocumentConverter()
documento = converter.convert(arquivo_pdf).document


arquivo_md = documento.export_to_markdown()

with open(output_complete, "w", encoding="utf-8") as f:
    f.write(arquivo_md)

