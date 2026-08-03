"""
Componente principal do chat, gerenciando exibição e input.
"""
import streamlit as st
import time
from components.message import render_message

def render_chat() -> None:
    """
    Renderiza o histórico de mensagens e o campo fixo de entrada na parte inferior,
    simulando a experiência de resposta (spinner + delay).
    """
    # Container para isolar mensagens do input
    chat_container = st.container()
    
    with chat_container:
        for msg in st.session_state.messages:
            render_message(msg["role"], msg["content"])

    # st.chat_input fica ancorado automaticamente na parte inferior no Streamlit
    if prompt := st.chat_input("Faça uma pergunta sobre o relatório..."):
        
        # 1. Adiciona e exibe mensagem do usuário
        st.session_state.messages.append({"role": "user", "content": prompt})
        with chat_container:
            render_message("user", prompt)
            
            # 2. Indicador de processamento fictício
            with st.spinner("Consultando informações..."):
                time.sleep(1) # Delay simulado
                
            # 3. Adiciona e exibe mensagem simulada da IA
            mock_response = "Resposta simulada. Aqui futuramente será integrada a resposta do pipeline RAG."
            st.session_state.messages.append({"role": "assistant", "content": mock_response})
            
            # st.rerun() limpa o input e reconstrói a tela de baixo para cima mantendo a estabilidade
            st.rerun()