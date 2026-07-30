import json
from docling.document_converter import DocumentConverter
import os


arquivo_pdf = "/home/hugo/Downloads/projeto-Rag_SI5/Projeto-Estudo-RAG/backend/arquivo-pdf/Relatório Covertype.pdf"

output_path = "/home/hugo/Downloads/projeto-Rag_SI5/Projeto-Estudo-RAG/backend/arquivo-json/Relatório Covertype.json"

converter = DocumentConverter()
documento = converter.convert(arquivo_pdf).document

doc_dict = documento.export_to_dict()
doc_json = json.dumps(doc_dict, indent=2)

with open(output_path, "w", encoding="utf-8") as f:
    f.write(doc_json)