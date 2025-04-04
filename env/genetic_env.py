import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.genetic_data import Truths, Actions, Outcomes

@registry.register_environment("GeneticEnv")
class GeneticEnv(BaseEnv):
    
    def __init__(self, datapoint=None):
        self.all_truths = Truths      # Genetic mutations
        self.all_actions = Actions    # DNA sequencing / gene expression assays
        self.ta_mapping = Outcomes
    
        self.env = None
        
        if datapoint is not None:
            self.reset(datapoint)

    
    def get_knowledge_book_prompt(self, truths, actions, ta_mapping):
        
        knowledge_book_prompt = \
        f"""
Please write a genetic analysis guidebook that introduces the following genetic mutations and assays in natural language according to the following information.

Genetic mutations: {truths}

Assays: {actions}

Results: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Results” represent the genetic mutations that must be **excluded or ruled out** when the corresponding state is observed.

For example,

    If the state of "Assay1" is:
    
    "Assay1":
    {
        "states": {
            "Outcome_1": ["Mutation1", "Mutation2"],
            "Outcome_2": ["Mutation3", "Mutation4"]
        }
    }
        
    This means:
    - When “Assay1” is performed and “Outcome_1” is observed, “Mutation1” and Mutation2 are ruled out (i.e., they are eliminated as possibilities).
    - This exclusion approach is applied instead of confirming or indicating which mutations are valid or related.

2. Explain the genetic mutations and tests in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rule should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify a genetic mutation responsible for a trait based on assay results. Each round, you'll be presented with a list of possible genetic mutations and available assays. You need to systematically rule out genetic mutations that do not match the observed results until only one plausible mutation remains. Your objective is to identify the mutation accurately in the fewest steps.

How to Play:

(1) View the list of possible genetic mutations and available assays.

(2) Choose one assay from the list to perform.

(3) Use the results to eliminate genetic mutations that don't match the observed outcome.

(4) Repeat steps 2 and 3 until you can confidently identify the mutation.

This is the initial state of the game:

Genetic Mutations: {self.env.truth_space}

Assays: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is a genetic analysis guidebook to introduce the genetic mutations and assays:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt