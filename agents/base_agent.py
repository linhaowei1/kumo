import random
from abc import ABC, abstractmethod

class BaseAgent:
    
    def __init__(self, T, A, K, llm_model, system_prompt):
        
        self.T = T
        self.A = A
        self.K = K
        
    def response(self, observation):
        
        # a simple agent that randomly chooses to predict or call an action
        response_type = random.choice(["predict", "call_action"])
        if response_type == "predict":
            return random.choice(self.T)
        else:
            return random.choice(self.A)
    
    def reset(self, T, A, K):
            
        self.T = T
        self.A = A
        self.K = K