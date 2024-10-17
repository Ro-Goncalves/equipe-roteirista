import streamlit as st

st.header("Simplificando a Criação de Roteiros Inteligentes 📝")

st.markdown("""
O **Roteirizador** é uma solução desenvolvida para automatizar a criação 
de roteiros a partir de textos, utilizando modelos avançados de 
linguagem. O objetivo do projeto é demonstrar como diferentes agentes 
podem trabalhar em conjunto para gerar narrativas dinâmicas e adaptáveis, 
otimizando a experiência de roteirização para os usuários.

## Tecnologias Utilizadas 🌐
O **Roteirizador** utiliza **LLMs (Large Language Models)** por meio da 
**Groq API** para acesso e processamento dos modelos. Entre os principais 
modelos empregados estão:

- **llama 3.1 8b** 🦙: Usado nos agentes principais para análise e geração 
de conteúdo.
- **llama 3.2 11b**: Implementado no agente planejador, garantindo uma visão 
estratégica e coordenação eficiente entre as etapas de criação de roteiros.

Essa combinação de modelos permite um equilíbrio entre performance e 
qualidade, entregando resultados rápidos e precisos mesmo com modelos 
relativamente menores. 🤖💡

## Público-Alvo 🎯
O **Roteirizador** foi desenvolvido especialmente para **desenvolvedores** 
que desejam explorar e aprender sobre o funcionamento das **Equipes de Agentes 
Inteligentes** da **CrewAI**. Ele oferece uma abordagem prática para compreender 
como esses agentes interagem e se complementam para criar soluções robustas e 
escaláveis.

## Objetivos e Benefícios 💡
O projeto visa mostrar como a integração entre agentes e LLMs pode potencializar 
o desempenho e a eficiência na geração de roteiros. Entre os principais benefícios, 
destacam-se:

- **Demonstrar a eficiência da integração**: Exemplificando como agentes e LLMs podem 
atuar em conjunto para entregar resultados interessantes.
- **Guia para iniciantes**: Oferecendo um passo a passo para quem está começando no 
universo das equipes de agentes inteligentes e quer entender como implementar soluções 
similares.

---

## Planejamento e Visão Futura 🛠️
O desenvolvimento do **Roteirizador** é contínuo, e há diversas melhorias planejadas 
para torná-lo ainda mais eficaz e adaptável:

- **Melhorar a performance dos agentes** ⚡
Otimizar o desempenho dos agentes para gerar roteiros com uma qualidade ainda maior.

- **Escolha do estilo de roteiro** 🎭  
  Permitir que o usuário escolha o estilo de roteiro, como comédia, drama, épico, entre 
  outros, para adaptar a narrativa ao tom desejado.

- **Escolha do tom do roteiro** 🎙️  
  Oferecer a opção de selecionar o tom do roteiro, como formal, casual, sombrio, etc., 
  permitindo mais controle criativo sobre a saída.

- **Incluir feedback das execuções** ✅  
  Adicionar uma funcionalidade que forneça um feedback das execuções de cada tarefa dos 
  agentes.

- **Memória dos agentes** 🧠  
  ~~Desenvolver uma memória para a equipe de agentes, tornando-os mais inteligentes a cada 
  nova execução e permitindo que aprendam com os processos anteriores.~~

- **Treinamento da equipe** 📚  
  Implementar uma funcionalidade para treinar os agentes com novos dados e melhorar suas 
  habilidades ao longo do tempo.

- **Escolha do modelo de LLM** 🔄  
  Permitir ao usuário escolher o modelo de **LLM** a ser utilizado pela equipe de agentes, 
  oferecendo flexibilidade e customização para diferentes tipos de tarefas.
  
O **Roteirizador** está em constante evolução, e cada atualização busca tornar a ferramenta 
mais intuitiva e poderosa para aqueles que desejam explorar o potencial dos agentes 
inteligentes na criação de conteúdo narrativo. 🌟
""")
