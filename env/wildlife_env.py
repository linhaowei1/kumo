import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.wildlife_data import Truths, Actions, Outcomes

@registry.register_environment("WildlifeEnv")
class WildlifeEnv(BaseEnv):
    
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
Please write a wildlife conservation strategy guide that introduces the endangered animal species and wildlife survey methods in natural language according to the following information.

Endangered Animal Species: {truths}

Wildlife Surveys: {actions}

Exclusion Criteria: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Exclusion Criteria” represent the animal species that must be **excluded or ruled out** when the corresponding survey observation is recorded.

For example,

    If the state of "SurveyMethod1" is:
    
    "SurveyMethod1":
    {
        "states": {
            "Observation_1": ["Species1", "Species2"],
            "Observation_2": ["Species3", "Species4"]
        }
    }
        
    This means:
    - When “SurveyMethod1” is performed and “Observation_1” is recorded, “Species1” and Species2 are ruled out (i.e., they are eliminated as possibilities).
	- This exclusion approach is applied instead of confirming or indicating which species are valid or related.

2. Explain the animal species and survey methods in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rule should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify an endangered animal species in a reserve based on survey observations. Each round, you'll be presented with a list of possible species and available survey methods. You need to systematically rule out species that do not match the observed data until only one plausible species remains. Your objective is to identify the species accurately in the fewest steps.

How to Play:

(1) View the list of possible animal species and available survey methods.

(2) Choose one survey method from the list to perform.

(3) Use the observations to eliminate species that don't match the recorded results.

(4) Repeat steps 2 and 3 until you can confidently identify the species.

This is the initial state of the game:

Animal Species: {self.env.truth_space}

Survey Methods: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is a wildlife conservation strategy guide to introduce the animal species and survey methods:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt