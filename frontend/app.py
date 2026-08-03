"""
Ponto de entrada principal da aplicação Frontend.
"""
import streamlit as st
from components.sidebar import render_sidebar
from components.chat import render_chat
from components.header import render_header
from utils.state_manager import init_session_state

def load_css(file_path: str) -> None:
    """
    Lê o arquivo CSS e o injeta na aplicação.
    
    Args:
        file_path (str): Caminho para o arquivo CSS.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning(f"Arquivo CSS não encontrado: {file_path}")

def main() -> None:
    """Função principal que orquestra os componentes e inicializa a UI."""
    
    # Configuração primordial da página (deve ser a primeira chamada do Streamlit)
    st.set_page_config(
        page_title="RAG Chatbot Frontend",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Injeção de CSS customizado
    load_css("styles/styles.css")
    
    # Inicialização de dados
    init_session_state()
    
    # Renderização de Layout
    render_sidebar()
    render_header()
    render_chat()

if __name__ == "__main__":
    main()