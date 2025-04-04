import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.language_data import Truths, Actions, Outcomes

@registry.register_environment("LanguageEnv")
class LanguageEnv(BaseEnv):
    
    def __init__(self, datapoint=None):
        self.all_truths = Truths      # Ancient languages
        self.all_actions = Actions    # Linguistic pattern analysis and cipher decoding
        self.ta_mapping = Outcomes
    
        self.env = None
        
        if datapoint is not None:
            self.reset(datapoint)

    
    def get_knowledge_book_prompt(self, truths, actions, ta_mapping):
        
        knowledge_book_prompt = \
        f"""
Please create a linguistic analysis guidebook that introduces the following ancient languages, linguistic patterns, and cipher decoding techniques in natural language according to the following information.

Ancient Languages: {truths}

Linguistic Patterns and Cipher Decoding Techniques: {actions}

Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Outcomes” represent the ancient languages that must be **excluded or ruled out** when the corresponding pattern or decoding is observed.

For example,

    If the pattern/decoding observation is:
    
    "Pattern1":
    {
        "states": {
            "Outcome_1": ["Language1", "Language2"],
            "Outcome_2": ["Language3", "Language4"]
        }
    }
        
    This means:
    - When “Pattern1” is analyzed and “Outcome_1” is observed, “Language1” and "Language2" are ruled out (i.e., they are eliminated as possibilities).
    - This exclusion approach is applied instead of confirming or indicating which languages are valid or related.

2. Explain the languages, patterns, and techniques in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rule should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This challenge tasks you to identify a lost ancient language used in an ancient manuscript based on linguistic patterns and decoding techniques. Each round, you'll be presented with a list of possible ancient languages and available analysis techniques. You need to systematically rule out languages that do not match the observed patterns or decoding outcomes until only one plausible language remains. Your objective is to identify the language accurately in the fewest steps.

How to Play:

(1) View the list of possible ancient languages and available analysis techniques.

(2) Choose one technique from the list to perform.

(3) Use the outcomes to eliminate languages that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the language.

This is the initial state of the challenge:

Ancient Languages: {self.env.truth_space}

Analysis Techniques: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is a linguistic analysis guidebook to introduce the languages and analysis techniques:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt