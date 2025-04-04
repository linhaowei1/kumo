import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.political_manifesto_data import Truths, Actions, Outcomes

@registry.register_environment("PoliticalManifestoEnv")
class PoliticalManifestoEnv(BaseEnv):
    
    def __init__(self, datapoint=None):
        self.all_truths = Truths      
        self.all_actions = Actions    
        self.ta_mapping = Outcomes
    
        self.env = None
        
        if datapoint is not None:
            self.reset(datapoint)

    
    def get_knowledge_book_prompt(self, truths, actions, ta_mapping):
        
        knowledge_book_prompt = \
        f"""
Please create a political analysis guidebook that evaluates the following political ideologies and methodologies according to the provided information.

Political ideologies: {truths}

Methodologies: {actions}

Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Outcomes” represent the political ideologies that must be **excluded or ruled out** when the corresponding methodology is applied.

For example,

    If the state of "Methodology1" is:
    
    "Methodology1":
    {
        "states": {
            "Outcome_1": ["Ideologies1", "Ideologies2"],
            "Outcome_2": ["Ideologies3", "Ideologies4"]
        }
    }
        
    This means:
    - When “Methodology1” is applied and “Outcome_1” is observed, “Ideologies1” and Ideologies2 are ruled out (i.e., they are eliminated as possibilities).
	- This exclusion approach is applied instead of confirming or indicating which ideologies are valid or related.

2. Provide clear and straightforward explanations of the political ideologies and methodologies to ensure the context and relationships are easy to grasp.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rule should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify the political ideology underpinning a manifesto based on policy analysis outcomes. Each round, you'll be presented with a list of possible political ideologies and available methodologies. You need to systematically rule out political ideologies that do not align with the observed outcomes until only one plausible ideology remains. Your objective is to determine the ideology accurately in the fewest steps.

How to Play:

(1) View the list of possible political ideologies and available methodologies.

(2) Choose one methodology from the list to apply.

(3) Use the outcomes to eliminate political ideologies that don't align with the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the ideology.

This is the initial state of the game:

Political Ideologies: {self.env.truth_space}

Methodologies: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is a political analysis guidebook to introduce the political ideologies and methodologies:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt