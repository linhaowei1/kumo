import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.stellar_data import Truths, Actions, Outcomes

@registry.register_environment("StellarEnv")
class StellarEnv(BaseEnv):
    
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
Please write an astronomical analysis guidebook that introduces the following star classifications and spectral analysis techniques in natural language according to the following information.

Star Classifications: {truths}

Spectral Line Analyses: {actions}

Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Outcomes” represent the star classifications that must be **excluded or ruled out** when the corresponding state is observed.

For example,

    If the state of "SpectralLineAnalysis1" is:
    
    "SpectralLineAnalysis1":
    {
        "states": {
            "Outcome_1": ["StarType1", "StarType2"],
            "Outcome_2": ["StarType3", "StarType4"]
        }
    }
        
    This means:
    - When “SpectralLineAnalysis1” is performed and “Outcome_1” is observed, “StarType1” and StarType2 are ruled out (i.e., they are eliminated as possibilities).
	- This exclusion approach is applied instead of confirming or indicating which star types are valid or related.

2. Explain the star classifications and spectral tests in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rules should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify a star type based on spectral data outcomes. Each round, you'll be presented with a list of possible star classifications and available spectral analyses. You need to systematically rule out star classifications that do not match the observed outcomes until only one plausible classification remains. Your objective is to identify the star type accurately in the fewest steps.

How to Play:

(1) View the list of possible star classifications and available spectral analyses.

(2) Choose one spectral line analysis from the list to perform.

(3) Use the outcomes to eliminate star classifications that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the star type.

This is the initial state of the game:

Star Classifications: {self.env.truth_space}

Spectral Analyses: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is an astronomical analysis guidebook to introduce the star classifications and spectral analyses:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt