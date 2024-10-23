import pysqlite3
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import streamlit as st
from datetime import datetime
import sys
from equipe.roteirista_execute import RoteiristaController
import yaml

# Config
st.set_page_config(layout="centered", page_title="Roteirizador", page_icon="🎬")
st.title("🎥 Roteirizador")

# Definição dos modelos e seus custos
MODELOS = {
    "gpt-4o-2024-08-06": {"prompt": 2.50, "completion": 10.00},
    "GPT-4o mini": {"prompt": 0.15, "completion": 0.60},
    "o1-preview": {"prompt": 15.00, "completion": 60.00},
    "o1-mini": {"prompt": 3.00, "completion": 12.00},
    "gemini-1.5-flash": {"prompt": 0.15, "completion": 0.60},
    "gemini-1.5-pro": {"prompt": 7.00, "completion": 21.00},
    "gemini-1.0-pro": {"prompt": 0.50, "completion": 1.50},
    "grog-Llama 3.1 70B": {"prompt": 0.59, "completion": 0.79},
    "groq-Llama 3.1 8B": {"prompt": 0.05, "completion": 0.08},
}

# Load the YAML file
with open('equipe_roteirista/texto_base_examples.yaml', 'r') as file:
    texto_base_examples = yaml.safe_load(file)

# Initial State
if 'texto_base' not in st.session_state:
    st.session_state['texto_base'] = ""
if 'texto_roteirizado' not in st.session_state:
    st.session_state['texto_roteirizado'] = ""
if 'token_usage' not in st.session_state:
    st.session_state['token_usage'] = None
if 'historico' not in st.session_state:
    st.session_state['historico'] = []
if 'tasks_output' not in st.session_state:
    st.session_state['tasks_output'] = []
if 'show_input' not in st.session_state:
    st.session_state['show_input'] = True
if 'total_tokens' not in st.session_state:
    st.session_state['total_tokens'] = 0
if 'total_prompt_tokens' not in st.session_state:
    st.session_state['total_prompt_tokens'] = 0
if 'total_completion_tokens' not in st.session_state:
    st.session_state['total_completion_tokens'] = 0
if 'total_successful_requests' not in st.session_state:
    st.session_state['total_successful_requests'] = 0
if 'modelo_selecionado' not in st.session_state:
    st.session_state['modelo_selecionado'] = "GPT-4o mini"

def calcular_custo(prompt_tokens, completion_tokens, modelo):
    custo_prompt = (prompt_tokens / 1_000_000) * MODELOS[modelo]["prompt"]
    custo_completion = (completion_tokens / 1_000_000) * MODELOS[modelo]["completion"]
    return custo_prompt + custo_completion

def display_token_usage():
    modelo = st.session_state.modelo_selecionado
    custo_total = calcular_custo(st.session_state.total_prompt_tokens, st.session_state.total_completion_tokens, modelo)
           
    st.metric("Custo Estimado", f"${custo_total:.4f}")    
    
    col1_token, col2_token, col3_token = st.columns(3)
    col1_token.metric(label="Tokens do Prompt", value=f"{st.session_state.total_prompt_tokens:,}")
    col2_token.metric(label="Tokens da Resposta", value=f"{st.session_state.total_completion_tokens:,}")
    col3_token.metric(label="Total de Tokens", value=f"{st.session_state.total_tokens:,}")

def analisar_texto(texto):
    palavras = texto.split()
    return {
        "num_palavras": len(palavras),
        "tempo_leitura": len(palavras) // 200  # Assumindo uma velocidade média de leitura de 200 palavras por minuto
    }
    
# Dessa forma evitamos o erro WARNING: Overriding of current TracerProvider is not allowed    
@st.cache_resource
def criar_roteirizador():
    return RoteiristaController()

controller = criar_roteirizador()

def main():
    # Sidebar       
    st.sidebar.info("""        
        O **Roteirizador** é uma ferramenta que converte textos em roteiros 
        detalhados e criativos, utilizando inteligência artificial para 
        criar narrativas envolventes "e" ~~diálogos dinâmicos entre personagens~~.
    """) 
   
    # Condiguração Roteirizador
    if st.session_state.show_input:
        st.subheader("Configurar Roteirizador")
        
        # Add a selectbox for choosing predefined examples
        example_options = ["Escreva seu próprio texto"] + [example['titulo'] for example in texto_base_examples['exemplos']]
        selected_example = st.selectbox("Escolha um exemplo ou escreva seu próprio texto", options=example_options)
        
        if selected_example == "Escreva seu próprio texto":
            texto_base = st.text_area(label="Digite ou cole seu texto aqui", height=200, key="input_text")
        else:
            selected_text = next(example['texto'] for example in texto_base_examples['exemplos'] if example['titulo'] == selected_example)
            texto_base = st.text_area(label="Digite ou cole seu texto aqui", value=selected_text, height=200, key="input_text")
        
        analise_base = analisar_texto(texto_base)
        st.write(f"Caracteres: {len(texto_base)} | Palavras: {analise_base['num_palavras']}")

        # Process button
        if st.button("Roteirizar", type="primary"):
            with st.spinner("Processando..."):
                crew_result = controller.run({
                    'texto_base': texto_base,
                })
            st.session_state.texto_roteirizado = crew_result.raw
            st.session_state.token_usage = crew_result.token_usage
            st.session_state.tasks_output = crew_result.tasks_output
            
            # Atualizar tokens acumulados
            st.session_state.total_tokens += crew_result.token_usage.total_tokens
            st.session_state.total_prompt_tokens += crew_result.token_usage.prompt_tokens
            st.session_state.total_completion_tokens += crew_result.token_usage.completion_tokens
            st.session_state.total_successful_requests += crew_result.token_usage.successful_requests
            
            st.session_state.historico.append({
                "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "texto_base": texto_base,
                "roteiro": crew_result.raw,
                "tasks_output": crew_result.tasks_output,
                "token_usage": {
                    "total_tokens": crew_result.token_usage.total_tokens,
                    "prompt_tokens": crew_result.token_usage.prompt_tokens,
                    "completion_tokens": crew_result.token_usage.completion_tokens,
                    "successful_requests": crew_result.token_usage.successful_requests
                },
            })
            st.session_state.show_input = False
            st.rerun()  # Rerun to update sidebar
    else:
        if st.button("Novo Roteiro", icon="🧪"):
            st.session_state.show_input = True
            st.rerun()

    if not st.session_state.show_input and st.session_state.tasks_output:
        # Resultados Roteirizador
        st.subheader("Resultados das Tarefas")
        
        # Criar tabs para cada tarefa
        task_agent = [task.agent for task in st.session_state.tasks_output]
        tabs = st.tabs(task_agent)
        
        for i, tab in enumerate(tabs):
            with tab:
                task = st.session_state.tasks_output[i]
                st.write(f"**Resumo:** {task.summary}")
                st.text_area("Resultado", value=task.raw, height=300, key=f"task_output_{i}")

        st.divider()
        
        st.subheader("Roteiro Final")
        texto_roteirizado = st.text_area("Roteiro gerado", value=st.session_state.texto_roteirizado, height=300, key="output_text")
        analise_roteiro = analisar_texto(texto_roteirizado)
        st.write(f"Caracteres: {len(texto_roteirizado)} | Palavras: {analise_roteiro['num_palavras']} | Tempo estimado de leitura: {analise_roteiro['tempo_leitura']} minutos")

        # Download button
        if st.session_state.texto_roteirizado:
            st.download_button(
                label="Baixar Roteiro",
                icon="🪄",
                data=st.session_state.texto_roteirizado,
                file_name=f"roteiro_gerado_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                mime="text/plain"
            )

        st.divider()

        # Gasto de Tokens   
        # Seleção do modelo
        st.subheader("Uso de Tokens (Acumulado)")
        st.session_state.modelo_selecionado = st.selectbox(
            "Selecione o modelo para calcular custo",
            options=list(MODELOS.keys()),
        )
        
        # Display Token Usage KPIs in sidebar
        display_token_usage()
        
        st.divider()

    # Histórico
    if st.session_state.historico:
        st.subheader("Histórico de Roteiros")
        for i, item in enumerate(reversed(st.session_state.historico)):
            with st.expander(f"Roteiro {len(st.session_state.historico) - i}: {item['data']}"):
                st.text_area("Texto Base", item['texto_base'], height=100, disabled=True, key=f"texto-base-{i}")
                st.text_area("Roteiro Gerado", item['roteiro'], height=200, key=f"roteiro-gerado-{i}")               
                st.write("**Uso de Tokens:**")
                col1, col2, col3 = st.columns(3)
                col1.metric("Total", f"{item['token_usage']['total_tokens']:,}")
                col2.metric("Prompt", f"{item['token_usage']['prompt_tokens']:,}")
                col3.metric("Resposta", f"{item['token_usage']['completion_tokens']:,}")
                st.write(f"Requisições bem-sucedidas: {item['token_usage']['successful_requests']}")                
                st.divider()
                if 'tasks_output' in item:
                    st.subheader("Resultados das Tarefas")
                    for task in item['tasks_output']:
                        st.write(f"**Agente:** {task.agent}")
                        st.write(f"**Tarefa:** {task.name}")
                        st.text_area("Resultado", value=task.raw, height=150, disabled=True, key=f"resultado-{i}-{task.agent}")                       
                   
roteirizador_page = st.Page(main, title="Roteirizador", icon=":material/home_work:", default=True)

objetivo_page = st.Page("paginas/sobre/objetivo.py", title="Objetivo", icon=":material/info:")
visao_geral_page = st.Page("paginas/sobre/visao_geral.py", title="Visão Geral", icon=":material/description:")

pg = st.navigation({
    "Home": [roteirizador_page],
    "Sobre": [objetivo_page, visao_geral_page],
})


if __name__ == "__main__":
    pg.run()
