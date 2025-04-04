import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.economic_data import Truths, Actions, Outcomes

@registry.register_environment("EconomicEnv")
class EconomicEnv(BaseEnv):
    
    def __init__(self, datapoint=None):
        self.all_truths = Truths      # Economic models
        self.all_actions = Actions    # Policy effect simulation / model comparison
        self.ta_mapping = Outcomes
    
        self.env = None
        
        if datapoint is not None:
            self.reset(datapoint)

    
    def get_knowledge_book_prompt(self, truths, actions, ta_mapping):
        
        knowledge_book_prompt = \
        f"""
Please create an economic analysis guidebook that introduces the following economic models and policy simulations in natural language according to the following information.

Economic models: {truths}

Policy simulations: {actions}

Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Outcomes” represent the economic models that must be **excluded or ruled out** when the corresponding state is observed.

For example,

    If the state of "PolicySimulation1" is:
    
    "PolicySimulation1":
    {
        "states": {
            "Outcome_1": ["Model1", "Model2"],
            "Outcome_2": ["Model3", "Model4"]
        }
    }
        
    This means:
    - When "PolicySimulation1" is conducted and "Outcome_1" is observed, "Model1" and "Model2" are ruled out (i.e., they are eliminated as possibilities).
	- This exclusion approach is applied instead of confirming or indicating which models are valid or related.

2. Explain the economic models and simulations in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rule should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify an economic model based on policy simulation outcomes. Each round, you'll be presented with a list of possible economic models and available policy simulations. You need to systematically rule out economic models that do not match the observed outcomes until only one plausible model remains. Your objective is to identify the model accurately in the fewest steps.

How to Play:

(1) View the list of possible economic models and available policy simulations.

(2) Choose one policy simulation from the list to perform.

(3) Use the outcomes to eliminate economic models that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the model.

This is the initial state of the game:

Economic Models: {self.env.truth_space}

Policy Simulations: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is an economic analysis guidebook to introduce the economic models and policy simulations:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt