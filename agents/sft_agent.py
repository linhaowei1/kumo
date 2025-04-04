
import copy

from agents.base_agent import BaseAgent
from common.registry import registry


@registry.register_agent("SFTAgent")
class SFTAgent(BaseAgent):
    
    def __init__(self, T, A, K, llm_model, system_prompt):
        
        super().__init__(T, A, K, llm_model, system_prompt)
        
        self.llm_model = llm_model
        self.system_prompt = system_prompt
        
        self.messages = self.llm_model.get_init_message(self.system_prompt)
        
        self.observations = []
        self.outputs = []

    def reset(self, T=None, A=None, K=None, system_prompt=None):
        
        if not (T is None or A is None or system_prompt is None):
            super().reset(T, A, K)
            self.system_prompt = system_prompt
        
        self.messages = self.llm_model.get_init_message(self.system_prompt)
        self.observations = []
    
    def response(self, observation):
        
        # On the first turn, the agent needs to select a diagnostic test

        self.observations.append(observation)
        if observation is not None:
            self.messages.append({'role': 'user', 'content': f"Observation from previous action: {observation}"})
        # call the LLM to generate the response
        outputs = self.llm_model.call_llm(self.messages, return_dict=True)
        
        answer = self.parse_output(outputs['generated_text'])

        # self.outputs.append(outputs['generated_text'])
        self.messages.append({'role': 'assistant', 'content': outputs['generated_text']})

        print("-----------------")
        print(outputs['generated_text'])

        # if answer in self.A or answer in self.T:
        return answer, outputs
        
    def parse_output(self, outputs):
        
        """
        Parse the LLM outputs to get the response.
        """
        try:
            # revise to get the final answer
            answer = outputs.split("<ANSWER>")[-1].split("</ANSWER>")[0].strip()
            if '${' in answer:
                answer = answer.split('${')[-1].split('}')[0]
        except:
            answer = None
        
        return answer