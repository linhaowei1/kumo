import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.machine_learning_data import Truths, Actions, Outcomes

@registry.register_environment("MLEnv")
class MLEnv(BaseEnv):
    
    def __init__(self, datapoint=None):
        self.all_truths = Truths      # ML models
        self.all_actions = Actions    # Performance metrics evaluation / cross-validation testing
        self.ta_mapping = Outcomes
    
        self.env = None
        
        if datapoint is not None:
            self.reset(datapoint)

    
    def get_knowledge_book_prompt(self, truths, actions, ta_mapping):
        
        knowledge_book_prompt = \
        f"""
Please write a machine learning model analysis guidebook that introduces the following ML models and evaluation techniques in natural language according to the following information.

ML Models: {truths}

Evaluation Techniques: {actions}

Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Outcomes” represent the ML models that must be **excluded or ruled out** when the corresponding state is observed.

For example,

    If the outcome of "Evaluation1" is:
    
    "Evaluation1":
    {
        "states": {
            "Outcome_1": ["Model1", "Model2"],
            "Outcome_2": ["Model3", "Model4"]
        }
    }
        
    This means:
    - When “Evaluation1” is performed and “Outcome_1” is observed, “Model1” and “Model2” are ruled out (i.e., they are eliminated as possibilities).
	- This exclusion approach is applied instead of confirming or indicating which models are valid or related.

2. Explain the ML models and testing methods in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rule should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify an ML model that best fits a dataset based on evaluation outcomes. Each round, you'll be presented with a list of possible ML models and available evaluation techniques. You need to systematically rule out models that do not match the observed outcomes until only one plausible model remains. Your objective is to identify the model accurately in the fewest steps.

How to Play:

(1) View the list of possible ML models and available evaluation techniques.

(2) Choose one evaluation technique from the list to perform.

(3) Use the outcomes to eliminate models that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the model.

This is the initial state of the game:

ML Models: {self.env.truth_space}

Evaluation Techniques: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is a machine learning model analysis guidebook to introduce the models and evaluation techniques:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt