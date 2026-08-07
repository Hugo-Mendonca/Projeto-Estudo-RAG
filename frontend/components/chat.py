"""
Componente principal do chat, gerenciando exibição e input.
"""
import streamlit as st
from components.message import render_message
import requests
import uuid
from datetime import datetime, timezone

def salvar_mensagem_api(chat_id: str,titulo: str, role: str, text_content: str, fontes: list = None):
    """
    Função auxiliar para salvar as mensagens e fontes no banco Elasticsearch.
    """
    fontes_limpas = []
    if fontes:
        for f in fontes:
            try:
                score_val = float(f.get("score", 0.0))
            except:
                score_val = 0.0
                
            fontes_limpas.append({
                "origem": str(f.get("origem", "Desconhecida")),
                "score": score_val,
                "conteudo": str(f.get("conteudo", ""))
            })
            
    dados = {
        "chat_id": chat_id,
        "title": titulo,
        "role": role,
        "date": datetime.now(timezone.utc).isoformat(), 
        "text_content": str(text_content),
        "fontes": fontes_limpas
    }
    
    try:
        resposta = requests.post("http://localhost:8000/api/chat/history", json=dados)
        
        if resposta.status_code != 200:
            # Imprime OBRIGATORIAMENTE no terminal do Streamlit
            print("\n" + "="*50)
            print("🚨 ERRO AO SALVAR NO ELASTICSEARCH")
            print(f"Status Code: {resposta.status_code}")
            print(f"Resposta da API: {resposta.text}")
            print("="*50 + "\n")
            
            # Tenta mostrar um aviso flutuante na interface
            st.toast("Falha ao salvar a mensagem no banco! Veja o terminal.", icon="❌")
            
    except Exception as e:
        print(f"\n🚨 ERRO DE CONEXÃO COM A API: {str(e)}\n")
        
        
def carregar_mensagens_do_banco(chat_id: str):
    """Busca as mensagens de uma sessão específica na API."""
    try:
        resposta = requests.get(
            "http://localhost:8000/api/chat/history",
            params={"chat_id": chat_id} 
        )
        if resposta.status_code == 200:
            return resposta.json().get("mensagens", [])
    except Exception as e:
        print(f"Erro ao buscar mensagens do backend: {e}")
    return []

def render_chat() -> None:
    # URL do nosso backend
    API_URL = "http://localhost:8000/api/chat"
    
# 1. Verifica se a bandeira foi levantada pela sidebar
    if st.session_state.get("deve_carregar_historico"):
        print(f"\n[DEBUG] 🚩 Bandeira ativada! Buscando chat_id: {st.session_state.chat_id}")
        st.session_state.messages = carregar_mensagens_do_banco(st.session_state.chat_id)
        
        # Abaixa a bandeira para não ficar recarregando em todo clique na tela
        st.session_state.deve_carregar_historico = False 
        
    # 2. Se não tem bandeira e a lista não existe, é uma conversa nova
    elif "messages" not in st.session_state:
        st.session_state.messages = []
        
    # 3. Garantia do chat_id
    if "chat_id" not in st.session_state:
        st.session_state.chat_id = None
        
    """
    Renderiza o histórico de mensagens e o campo fixo de entrada na parte inferior,
    agora integrado com a API do FastAPI.
    """
    # Container para isolar mensagens do input
    chat_container = st.container()
    
    with chat_container:
        # Renderiza todo o histórico salvo na sessão
        for msg in st.session_state.messages:
            
            # 1. Renderiza o balão de texto normalmente
            render_message(msg["role"], msg["content"])
            
            # 2. A MÁGICA ACONTECE AQUI: Renderiza os chunks se for mensagem da IA
            if msg["role"] == "assistant" and msg.get("fontes"):
                
                # Ordena do maior score para o menor (decrescente)
                fontes_ordenadas = sorted(msg["fontes"], key=lambda x: float(x.get("score", 0.0)), reverse=True)
                
                st.markdown("<br><b>📚 Documentos Consultados:</b>", unsafe_allow_html=True)
                
                # Desenha cada documento
                for i, fonte in enumerate(fontes_ordenadas, 1):
                    origem = fonte.get("origem", "Fonte Desconhecida")
                    
                    # FORÇA o score a virar um número decimal
                    try:
                        score = float(fonte.get("score", 0.0))
                    except:
                        score = 0.0
                        
                    conteudo = fonte.get("conteudo", "Conteúdo indisponível.")
                    
                    st.markdown(f"**Documento {i}: {origem}** | Score: `{score:.4f}`")
                    
                    # TRUQUE DEFINITIVO PARA OS PARÁGRAFOS
                    conteudo_str = str(conteudo)
                    # 1. Converte quebras falsas (\\n) do JSON em quebras reais (\n)
                    conteudo_str = conteudo_str.replace('\\n', '\n')
                    # 2. Troca todas as quebras por duplas para o Markdown desgrudar
                    conteudo_formatado = conteudo_str.replace('\n', '\n\n')
                    
                    st.markdown(f"> {conteudo_formatado}")
                
                # Linha para separar da próxima pergunta
                st.divider()

    # st.chat_input fica ancorado automaticamente na parte inferior
    if prompt := st.chat_input("Faça uma pergunta sobre o relatório..."):
        
        # --- MUDANÇA 2: Geração do Título/chat_id na primeira pergunta ---
        if not st.session_state.chat_id:
            titulo_pergunta = prompt[:30].strip()
            codigo_unico = uuid.uuid4().hex[:4]
            # O chat_id vira algo como: "Qual o nome do projeto?... - 1a2b"
            st.session_state.chat_title = f"{titulo_pergunta}..."
            st.session_state.chat_id = f"{titulo_pergunta}... - {codigo_unico}"
            
        titulo_atual = st.session_state.get("chat_title", st.session_state.chat_id)        
        # 1. Adiciona e exibe mensagem do usuário
        st.session_state.messages.append({"role": "user", "content": prompt})
        with chat_container:
            render_message("user", prompt)
            
            # --- MUDANÇA 3: Dispara o salvamento da mensagem do usuário ---
            salvar_mensagem_api(st.session_state.chat_id, titulo_atual, "user", prompt)            
            
            # 2. Comunicação com o Backend
            with st.spinner("Analisando os documentos e gerando resposta..."):
                texto_resposta = "Ocorreu um erro ao processar a resposta."
                fontes = []
                try:
                    # Preparamos o pacote de dados (payload)
                    payload = {"pergunta": prompt}
                    
                    # Disparamos a requisição POST para o FastAPI
                    resposta_api = requests.post(API_URL, json=payload)
                    
                    # Verificamos se o servidor respondeu com sucesso (HTTP 200)
                    if resposta_api.status_code == 200:
                        dados = resposta_api.json()
                        
                        # Pegamos o que vier dentro de "resposta"
                        pacote_interno = dados.get("resposta", "")
                        
                        # TRAVA DE SEGURANÇA:
                        # Se for um dicionário (a boneca russa com as fontes)
                        if isinstance(pacote_interno, dict):
                            texto_resposta = pacote_interno.get("resposta", "Texto não encontrado no JSON")
                            fontes = pacote_interno.get("fontes_utilizadas", [])
                        
                        # Se o backend mandou apenas o texto direto (string)
                        else:
                            texto_resposta = str(pacote_interno)
                            fontes = []
                        
                except requests.exceptions.ConnectionError:
                    # Se o servidor do FastAPI estiver desligado
                    texto_resposta = "Erro de conexão: O backend parece estar offline. Verifique se o Uvicorn está rodando."
                except Exception as e:
                    # Captura qualquer outro erro inesperado no frontend
                    texto_resposta = f"Ocorreu um erro interno no chat: {str(e)}"
                
            # 3. Adiciona a resposta real (ou erro) da IA ao estado da sessão
            st.session_state.messages.append({
                "role": "assistant", 
                "content": texto_resposta,
                "fontes": fontes
            })
            
            # --- MUDANÇA 4: Dispara o salvamento da mensagem da IA (com as fontes) ---
            salvar_mensagem_api(st.session_state.chat_id, titulo_atual, "assistant", texto_resposta, fontes)
            
            # 4. Reconstrói a tela para renderizar a nova mensagem da IA
            st.rerun()