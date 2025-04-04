import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.fashion_data import Truths, Actions, Outcomes

@registry.register_environment("FashionEnv")
class FashionEnv(BaseEnv):
    
    def __init__(self, datapoint=None):
        self.all_truths = Truths      #
        self.all_actions = Actions    #
        self.ta_mapping = Outcomes
    
        self.env = None
        
        if datapoint is not None:
            self.reset(datapoint)

    
    def get_knowledge_book_prompt(self, truths, actions, ta_mapping):
        
        knowledge_book_prompt = \
        f"""
Please write a fashion analysis guidebook that introduces the following fashion styles or movements and assessments in natural language according to the following information.

Fashion styles or movements: {truths}

Assessments: {actions}

Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Outcomes” represent the fashion styles or movements that must be **excluded or ruled out** when the corresponding state is observed.

For example,

    If the state of "Assessment1" is:
    
    "Assessment1":
    {
        "states": {
            "Outcome_1": ["Style1", "Style2"],
            "Outcome_2": ["Style3", "Style4"]
        }
    }
        
    This means:
    - When “Assessment1” is performed and “Outcome_1” is observed, “Style1” and “Style2” are ruled out (i.e., they are eliminated as possibilities).
	- This exclusion approach is applied instead of confirming or indicating which styles are valid or related.

2. Explain the fashion styles and assessments in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rule should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify a fashion style or movement based on assessment outcomes. Each round, you'll be presented with a list of possible fashion styles and available assessments. You need to systematically rule out fashion styles or movements that do not match the observed outcomes until only one plausible style remains. Your objective is to identify the style accurately in the fewest steps.

How to Play:

(1) View the list of possible fashion styles or movements and available assessments.

(2) Choose one assessment from the list to perform.

(3) Use the outcomes to eliminate styles that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the style.

This is the initial state of the game:

Fashion Styles or Movements: {self.env.truth_space}

Assessments: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is a fashion analysis guidebook to introduce the fashion styles and assessments:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt