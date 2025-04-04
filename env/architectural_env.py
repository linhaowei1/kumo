import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.architectural_data import Truths, Actions, Outcomes

@registry.register_environment("ArchitecturalEnv")
class ArchitecturalEnv(BaseEnv):
    
    def __init__(self, datapoint=None):
        self.all_truths = Truths      # Architectural styles
        self.all_actions = Actions    # Structural pattern comparison / historical design references
        self.ta_mapping = Outcomes
    
        self.env = None

        if datapoint is not None:
            self.reset(datapoint)

    
    def get_knowledge_book_prompt(self, truths, actions, ta_mapping):
        
        knowledge_book_prompt = \
        f"""
Please write a guidebook for architectural analysis that introduces the following architectural styles and comparisons based on structural patterns and historical design references in natural language according to the following information.

Architectural styles: {truths}

Structural pattern comparisons / Historical design references: {actions}

Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Outcomes” represent the architectural styles that must be **excluded or ruled out** when the corresponding state is observed.

For example,

    If the state of "Comparison1" is:
    
    "Comparison1":
    {
        "states": {
            "Outcome_1": ["Style1", "Style2"],
            "Outcome_2": ["Style3", "Style4"]
        }
    }
        
    This means:
    - When “Comparison1” is performed and “Outcome_1” is observed, “Style1” and “Style2” are ruled out (i.e., they are eliminated as possibilities).
    - This exclusion approach is applied instead of confirming or indicating which styles are valid or related.

2. Explain the architectural styles and comparisons in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rule should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify an architectural style based on structural pattern comparisons and historical design references. Each round, you'll be presented with a list of possible architectural styles and available comparisons. You need to systematically rule out styles that do not match the observed outcomes until only one plausible style remains. Your objective is to identify the style accurately in the fewest steps.

How to Play:

(1) View the list of possible architectural styles and available comparisons.

(2) Choose one comparison from the list to perform.

(3) Use the outcomes to eliminate architectural styles that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the style.

This is the initial state of the game:

Architectural Styles: {self.env.truth_space}

Comparisons: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is a guidebook for architectural styles and comparisons:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt