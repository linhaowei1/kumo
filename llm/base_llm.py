from abc import ABC, abstractmethod
from common.registry import registry

class BASELLM:
    
    def __init__(self, llm_config):

        self.model = llm_config.model_name_or_path
    
    @abstractmethod
    def call_llm(self, messages, num_trials=5, return_dict=False):
        pass
    
    def process_message(self, messages):
        if not isinstance(messages, list):
            messages = [
                {"role": "user", "content": messages}
            ]
        if 'gemma' in self.model:
            role = 'user'
            new_message = []
            for i, message in enumerate(messages):
                if message['role'] != role:
                    # merge the messages into the last message
                    new_message[-1]['content'] += '\n' + message['content']
                else:
                    new_message.append(message)
                
                role = 'assistant' if role == 'user' else 'user'
        
            return new_message

        return messages
    
    def get_init_message(self, system_prompt):
        if self.model == 'o1-preview' or self.model == 'o1-mini' or 'gemma' in self.model or 'claude' in self.model:
            return [{'role': 'user', 'content': system_prompt}]
    
        return [{'role': 'system', 'content': system_prompt}]