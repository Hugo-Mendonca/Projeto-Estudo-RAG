"""
Componente principal do chat, gerenciando exibição e input.
"""
import streamlit as st
from components.message import render_message
import requests

def render_chat() -> None:
    # URL do nosso backend
    API_URL = "http://localhost:8000/api/chat"
    
    """
    Renderiza o histórico de mensagens e o campo fixo de entrada na parte inferior,
    agora integrado com a API do FastAPI.
    """
    # Container para isolar mensagens do input
    chat_container = st.container()
    
    with chat_container:
        # Renderiza todo o histórico salvo na sessão
        for msg in st.session_state.messages:
            render_message(msg["role"], msg["content"])

    # st.chat_input fica ancorado automaticamente na parte inferior
    if prompt := st.chat_input("Faça uma pergunta sobre o relatório..."):
        
        # 1. Adiciona e exibe mensagem do usuário
        st.session_state.messages.append({"role": "user", "content": prompt})
        with chat_container:
            render_message("user", prompt)
            
            # 2. Comunicação com o Backend
            with st.spinner("Analisando os documentos e gerando resposta..."):
                try:
                    # Preparamos o pacote de dados (payload)
                    payload = {"pergunta": prompt}
                    
                    # Disparamos a requisição POST para o FastAPI
                    resposta_api = requests.post(API_URL, json=payload)
                    
                    # Verificamos se o servidor respondeu com sucesso (HTTP 200)
                    if resposta_api.status_code == 200:
                        dados = resposta_api.json()
                        # Extraímos a string da chave 'reposta' (conforme seu backend)
                        resposta_ia = dados.get("resposta", "Erro: Resposta vazia.")
                    else:
                        # Se o backend der erro 500 ou 422
                        resposta_ia = f"Ops, o servidor retornou um erro: {resposta_api.status_code}"
                        
                except requests.exceptions.ConnectionError:
                    # Se o servidor do FastAPI estiver desligado
                    resposta_ia = "Erro de conexão: O backend parece estar offline. Verifique se o Uvicorn está rodando."
                except Exception as e:
                    # Captura qualquer outro erro inesperado no frontend
                    resposta_ia = f"Ocorreu um erro interno no chat: {str(e)}"
                
            # 3. Adiciona a resposta real (ou erro) da IA ao estado da sessão
            st.session_state.messages.append({"role": "assistant", "content": resposta_ia})
            
            # 4. Reconstrói a tela para renderizar a nova mensagem da IA
            st.rerun()