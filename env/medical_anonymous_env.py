from common.registry import registry
from .medical_env import MedicalEnv
from .engine import Environment

@registry.register_environment("MedicalAnonymousEnv")
class MedicalAnonymousEnv(MedicalEnv):
    
    def __init__(self, datapoint=None):
        super().__init__(datapoint)
    
    def reset(
        self, datapoint,
    ):
        hash_truths = [f'AnonymousDisease{i}' for i in range(len(self.all_truths))]
        hash_actions = [f'AnonymousDiagnosis{i}' for i in range(len(self.all_actions))]
        
        hash_map = {
            truth: hash_truth for truth, hash_truth in zip(self.all_truths, hash_truths)
        }
        hash_map.update({
            action: hash_action for action, hash_action in zip(self.all_actions, hash_actions)
        })
        
        hash_action_map = {}
        
        hash_ta_mapping = {}
        for key, value in self.ta_mapping.items():
            if value['type'] == 'str':
                outcomes = list(value['states'].keys())
                hash_ta_mapping[hash_map[key]] = {
                    'type': value['type'],
                    'states': {
                        f'Outcome{i}': [hash_map[truth] for truth in truths] for i, (state, truths) in enumerate(value['states'].items())
                    }
                }
                hash_action_map[key] = {
                    outcomes[i]: f'Outcome{i}' for i in range(len(value['states']))
                }
                
            elif value['type'] == 'float':
                hash_ta_mapping[hash_map[key]] = {
                    'type': value['type'],
                    'states': {
                        state: [hash_map[truth] for truth in truths] for i, (state, truths) in enumerate(value['states'].items())
                    }
                }
            
        hash_observations = {}
        for key, value in datapoint['observations'].items():
            if isinstance(value, str):
                hash_observations[hash_map[key]] = hash_action_map[key][value]
            else:
                hash_observations[hash_map[key]] = value
        
        self.hash_ta_mapping = hash_ta_mapping
        self.hash_actions = hash_actions
        self.hash_truths = hash_truths
        
        self.env = Environment(
            [hash_map[truth] for truth in datapoint['truths']], 
            [hash_map[action] for action in datapoint['actions']], 
            hash_ta_mapping, 
            hash_observations, 
            datapoint['seed']
        )
        
        
    def get_system_prompt(self, book=None, agent_type='VanillaAgent'):
        
        assert agent_type == 'SFTAgent'

        system_prompt = \
            f"""
This game challenges you to identify a disease based on diagnostic results. Each round, you'll see possible diseases and available diagnostic tests. You need to rule out diseases that don't fit the observed outcomes until only one plausible disease remains. Your objective is to accurately identify the only one disease in the fewest actions.

How to Play:

(1) View the list of possible diseases and available diagnostic tests.

(2) Select one diagnostic test per round to see its outcome.

(3) Use the outcomes to eliminate diseases that don't match the observed results.

(4) Repeat steps 2 and 3 until you can confidently identify the disease.

This is the initial state of the game:

Disease: {self.env.truth_space}

Diagnostic Tests: {self.env.action_space}
                
"""
            
        system_prompt += f"\n\nThe rule-out relationship:\n\n{self.get_reduced_ta_mapping(self.hash_ta_mapping)}"
        return system_prompt

        
    def get_reduced_ta_mapping(self, ta_mapping=None):
        if ta_mapping is None:
            ta_mapping = self.ta_mapping
        seen_observations = {action: ta_mapping[action]['states'] for action in self.env.action_space}
        
        for k, v in seen_observations.items():
            new_v = {
                state: {value for value in v[state] if value in self.env.truth_space}
                for state in v
            }
            seen_observations[k] = new_v
        return seen_observations