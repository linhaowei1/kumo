import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.sci_fi_data import Truths, Actions, Outcomes

@registry.register_environment("SciFiEnv")
class SciFiEnv(BaseEnv):
    
    def __init__(self, datapoint=None):
        self.all_truths = Truths      # Fictional planets
        self.all_actions = Actions    # Environmental scans / atmospheric sampling
        self.ta_mapping = Outcomes    # Sci-fi outcomes mapped to observations
    
        self.env = None
        
        if datapoint is not None:
            self.reset(datapoint)

    
    def get_knowledge_book_prompt(self, truths, actions, ta_mapping):
        
        knowledge_book_prompt = \
        f"""
Please write a guidebook for determining if a planet supports life in a sci-fi setting using the following information.

Planets: {truths}

Scans and Samples: {actions}

Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Outcomes” represent the planets that must be **excluded or ruled out** when the corresponding observation is made.

For example,

    If the state of "Scan1" is:
    
    "Scan1":
    {
        "states": {
            "Outcome_1": ["Planet1", "Planet2"],
            "Outcome_2": ["Planet3", "Planet4"]
        }
    }
        
    This means:
    - When “Scan1” is performed and “Outcome_1” is observed, “Planet1” and “Planet2” are ruled out (i.e., they are eliminated as possibilities).
	- This exclusion approach is applied instead of confirming or indicating which planets are viable for life.

2. Explain the fictional planets and scans in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rule should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This exploration challenges you to identify which fictional planet supports life based on scan results. Each round, you'll be presented with a list of possible planets and available environmental scans. You need to systematically rule out planets that do not match the observed outcomes until only one plausible life-supporting planet remains. Your objective is to identify the planet accurately in the fewest steps.

How to Play:

(1) View the list of possible planets and available scans.

(2) Choose one scan from the list to perform.

(3) Use the outcomes to eliminate planets that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the planet that supports life.

This is the initial state of the exploration:

Planets: {self.env.truth_space}

Scans: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is a guidebook for determining planetary habitability:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt