import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.herb_data import Truths, Actions, Outcomes

@registry.register_environment("HerbEnv")
class HerbEnv(BaseEnv):
    
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
Please write a healing elixir creation guidebook that introduces the following mystical plants and experiments in natural language according to the following information.

Mystical Plants: {truths}

Herb Testing and Brewing Experiments: {actions}

Medicinal Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Outcomes” represent the mystical plants that must be **excluded or ruled out** when the corresponding state is observed.

For example,

    If the state of "Experiment1" is:
    
    "Experiment1":
    {
        "states": {
            "Outcome_1": ["Plant1", "Plant2"],
            "Outcome_2": ["Plant3", "Plant4"]
        }
    }
        
    This means:
    - When “Experiment1” is performed and “Outcome_1” is observed, “Plant1” and Plant2 are ruled out (i.e., they are eliminated as possibilities).
    - This exclusion approach is applied instead of confirming or indicating which plants are valid or related.

2. Explain the mystical plants and tests in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rule should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify the mystical plant needed to create a healing elixir based on test outcomes. Each round, you'll be presented with a list of possible plants and available herbal testing or brewing experiments. You need to systematically rule out mystical plants that do not match the observed outcomes until only one plausible plant remains. Your objective is to identify the plant accurately in the fewest steps.

How to Play:

(1) View the list of possible mystical plants and available experiments.

(2) Choose one experiment from the list to perform.

(3) Use the outcomes to eliminate mystical plants that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the plant.

This is the initial state of the game:

Mystical Plants: {self.env.truth_space}

Herb Testing and Brewing Experiments: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is a healing elixir creation guidebook to introduce the mystical plants and experiments:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt