from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from typing import List
from .agente_config import AgenteConfig

@CrewBase
class RoteiristaCrew():
    """
    Gerencia os diferentes agentes de roteiristas para a equipe.

    Atributos:
        analista_texto_config (AgenteConfig): Configuração do agente analista de texto.
        roteirista_principal_config (AgenteConfig): Configuração do roteirista principal.
        revisor_roteiro_config (AgenteConfig): Configuração do agente revisor de roteiro.
        max_rpm (int): Limite máximo de requisições por minuto (RPM).
    """

    def __init__(self, config: List[AgenteConfig]) -> None:
        """
        Inicializa a classe com a lista de configurações de agentes e o limite de RPM.

        Parâmetros:
            config (List[AgenteConfig]): Lista de configurações dos agentes.           
        
        Levanta:
            ValueError: Se o número de configurações fornecidas não for 3.          
        """
        if len(config) != 3:
            raise ValueError("A lista de configurações deve conter exatamente 3 elementos.")        
       

        self.analista_texto_config = config[0]
        self.roteirista_principal_config = config[1]
        self.revisor_roteiro_config = config[2]       

    @agent
    def analista_texto(self) -> Agent:
        """
        Retorna um agente que atua como analista de texto.
        """        
        return Agent(
            config=self.agents_config['analista_texto'],
            llm=self.analista_texto_config.model_name,
            max_rpm=self.analista_texto_config.max_rpm,
            memory=True,
            allow_delegation=False,
            verbose=True,            
        )
    
    @agent
    def roteirista_principal(self) -> Agent:
        return Agent(
            config=self.agents_config['roteirista_principal'],
            llm=self.roteirista_principal_config.model_name,
            max_rpm=self.roteirista_principal_config.max_rpm,
            memory=True,
            allow_delegation=False,
            verbose=True,
        )
        
    @agent
    def revisor_roteiro(self) -> Agent: 
        return Agent(
            config=self.agents_config['revisor_roteiro'],
            llm=self.revisor_roteiro_config.model_name,
            max_rpm=self.revisor_roteiro_config.max_rpm,
            memory=True,
            allow_delegation=True,
            verbose=True,
        )
    
    @task
    def tarefa_analise_texto(self) -> Task: 
        """
        Retorna uma tarefa que descreve a análise do texto.
        """
        return Task(
            config=self.tasks_config['tarefa_analise_texto'],
            agent=self.analista_texto(),
        )
    
    
    @task
    def tarefa_criacao_roteiro(self) -> Task:
        return Task(
            config=self.tasks_config['tarefa_criacao_roteiro'],
            agent=self.roteirista_principal(),
        )    
    
    @task
    def tarefa_revisao_roteiro(self) -> Task: 
        return Task(
            config=self.tasks_config['tarefa_revisao_roteiro'],
            agent=self.revisor_roteiro(),
        )

    @crew
    def crew(self) -> Crew:
        """
        Cria e retorna a equipe de roteiristas.
        """
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            cache=True,
            verbose=True,
            planning=True,
            planning_llm=LLM(model="groq/llama-3.2-90b-text-preview", temperature=0.35),
            memory=True,
            embedder={
                "provider": "google",
                "config": {
                    "model": 'models/text-embedding-004',
                    "task_type": "retrieval_document",
                    "title": "Embeddings for Embedchain"
                }
            }
            # long_term_memory=EnhanceLongTermMemory(
            #     storage=LTMSQLiteStorage(
            #         db_path="/my_data_dir/my_crew1/long_term_memory_storage.db"
            #     )
            # ),
            # short_term_memory=EnhanceShortTermMemory(
            #     storage=CustomRAGStorage(
            #         crew_name="my_crew",
            #         storage_type="short_term",
            #         data_dir="//my_data_dir",
            #         model=embedder["model"],
            #         dimension=embedder["dimension"],
            #     ),
            # ),
            # entity_memory=EnhanceEntityMemory(
            #     storage=CustomRAGStorage(
            #         crew_name="my_crew",
            #         storage_type="entities",
            #         data_dir="//my_data_dir",
            #         model=embedder["model"],
            #         dimension=embedder["dimension"],
            #     ),
            # ),
        )