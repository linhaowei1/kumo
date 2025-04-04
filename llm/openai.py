from openai import OpenAI
import traceback
import sys
from common.registry import registry
from .base_llm import BASELLM
@registry.register_llm("OPENAI")
class OPENAI(BASELLM):
    
    def __init__(self, llm_config):
        
        super().__init__(llm_config)
        
        api_base = llm_config.api_base
        api_key = llm_config.api_key
        
        self.client = OpenAI(
            api_key=api_key,
            base_url=api_base,
        )

        self.model = llm_config.model_name_or_path
    
    def call_llm(self, messages, num_trials=5, return_dict=False):
        
        # check if messages are "Conversation roles must alternate user/assistant/user/assistant/..."
        messages = self.process_message(messages)
        while num_trials > 0:
            try:
                chat_completion = self.client.chat.completions.create(
                    model=self.model,
                    messages=messages
                )
                if chat_completion.choices[0].finish_reason == 'stop':
                    generated_text = chat_completion.choices[0].message.content
                    consumed_tokens = chat_completion.usage.total_tokens
                    break
                else:
                    raise ValueError(f"Unknown finish reason: {chat_completion.choices[0].finish_reason}.")                
            except Exception as e:
                if num_trials == 1:
                    print(f"Failed to call the LLM with the following error: {e}")
                    consumed_tokens = 0
                    generated_text = None
                num_trials -= 1
                continue

            
        if return_dict:
            return {
                'consumed_tokens': consumed_tokens,
                'generated_text': generated_text
            }
        
        return generated_text
    
        