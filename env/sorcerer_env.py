import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.sorcerer_data import Truths, Actions, Outcomes

@registry.register_environment("SorcererEnv")
class SorcererEnv(BaseEnv):
    
    def __init__(self, datapoint=None):
        self.all_truths = Truths      # Different sorcerer bloodlines
        self.all_actions = Actions    # Lineage tracing / Ancestral record examination / Magical heritage analysis
        self.ta_mapping = Outcomes
    
        self.env = None
        
        if datapoint is not None:
            self.reset(datapoint)

    
    def get_knowledge_book_prompt(self, truths, actions, ta_mapping):
        
        knowledge_book_prompt = \
        f"""
Please write an ancestral examination guidebook that introduces the following sorcerer bloodlines and lineage verification methods in natural language according to the following information.

Sorcerer Bloodlines: {truths}

Lineage Verification Methods: {actions}

Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Outcomes” represent the sorcerer bloodlines that must be **excluded or ruled out** when the corresponding state is observed.

For example,

    If the state of "LineageTrace1" is:
    
    "LineageTrace1":
    {
        "states": {
            "Outcome_1": ["Bloodline1", "Bloodline2"],
            "Outcome_2": ["Bloodline3", "Bloodline4"]
        }
    }
        
    This means:
    - When “LineageTrace1” is performed and “Outcome_1” is observed, “Bloodline1” and Bloodline2 are ruled out (i.e., they are eliminated as possibilities).
    - This exclusion approach is applied instead of confirming or indicating which bloodlines are valid or related.

2. Explain the sorcerer bloodlines and verification methods in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rule should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify a sorcerer bloodline based on lineage verification outcomes. Each round, you'll be presented with a list of possible sorcerer bloodlines and available verification methods. You need to systematically rule out bloodlines that do not match the observed outcomes until only one plausible bloodline remains. Your objective is to identify the bloodline accurately in the fewest steps.

How to Play:

(1) View the list of possible sorcerer bloodlines and available verification methods.

(2) Choose one verification method from the list to perform.

(3) Use the outcomes to eliminate sorcerer bloodlines that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the bloodline.

This is the initial state of the game:

Sorcerer Bloodlines: {self.env.truth_space}

Verification Methods: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is an ancestral examination guidebook to introduce the sorcerer bloodlines and verification methods:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt