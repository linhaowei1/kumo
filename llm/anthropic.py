from anthropic import Anthropic
import traceback
import sys
from common.registry import registry
from .base_llm import BASELLM

@registry.register_llm("ANTHROPIC")
class ANTHROPIC(BASELLM):
    
    def __init__(self, llm_config):
        
        super().__init__(llm_config)
        
        api_key = llm_config.api_key

        self.client = Anthropic(
            api_key=api_key,
        )

        self.model = llm_config.model_name_or_path
    
    def call_llm(self, messages, num_trials =5, return_dict=False):
        
        # check if messages are "Conversation roles must alternate user/assistant/user/assistant/..."
        messages = self.process_message(messages)
        while num_trials > 0:
            try:
                chat_completion = self.client.messages.create(
                    model=self.model,
                    messages=messages,
                    max_tokens=4096 if 'haiku' in self.model else 8192
                )
                if chat_completion.stop_reason == 'end_turn':
                    generated_text = chat_completion.content[0].text
                    consumed_tokens = chat_completion.usage.input_tokens + chat_completion.usage.output_tokens
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
    
        