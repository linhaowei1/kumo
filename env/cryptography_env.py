import os
import json
from common.registry import registry
from .base_env import BaseEnv
from env.data.cryptography_data import Truths, Actions, Outcomes

@registry.register_environment("CryptographyEnv")
class CryptographyEnv(BaseEnv):
    
    def __init__(self, datapoint=None):
        self.all_truths = Truths       # Cryptographic ciphers
        self.all_actions = Actions   # Frequency analysis / key pattern testing
        self.ta_mapping = Outcomes       # Outcomes of techniques applied

        self.env = None
        
        if datapoint is not None:
            self.reset(datapoint)

    def get_knowledge_book_prompt(self, ciphers, techniques, ta_mapping):
        
        knowledge_guide_prompt = \
        f"""
Please write a cryptographic analysis guidebook that introduces the following cryptographic ciphers and techniques in a way that is understandable. The guidebook should adhere to the information outlined below.

Cryptographic Ciphers: {ciphers}

Techniques: {techniques}

Outcomes: {ta_mapping}

""" + """
Guidelines:

1. The sets defined under the state of “Outcomes” represent the cryptographic ciphers that must be **excluded or ruled out** when a given outcome is obtained.

For example,

    If the result of "Technique1" is:
    
    "Technique1":
    {
        "outcomes": {
            "Result_1": ["Cipher1", "Cipher2"],
            "Result_2": ["Cipher3", "Cipher4"]
        }
    }
        
    This implies:
    - When “Technique1” is applied and “Result_1” is observed, “Cipher1” and “Cipher2” are ruled out (i.e., they can no longer be considered as possibilities).
    - This approach excludes ciphers rather than confirming related or valid ones.

2. Clearly explain the ciphers and techniques to make the relationships comprehensible to the reader.

3. Present all relevant rule-out information to prevent any misunderstanding. Each rule should be articulated clearly and in context.

"""
        
        return knowledge_guide_prompt
    
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        if agent_type == 'VanillaAgent' or agent_type == 'SFTAgent':
            system_prompt = \
                f"""
This challenge tasks you with identifying the cryptographic cipher used to encode a message based on the outcomes of applied techniques. Each round, you'll see a list of possible ciphers and available analysis techniques. Your goal is to systematically exclude ciphers that don't align with observed results until only one plausible cipher is left, using the fewest moves possible.

How to Play:

(1) Review the list of potential cryptographic ciphers and available analysis techniques.

(2) Select one technique from the list to apply.

(3) Use the technique's outcomes to exclude ciphers that don't match the results.

(4) Repeat steps 2 and 3 until you can confidently pinpoint the cipher.

Initial State of the Game:

Cryptographic Ciphers: {self.env.truth_space}

Techniques: {self.env.action_space}
                
"""
            
            if book is not None and agent_type != 'SFTAgent':
                system_prompt += f"\n\nHere is a cryptographic analysis guidebook detailing the ciphers and techniques:\n\n{book}"
            elif agent_type == 'SFTAgent':
                system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping()}"
            return system_prompt