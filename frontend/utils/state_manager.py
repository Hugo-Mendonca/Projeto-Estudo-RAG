"""
Módulo responsável por gerenciar o st.session_state da aplicação.
"""
import streamlit as st

def init_session_state() -> None:
    """Inicializa as variáveis de estado da sessão caso não existam."""
    if "messages" not in st.session_state:
        st.session_state.messages = []

def clear_chat() -> None:
    """Limpa o histórico de mensagens da sessão atual."""
    st.session_state.messages = []