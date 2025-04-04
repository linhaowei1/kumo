from .openai import OPENAI
from .anthropic import ANTHROPIC
from common.registry import registry

__all__ = [
    "OPENAI",
    'ANTHROPIC'
]

def load_llm(name, config):
    llm = registry.get_llm_class(name)(config)
    
    return llm
    