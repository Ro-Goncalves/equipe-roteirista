<div align="center">

# RG Brain - Projeto Automatize-ME - Roteirizador <!-- omit in toc -->

🎥 **Roteirizador:** Gere roteiros de forma automatizada a partir de qualquer texto com a ajuda de agentes inteligentes.

</div>

## Menu <!-- omit in toc -->

- [Descrição ✍️](#descrição-️)
- [Tecnologias Utilizadas ⚙️](#tecnologias-utilizadas-️)
- [Instalação 🛠️](#instalação-️)
  - [Pré-requisitos](#pré-requisitos)
    - [1. Instalando o Python 🐍](#1-instalando-o-python-)
    - [2. Instalando o Poetry 📦](#2-instalando-o-poetry-)
  - [Passo a Passo](#passo-a-passo)
- [Como Usar 🚀](#como-usar-)
- [Planejamento 🛠️](#planejamento-️)
- [Contribua 🤝](#contribua-)
  - [Como você pode contribuir 🚀](#como-você-pode-contribuir-)
  - [Passos para Contribuir 📝](#passos-para-contribuir-)
- [Licença 📜](#licença-)
- [Contato 📫](#contato-)
- [Contatos 📫](#contatos-)

## Descrição ✍️

Há algum tempo, imaginei o seguinte:

> **Imagine pegar uma matéria de jornal, transformá-la em um roteiro, gerar diálogos para dois personagens com base nesse roteiro, dar vida a esse diálogo narrando-o e juntar tudo isso em um vídeo.** 🎬✨

Essa é uma parte mais bonita e romantizada do que pensei. Na verdade, foi algo mais parecido com:

> **Eu poderia pegar uma matéria de jornal e transformá-la em um roteiro para uma história épica medieval, com um tom sombrio.** ⚔️🌑 Depois, criaria um diálogo entre dois personagens, usando estilos de fala de personagens conhecidos, como Spoke e Yoda, Pink e Smeagol, ou ainda Gandalf e Dumbledore. 🤔🔮 Em seguida, geraria uma voz bem grave, semelhante à de locutores, para narrar o texto. Por fim, criaria um GIF de um senhor sentado em uma cadeira, com seus netos à frente e uma lareira ao lado, narrando essa história com a voz criada. 👴🔥👶

E sim, **eu não deveria estar aprendendo a utilizar os LLMs**. 😅

O **Roteirizador** é a primeira parte desse projeto e tem como principal objetivo explorar o framework CrewAI através da **geração automatizada de roteiros**. Esse projeto une aprendizado e diversão, permitindo que eu utilize minha paixão por leitura e criatividade para transformar ideias em roteiros estruturados. 📚💡

Embora o projeto tenha um lado experimental, ele é funcional e produz roteiros com base no texto fornecido pelo usuário. A interface é simples e direta: basta inserir o texto que deseja roteirizar, clicar no botão *Roteirizar*, e o sistema de agentes inteligentes faz o resto, gerando um roteiro coerente e bem estruturado de forma automática. 🪄✨ Pode parecer mágica, mas não é, acredite em mim! 🤫

## Tecnologias Utilizadas ⚙️

- **Linguagens**:
  - **Python** 🐍: A principal linguagem de programação utilizada no desenvolvimento do projeto, escolhida por ser a *"linguagem das IAs"*.

- **Frameworks**:
  - **CrewAI** 🤖: Um framework poderoso para criar *agentes inteligentes*, permitindo a **geração automatizada de roteiros** de forma intuitiva.
  - **Streamlit** 🚀: Usado para construir a *interface do usuário* de maneira rápida e interativa, facilitando a **interação com o projeto**.

- **Serviços**:
  - **Groq API** 🌐: API utilizada para integrar funcionalidades *avançadas de inteligência artificial*, possibilitando uma **melhor performance na geração dos roteiros**.

## Instalação 🛠️

Siga os passos abaixo para configurar o projeto em seu ambiente local:

### Pré-requisitos

Antes de começar, certifique-se de ter os seguintes itens instalados:

- **Python** (versão >= 3.10 e <= 3.13) 🐍
- **Poetry** (ferramenta de gerenciamento de dependências e ambientes virtuais) 📦

#### 1. Instalando o Python 🐍

Se você ainda não tem o Python instalado, siga os passos abaixo:

- **Windows**:
  1. Acesse o site oficial do [Python](https://www.python.org/downloads/).
  2. Baixe a versão compatível (>= 3.10 e <= 3.13).
  3. Durante a instalação, marque a opção "Add Python to PATH".
  
- **macOS/Linux**:
  1. No macOS, você pode instalar via [Homebrew](https://brew.sh/):

      ```bash
      brew install python@3.10
      ```

  2. No Linux, use o gerenciador de pacotes da sua distribuição (ex: apt para Ubuntu):

     ```bash
     sudo apt-get install python3.10
     ```

#### 2. Instalando o Poetry 📦

Para instalar o Poetry, siga os passos abaixo:

- **Comando Universal (funciona no Windows/macOS/Linux)**:

  ```bash
  curl -sSL https://install.python-poetry.org | python3 -
  ```

Após a instalação, adicione o **Poetry** ao seu PATH (caso não tenha sido feito automaticamente):

- **Linux/macOS**:

  ```bash
  export PATH="$HOME/.local/bin:$PATH"
  ```

- **Windows**:

  1. Abra o *Prompt de Comando* ou *PowerShell* e digite:

     ```bash
     $Env:Path += ";C:\Users\<Seu-Usuário>\AppData\Roaming\Python\Scripts"
     ```

📌 Se você tiver problemas ao instalar o **Poetry** usando o guia acima, pode optar por instalá-lo via **pipx**. Primeiro, siga a documentação para instalar o pipx [aqui](https://github.com/pypa/pipx) e depois instale o Poetry seguindo o guia oficial [aqui](https://python-poetry.org/docs/). 🛠️

### Passo a Passo

1. **Clone o repositório** 🌀

   ```bash
   git clone https://github.com/Ro-Goncalves/equipe-roteirista.git
   cd equipe-roteirista
   ```

2. **Crie o ambiente virtual com o Poetry** 🚀

   ```bash
   poetry install
   ```

3. **Execute o projeto com o Streamlit** 🎬

   ```bash
   poetry run streamlit run equipe_roteirista/streamlit_app.py
   ```

Agora o projeto estará rodando localmente! 🏃‍♂️💨

🌐 Você pode acessar o projeto online pelo link: [equipe-roteirista.streamlit.app](https://equipe-roteirista.streamlit.app/) 🎬

## Como Usar 🚀

O processo para gerar um roteiro é simples e intuitivo. Siga os passos abaixo:

1. **Insira o Texto Base** 📝  
  No campo **"Digite ou cole seu texto base aqui"**, insira o texto que deseja transformar em um roteiro. Você pode digitar manualmente ou colar o conteúdo diretamente na caixa de texto.

2. **Clique em Roteirizar** 🎬  
  Após inserir o texto, clique no botão **"Roteirizar"**. O sistema começará a processar o texto, e você verá uma mensagem de **"Processando..."** enquanto a equipe de agentes inteligentes trabalha para gerar o roteiro.

3. **Explore as Abas de Agentes** 📂  
  Quando o processamento terminar, você poderá navegar entre as três abas principais:
  
   - **Analista de Texto**: Aqui está o resultado da análise inicial do texto.
   - **Roteirista Principal**: Esta aba exibe o roteiro principal gerado com base no seu texto.
   - **Revisor de Roteiro**: O agente Revisor garante que o roteiro está coeso e consistente.

4. **Veja o Roteiro Final** 🎥  
   Um pouco mais abaixo, você encontrará o **Roteiro Final**, que é a versão final gerada pelo último agente. Nessa seção, também há um botão para fazer o download do roteiro em formato **TXT**.

5. **Histórico de Roteiros** 📜  
   A seção de **Histórico de Roteiros** mantém os resultados de até **3 execuções** anteriores. Lá, você poderá ver o **Texto Base**, o **Roteiro Gerado**, a estimativa da quantidade de **tokens gastos** e o resultado de cada tarefa.

6. **Simulação de Custo de Tokens** 💰  
   No menu à esquerda, você encontrará a estimativa da quantidade total de **tokens acumulados**. Além disso, é possível simular o custo com base em diferentes modelos, selecionando a opção em **"Selecione o modelo para calcular custo"**.

## Planejamento 🛠️

Minha visão para o **Roteirizador** vai além da versão atual. Estou trabalhando em várias melhorias e novos recursos que irão tornar o projeto ainda mais robusto e divertido de usar. Aqui estão alguns dos próximos passos:

- **Melhorar a performance dos agentes** ⚡  
  Otimizar o desempenho dos agentes para gerar roteiros com uma qualidade ainda maior.

- **Escolha do estilo de roteiro** 🎭  
  Permitir que o usuário escolha o estilo de roteiro, como comédia, drama, épico, entre outros, para adaptar a narrativa ao tom desejado.

- **Escolha do tom do roteiro** 🎙️  
  Oferecer a opção de selecionar o tom do roteiro, como formal, casual, sombrio, etc., permitindo mais controle criativo sobre a saída.

- **Incluir feedback das execuções** ✅  
  Adicionar uma funcionalidade que forneça um feedback das execuções de cada tarefa dos agentes.

- **Memória dos agentes** 🧠  
  Desenvolver uma memória para a equipe de agentes, tornando-os mais inteligentes a cada nova execução e permitindo que aprendam com os processos anteriores.

- **Treinamento da equipe** 📚  
  Implementar uma funcionalidade para treinar os agentes com novos dados e melhorar suas habilidades ao longo do tempo.

- **Escolha do modelo de LLM** 🔄  
  Permitir ao usuário escolher o modelo de **LLM** a ser utilizado pela equipe de agentes, oferecendo flexibilidade e customização para diferentes tipos de tarefas.

## Contribua 🤝

Este é o meu primeiro projeto aberto, e estou super animado para ver até onde ele pode ir com a ajuda da comunidade! Se você achou o **Roteirizador** interessante e quer contribuir de alguma forma, aqui estão algumas maneiras de ajudar:

### Como você pode contribuir 🚀

1. **Relatar bugs** 🐛  
   Encontrou algum problema ou comportamento inesperado? Abra uma issue no repositório do GitHub e me avise para que possamos resolver juntos.

2. **Sugestões de melhorias** 💡  
   Tem uma ideia para melhorar o projeto? Fique à vontade para compartilhar! Eu adoraria ouvir suas sugestões e ver como podemos torná-lo ainda melhor.

3. **Adicionar novas funcionalidades** ✨  
   Se você tiver uma ideia de funcionalidade que pode tornar o projeto mais útil ou interessante, faça um fork, implemente a ideia e envie um pull request. Estou aberto a novas funcionalidades!

4. **Melhorias no código ou na documentação** 📚  
   Mesmo pequenos ajustes, como melhorias no código ou na clareza da documentação, são bem-vindos! Cada contribuição conta.

### Passos para Contribuir 📝

1. Faça um **fork** do repositório.
2. Crie uma **branch** para a funcionalidade ou correção:  
   `git checkout -b minha-nova-funcionalidade`
3. Faça o **commit** das suas alterações:  
   `git commit -m 'Adiciona minha nova funcionalidade'`
4. Envie para a **branch** principal:  
   `git push origin minha-nova-funcionalidade`
5. Abra um **pull request** e descreva suas alterações.

Vamos colaborar para tornar o **Roteirizador** ainda melhor! ✨

## Licença 📜

Este projeto está licenciado sob a Licença MIT. Isso significa que você pode usar, modificar e distribuir este software da maneira que preferir, desde que mantenha o aviso de copyright original. Não há garantias ou responsabilidade associadas ao uso deste software.

Leia o arquivo LICENSE para mais detalhes.

## Contato 📫

Se você tiver dúvidas ou sugestões, sinta-se à vontade para entrar em contato:

## Contatos 📫

- **LinkedIn:** 🔗 [Meu Perfil no LinkedIn](https://www.linkedin.com/in/ro-goncalves/)
- **E-mail:** ✉️ <ro.go.calves@gmail.com>
