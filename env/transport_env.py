import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.transport_data import Truths, Actions, Outcomes

@registry.register_environment("TransportEnv")
class TransportEnv(BaseEnv):
    
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
Please write a transportation analysis guidebook that explores various transportation methods of civilizations in natural language according to the following information.

Transport methods (historical/futuristic): {truths}

Artifact examination / route pattern mapping: {actions}

Outcomes: {ta_mapping}

""" + """
Requirements:

1. The sets defined under the state of “Outcomes” represent the transport methods that must be **excluded or ruled out** when the corresponding state is observed.

For example,

    If the state of "Artifact Examination" is:
    
    "Artifact Examination":
    {
        "states": {
            "Outcome_1": ["TransportMethod1", "TransportMethod2"],
            "Outcome_2": ["TransportMethod3", "TransportMethod4"]
        }
    }
        
    This means:
    - When “Artifact Examination” is performed and “Outcome_1” is observed, “TransportMethod1” and TransportMethod2 are ruled out (i.e., they are eliminated as possibilities).
	- This exclusion approach is applied instead of confirming or indicating which transport methods are valid or related.

2. Explain the transport methods and analyses in a clear, straightforward manner to ensure the context and relationships are easy to understand.

3. Ensure that all relevant information is fully communicated without omissions. Every "rule-out" rules should be presented clearly and cohesively.

"""
        
        return knowledge_book_prompt
        
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This game challenges you to identify a transportation method used by a civilization based on artifact examinations and route pattern mappings. Each round, you'll be presented with a list of possible transport methods and available analyses. You need to systematically rule out transport methods that do not match the observed outcomes until only one plausible method remains. Your objective is to identify the method accurately in the fewest steps.

How to Play:

(1) View the list of possible transport methods and available analyses.

(2) Choose one analysis from the list to perform.

(3) Use the outcomes to eliminate transport methods that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the transport method.

This is the initial state of the game:

Transport Methods: {self.env.truth_space}

Artifact Examinations / Route Pattern Mappings: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is a transport analysis guidebook to introduce the transport methods and analyses:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt