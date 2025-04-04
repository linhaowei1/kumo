import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.demographic_data import Truths, Actions, Outcomes

@registry.register_environment("DemographicEnv")
class DemographicEnv(BaseEnv):
    
    def __init__(self, datapoint=None):
        self.all_truths = Truths      # Demographic segments
        self.all_actions = Actions    # Survey data analysis / consumer behavior modeling / trend extrapolation
        self.ta_mapping = Outcomes
    
        self.env = None
        
        if datapoint is not None:
            self.reset(datapoint)

    
    def get_knowledge_book_prompt(self, truths, actions, ta_mapping):
        
        knowledge_book_prompt = \
        f"""
Please write a demographic analysis guidebook that introduces the following demographic segments and techniques in natural language according to the following information.

Demographic Segments: {truths}

Analysis Techniques: {actions}

Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Outcomes” represent the demographic segments that must be **excluded or ruled out** when the corresponding state is observed.

For example,

    If the state of "Technique1" is:
    
    "Technique1":
    {
        "states": {
            "Outcome_1": ["Segment1", "Segment2"],
            "Outcome_2": ["Segment3", "Segment4"]
        }
    }
        
    This means:
    - When “Technique1” is applied and “Outcome_1” is observed, “Segment1” and Segment2 are ruled out (i.e., they are eliminated as possibilities).
    - This exclusion approach is applied instead of confirming or indicating which segments are valid or related.

2. Explain the demographic segments and techniques in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rule should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify a target demographic based on analysis outcomes. Each round, you'll be presented with a list of possible demographic segments and available analysis techniques. You need to systematically rule out demographic segments that do not match the observed outcomes until only one plausible segment remains. Your objective is to identify the segment accurately in the fewest steps.

How to Play:

(1) View the list of possible demographic segments and available analysis techniques.

(2) Choose one technique from the list to perform.

(3) Use the outcomes to eliminate demographic segments that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the segment.

This is the initial state of the game:

Demographic Segments: {self.env.truth_space}

Analysis Techniques: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is a demographic analysis guidebook to introduce the demographic segments and techniques:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt