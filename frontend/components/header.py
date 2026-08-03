"""
Componente do cabeçalho principal da aplicação.
"""
import streamlit as st

def render_header() -> None:
    """Renderiza o título e a descrição do assistente na área principal."""
    st.title("Assistente virtual do seu relatório")
    st.markdown("Interface moderna para consulta de relatório da cadeira de CoverType.")
    st.divider()