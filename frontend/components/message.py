"""
Componente de interface para renderização dos balões de mensagens.
"""
import streamlit as st

def render_message(role: str, content) -> None:
    """
    Renderiza um balão de mensagem no formato HTML/CSS.
    """
    
    # 1. Tratamento de segurança: garante que vamos trabalhar com uma string
    if isinstance(content, dict):
        # Se vier um dicionário, tenta pegar a chave 'resposta', se não achar, converte o dict para string
        texto_limpo = content.get("resposta", str(content))
    else:
        # Se já for string (que é o correto/esperado), apenas garante o tipo
        texto_limpo = str(content)

    # 2. Escapa quebras de linha para renderizar corretamente no HTML
    content_html = texto_limpo.replace("\n", "<br>")

    # 3. Renderiza o HTML dependendo de quem enviou
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