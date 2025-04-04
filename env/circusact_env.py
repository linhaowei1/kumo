import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.circus_data import Truths, Actions, Outcomes

@registry.register_environment("CircusActEnv")
class CircusActEnv(BaseEnv):
    
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
Please write a guidebook for analyzing circus performances that introduces the following acrobatic techniques and analysis methods in natural language according to the following information.

Acrobatic techniques: {truths}

Body position analysis / timing and motion studies: {actions}

Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Outcomes” represent the acrobatic techniques that must be **excluded or ruled out** when the corresponding state is observed.

For example,

    If the state of "BodyPositionAnalysis1" is:
    
    "BodyPositionAnalysis1":
    {
        "states": {
            "Outcome_1": ["Technique1", "Technique2"],
            "Outcome_2": ["Technique3", "Technique4"]
        }
    }
        
    This means:
    - When “BodyPositionAnalysis1” is performed and “Outcome_1” is observed, “Technique1” and Technique2 are ruled out (i.e., they are eliminated as possibilities).
    - This exclusion approach is applied instead of confirming or indicating which techniques are valid or related.

2. Explain the acrobatic techniques and analysis methods in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rule should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify an acrobatic technique used in a circus act based on analysis outcomes. Each round, you'll be presented with a list of possible techniques and available analysis methods. You need to systematically rule out techniques that do not match the observed outcomes until only one plausible technique remains. Your objective is to identify the technique accurately in the fewest steps.

How to Play:

(1) View the list of possible acrobatic techniques and available analysis methods.

(2) Choose one analysis method from the list to perform.

(3) Use the outcomes to eliminate techniques that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the technique.

This is the initial state of the game:

Acrobatic Techniques: {self.env.truth_space}

Body Position Analysis / Timing and Motion Studies: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is a guidebook to introduce the acrobatic techniques and analysis methods:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt