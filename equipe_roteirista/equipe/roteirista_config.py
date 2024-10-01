from typing import Dict, Any
from .agente_config import AgenteConfig

def default_config() -> Dict[str, Any]:
    """
    Função que retorna a configuração padrão para o roteirista.

    Retorna:
        Dict[str, Any]: Um dicionário contendo 'max_rpm' e a lista 'agente_config'.
    """    
    return {        
        'agente_config': [AgenteConfig(model_name='groq/llama3-70b-8192', max_rpm=30) for _ in range(3)]
    }
