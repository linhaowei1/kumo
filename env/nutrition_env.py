import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.nutrition_data import Truths, Actions, Outcomes

@registry.register_environment("NutritionEnv")
class NutritionEnv(BaseEnv):
    
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
Please write a nutritional analysis guidebook that introduces the following dietary regimens and health evaluations in natural language according to the following information.

Dietary regimens: {truths}

Health evaluations: {actions}

Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Outcomes” represent the dietary regimens that must be **excluded or ruled out** when the corresponding state is observed.

For example,

    If the state of "Evaluation1" is:
    
    "Evaluation1":
    {
        "states": {
            "Outcome_1": ["Regimen1", "Regimen2"],
            "Outcome_2": ["Regimen3", "Regimen4"]
        }
    }
        
    This means:
    - When “Evaluation1” is performed and “Outcome_1” is observed, “Regimen1” and "Regimen2" are ruled out (i.e., they are eliminated as possibilities).
    - This exclusion approach is applied instead of confirming or indicating which regimens are valid or related.

2. Explain the dietary regimens and evaluations in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rule should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify which dietary regimen improves a patient's condition based on health evaluations. Each round, you'll be presented with a list of possible dietary regimens and available health evaluations. You need to systematically rule out dietary regimens that do not match the observed outcomes until only one plausible regimen remains. Your objective is to identify the regimen accurately in the fewest steps.

How to Play:

(1) View the list of possible dietary regimens and available health evaluations.

(2) Choose one evaluation from the list to perform.

(3) Use the outcomes to eliminate dietary regimens that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the regimen.

This is the initial state of the game:

Dietary Regimens: {self.env.truth_space}

Health Evaluations: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is a nutritional analysis guidebook to introduce the dietary regimens and evaluations:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt