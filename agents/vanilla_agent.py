import copy

from agents.base_agent import BaseAgent
from common.registry import registry


@registry.register_agent("VanillaAgent")
class VanillaAgent(BaseAgent):
    
    def __init__(self, T, A, K, llm_model, system_prompt):
        
        super().__init__(T, A, K, llm_model, system_prompt)
        
        self.llm_model = llm_model
        self.system_prompt = system_prompt
        
        self.messages = self.llm_model.get_init_message(self.system_prompt)
        
        self.observations = []
        self.outputs = []

    def reset(self, T=None, A=None, K=None, system_prompt=None):
        
        if not (T is None or A is None or K is None or system_prompt is None):
            super().reset(T, A, K)
            self.system_prompt = system_prompt
        
        self.messages = self.llm_model.get_init_message(self.system_prompt)
        self.observations = []
    
    def response(self, observation):
        
        # On the first turn, the agent needs to select a diagnostic test

        self.observations.append(observation)
        if observation is not None:
            self.messages.append({'role': 'user', 'content': f"Observation from previous action: {observation}"})

        messages = copy.deepcopy(self.messages)

        cur_inst = f"At this round, You need to select an `action_name` from the list: {self.A} or predict a `truth_name` from the list: {self.T}. \nReason and end your response with the format '<ANSWER> ${{action_name}} </ANSWER>' or '<ANSWER> ${{truth_name}} </ANSWER>'."
        if observation is not None:
            messages[-1]["content"] += "\n\n" + cur_inst
        else:
            self.messages.append({"role": "user", "content": "Begin the game."})
            messages.append({"role": "user", "content": cur_inst})
        
        # call the LLM to generate the response
        outputs = self.llm_model.call_llm(messages, return_dict=True)
        
        answer = self.parse_output(outputs['generated_text'])

        # self.outputs.append(outputs['generated_text'])
        self.messages.append({'role': 'assistant', 'content': outputs['generated_text']})

        print("-----------------")
        print(outputs['generated_text'])

        if answer in self.A or answer in self.T:
            return answer, outputs
        else:
            # import pdb; pdb.set_trace()
            return None, outputs
        
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