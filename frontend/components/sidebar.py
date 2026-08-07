"""
Componente de interface para a barra lateral (Sidebar).
"""
import streamlit as st
from utils.state_manager import clear_chat
import requests

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
                
                # O chat_id é algo como "Olá faça um resumo... - 4b2a"
                # Vamos dividir pelo traço e pegar só a primeira parte para o título
                if " - " in sessao_id:
                    titulo_limpo = sessao_id.split(" - ")[0]
                else:
                    titulo_limpo = sessao_id[:25] # Backup de segurança
                
                # Renderiza o botão com o título limpo
                if st.button(f" {titulo_limpo}", key=sessao_id, width="stretch"):
                    st.session_state.chat_id = sessao_id
                    st.session_state.deve_carregar_historico = True
                    
                    if "messages" in st.session_state:
                        del st.session_state["messages"]
                        
                    st.rerun()
        
        # Spacer natural usando CSS / markdown para empurrar footer
        st.markdown("<br><br><br><br><br><br>", unsafe_allow_html=True)
        
        st.divider()
        # Footer
        st.markdown("⚙️ **Configurações**")
        st.caption("v1.0.0 - Apenas UI")