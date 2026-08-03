"""
Componente do cabeçalho principal da aplicação.
"""
import streamlit as st

def render_header() -> None:
    """Renderiza o título e a descrição do assistente na área principal."""
    st.title("🤖 Chat Assistant")
    st.markdown("Interface moderna para consulta de relatório da cadeira de CoverType.")
    st.divider()