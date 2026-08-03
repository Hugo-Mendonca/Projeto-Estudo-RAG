"""
Componente de interface para a barra lateral (Sidebar).
"""
import streamlit as st
from utils.state_manager import clear_chat

def render_sidebar() -> None:
    """Renderiza os elementos visuais e de navegação da barra lateral."""
    with st.sidebar:
        # Logo e Nome
        st.markdown("### 💠 Logo Placeholder")
        st.markdown("## Sistema RAG")
        st.write("") # Espaçamento
        
        # Botão nova conversa
        if st.button("➕ Nova conversa", use_container_width=True):
            clear_chat()
            st.rerun()
            
        st.divider()
        
        # Histórico Fictício
        st.markdown("#### Histórico de Conversas")
        st.button("📄 Relatório Q3 2023", use_container_width=True, type="tertiary")
        st.button("💰 Análise de Custos", use_container_width=True, type="tertiary")
        st.button("📝 Contratos Ativos", use_container_width=True, type="tertiary")
        
        # Spacer natural usando CSS / markdown para empurrar footer
        st.markdown("<br><br><br><br><br><br>", unsafe_allow_html=True)
        
        st.divider()
        # Footer
        st.markdown("⚙️ **Configurações**")
        st.caption("v1.0.0 - Apenas UI")