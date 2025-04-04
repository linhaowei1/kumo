import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.license_data import Truths, Actions, Outcomes

@registry.register_environment("LicenseEnv")
class LicenseEnv(BaseEnv):
    
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
Please write a software licensing analysis guidebook that introduces the following software licenses and analysis methods in natural language according to the following information.

Software Licenses: {truths}

Analysis Methods: {actions}

Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Outcomes” represent the software licenses that must be **excluded or ruled out** when the corresponding state is observed.

For example,

    If the state of "License Term Analysis" is:
    
    "License Term Analysis":
    {
        "states": {
            "Outcome_1": ["License1", "License2"],
            "Outcome_2": ["License3", "License4"]
        }
    }
        
    This means:
    - When “License Term Analysis” is performed and “Outcome_1” is observed, “License1” and License2 are ruled out (i.e., they are eliminated as possibilities).
	- This exclusion approach is applied instead of confirming or indicating which licenses are valid or related.

2. Explain the software licenses and analysis methods in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rule should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify a software license based on analysis outcomes. Each round, you'll be presented with a list of possible software licenses and available analysis methods. You need to systematically rule out software licenses that do not match the observed outcomes until only one plausible license remains. Your objective is to identify the license accurately in the fewest steps.

How to Play:

(1) View the list of possible software licenses and available analysis methods.

(2) Choose one analysis method from the list to perform.

(3) Use the outcomes to eliminate software licenses that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the license.

This is the initial state of the game:

Software Licenses: {self.env.truth_space}

Analysis Methods: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is a software licensing analysis guidebook to introduce the software licenses and analysis methods:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt