from .vanilla_agent import VanillaAgent
from .base_agent import BaseAgent
from .sft_agent import SFTAgent
from common.registry import registry

__all__ = ["VanillaAgent", "BaseAgent", "SFTAgent"]


def load_agent(name, T, A, K, llm_model, system_prompt):
    agent = registry.get_agent_class(name)(T, A, K, llm_model, system_prompt)
    return agent