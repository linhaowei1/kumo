import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.renewable_energy_data import Truths, Actions, Outcomes

@registry.register_environment("RenewableEnergyEnv")
class RenewableEnergyEnv(BaseEnv):
    
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
Please create a renewable energy assessment guidebook that outlines different renewable energy technologies and methods for evaluating their suitability for a specific location according to the provided information.

Renewable Energy Technologies: {truths}

Assessment Methods: {actions}

Exclusion Criteria: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Exclusion Criteria” represent the renewable energy technologies that must be **excluded or ruled out** when the corresponding state is observed.

For example,

    If the state of "Resource Assessment" is:
    
    "Resource Assessment":
    {
        "states": {
            "Outcome_1": ["Technology1", "Technology2"],
            "Outcome_2": ["Technology3", "Technology4"]
        }
    }
        
    This means:
    - When “Resource Assessment” is conducted and “Outcome_1” is observed, “Technology1” and Technology2 are ruled out (i.e., they are eliminated as possibilities).
    - This exclusion approach is applied instead of confirming or indicating which technologies are valid or related.

2. Explain the renewable energy technologies and assessment methods in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rule should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify the most suitable renewable energy technology for a location based on assessment outcomes. Each round, you'll be presented with a list of potential renewable energy technologies and available assessment methods. You need to systematically rule out technologies that do not match the observed outcomes until only one plausible technology remains. Your objective is to identify the technology accurately in the fewest steps.

How to Play:

(1) View the list of potential renewable energy technologies and available assessment methods.

(2) Choose one assessment method from the list to perform.

(3) Use the outcomes to eliminate technologies that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the optimal technology.

This is the initial state of the game:

Renewable Energy Technologies: {self.env.truth_space}

Assessment Methods: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is a renewable energy assessment guidebook to introduce the technologies and assessment methods:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt