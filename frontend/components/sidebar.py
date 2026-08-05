"""
Componente de interface para a barra lateral (Sidebar).
"""
import streamlit as st
from utils.state_manager import clear_chat
import requests
import uuid

BASE_URL = "http://localhost:8000/api/chat"

def carregar_sessoes_api():
    """Busca a lista de IDs de conversas existentes no backend."""
    try:
        resposta = requests.get(f"{BASE_URL}/sessions")
        if resposta.status_code == 200:
            return resposta.json().get("sessoes", [])
        return []
    except:
        return []

def render_sidebar() -> None:
    """Renderiza os elementos visuais e de navegação da barra lateral."""
    with st.sidebar:
        # Logo e Nome
        st.image(r"C:\Users\hugo.bastos\Desktop\Projeto-RAG-SI5\Projeto-Estudo-RAG\frontend\utils\Logo RAG.avif", use_container_width=True)
        st.markdown("## Sistema RAG do Relatório do CoverType")
        st.write("") # Espaçamento
        
        # Botão nova conversa
        if st.button("➕ Nova conversa", use_container_width=True):
            clear_chat()
            st.rerun()
            
        st.divider()
        
        st.subheader("Histórico de conversas")
        
        sessoes_antigas = carregar_sessoes_api()
        
        if not sessoes_antigas:
            st.info("Nenhuma conversa salva ainda.")
        else:
            for sessao_id in sessoes_antigas:
                # Cria um botão para cada sessão
                if st.button(f"📄 {sessao_id[:8]}...", key=sessao_id, use_container_width=True):
                    # Se o usuário clicar, mudamos o chat ativo
                    st.session_state.chat_id = sessao_id
                    
                    # Removemos as mensagens atuais do estado para forçar o chat.py a 
                    # puxar o histórico dessa sessão específica no banco
                    if "messages" in st.session_state:
                        del st.session_state["messages"]
                        
                    st.rerun() # Atualiza a página para carregar o chat selecionado
        
        # Spacer natural usando CSS / markdown para empurrar footer
        st.markdown("<br><br><br><br><br><br>", unsafe_allow_html=True)
        
        st.divider()
        # Footer
        st.markdown("⚙️ **Configurações**")
        st.caption("v1.0.0 - Apenas UI")