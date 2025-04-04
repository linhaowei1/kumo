import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.ecological_data import Truths, Actions, Outcomes

@registry.register_environment("EcologicalEnv")
class EcologicalEnv(BaseEnv):
    
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
Please write an ecological analysis guide that introduces the following ecological niches and investigations in natural language according to the following information.

Ecological niches: {truths}

Investigations: {actions}

Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Outcomes” represent the ecological niches that must be **excluded or ruled out** when the corresponding state is observed.

For example,

    If the state of "HabitatObservation" is:
    
    "HabitatObservation":
    {
        "states": {
            "Outcome_1": ["Niche1", "Niche2"],
            "Outcome_2": ["Niche3", "Niche4"]
        }
    }
        
    This means:
    - When “HabitatObservation” is performed and “Outcome_1” is observed, “Niche1” and Niche2 are ruled out (i.e., they are eliminated as possibilities).
	- This exclusion approach is applied instead of confirming or indicating which niches are valid or related.

2. Explain the ecological niches and investigations in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rule should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify which ecological niche a newly discovered organism occupies based on investigation outcomes. Each round, you'll be presented with a list of possible ecological niches and available investigations. You need to systematically rule out ecological niches that do not match the observed outcomes until only one plausible niche remains. Your objective is to identify the niche accurately in the fewest steps.

How to Play:

(1) View the list of possible ecological niches and available investigations.

(2) Choose one investigation from the list to perform.

(3) Use the outcomes to eliminate ecological niches that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the niche.

This is the initial state of the game:

Ecological Niches: {self.env.truth_space}

Investigations: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is an ecological analysis guide to introduce the ecological niches and investigations:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt