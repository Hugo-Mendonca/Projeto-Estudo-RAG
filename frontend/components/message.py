"""
Componente de interface para renderização dos balões de mensagens.
"""
import streamlit as st

def render_message(role: str, content: str) -> None:
    """
    Renderiza um balão de mensagem no formato HTML/CSS.
    
    Args:
        role (str): Papel de quem enviou ('user' ou 'assistant').
        content (str): Texto da mensagem.
    """
    # Escapa quebras de linha para renderizar corretamente no HTML
    content_html = content.replace("\n", "<br>")
    
    if role == "user":
        st.markdown(f"""
        <div class="msg-container msg-user">
            <div class="bubble bubble-user">{content_html}</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="msg-container msg-ai">
            <div class="bubble bubble-ai">{content_html}</div>
        </div>
        """, unsafe_allow_html=True)