"""
Script for sampling specific tasks from generated seed config using SAT solver.
See `./common/config.py` for detailed arguments definitions.
"""

import json
import os
import random
from collections import defaultdict
from typing import Optional

from pysat.card import CardEnc
from pysat.solvers import Solver
from tqdm import tqdm
from transformers import HfArgumentParser

from common.configs import Data_Arguments
from common.utils import get_env


def generate_subset(all_truths, all_actions, ta_mapping, num_truths=4, num_valid_truths=1, num_actions=None, sample_mode="truth"):
    """
    Generate a data item consisting of a subset of truths, actions, and observations.
    """
    # sample a subset of truths
    truths = random.sample(all_truths, num_truths)
    if sample_mode == "truth":
        # generate a subset of actions & observations based on valid truths
        valid_truths = random.sample(truths, num_valid_truths)
        complete, actions, observations = _sample_observations_actions_subset(truths, ta_mapping, valid_truths, num_actions)
    elif sample_mode == "action":
        raise NotImplementedError()
    else:
        raise ValueError(f"Invalid sampling mode: {sample_mode}")

    # To default format
    if num_valid_truths == 1:
        valid_truths = valid_truths[0]

    return complete, truths, actions, observations, valid_truths

def _sample_observations_actions_subset(subset_truths, ta_mapping, valid_truths, num_actions):
    if isinstance(valid_truths, str):
        valid_truths = [valid_truths]
    invalid_truths = [truth for truth in subset_truths if truth not in valid_truths]
    subset_actions = set()
    valid_truth_related_actions = set()
    valid_state_dicts = defaultdict(dict)

    # Extract necessary infomation for further SAT solver
    for action, action_info in ta_mapping.items():
        action_relevant = False
        action_contradict = False
        for state, impossible_diseases in action_info["states"].items():
            state_relevant = False
            state_contradict = False
            for truth in subset_truths:
                if truth in impossible_diseases:
                    state_relevant  =True
                    if truth in valid_truths:
                        state_contradict = True
            if state_relevant:
                action_relevant = True
                if state_contradict:
                    action_contradict = True
                else:
                    state_dict = {t:t in impossible_diseases for t in invalid_truths}
                    valid_state_dicts[action].update({state:state_dict})
        if action_relevant:
            subset_actions.add(action)
        if action_contradict:
            valid_truth_related_actions.add(action)

    # Call SAT solver
    complete, observations = _sat_solve(invalid_truths, valid_state_dicts, num_actions)
    
    # Sample extra actions
    if complete:
        num_extra_actions = num_actions - len(observations)
        unused_actions = [action for action in subset_actions if action not in observations]
        
        # Sample extra actions from unused related actions
        for action in random.sample(unused_actions, min(len(unused_actions), num_extra_actions)):
            if action in valid_truth_related_actions:
                allowed_states = []
                for state in ta_mapping[action]['states']:
                    if all(valid_truth not in ta_mapping[action]["states"][state] for valid_truth in valid_truths):
                        allowed_states.append(state)
                observations[action] = random.choice(allowed_states)
            else:
                observations[action] = random.choice(list(ta_mapping[action]['states'].keys()))
        
        # If still not enough, sample actions from irrelevant actions
        if num_extra_actions > len(unused_actions):
            irrelevant_actions = [action for action in ta_mapping if action not in subset_actions]
            for action in random.sample(irrelevant_actions, num_extra_actions - len(unused_actions)):
                observations[action] = random.choice(list(ta_mapping[action]['states'].keys()))
        
        # Sample number for float type observations
        for action in observations:
            if ta_mapping[action]["type"] == "float":
                try:
                    observations[action] = random.uniform(observations[action][0], observations[action][1])
                except:
                    import pdb; pdb.set_trace()
        
        subset_actions = list(observations)
    
    return complete, subset_actions, observations

def _sat_solve(invalid_truths, valid_state_dicts:dict, max_actions:Optional[int]=None):
    
    # Unpack valid_state_dicts to lists
    Actions = []
    States = []
    Vectors = []
    for action, s in valid_state_dicts.items():
        Actions.append(action)
        States.append([])
        Vectors.append([])
        for state, d in s.items():
            States[-1].append(state)
            vector = []
            for invalid_truth in invalid_truths:
                vector.append(d[invalid_truth])
            Vectors[-1].append(vector)
    
    num_actions = len(Actions)
    max_actions = min(max_actions, num_actions) if max_actions is not None else num_actions
    num_invalid_truths = len(invalid_truths)
    
    # Define solver
    solver = Solver()
    
    # Define variables
    var_map = {}
    var_id = 1
    for i in range(num_actions):
        for j in range(len(Vectors[i])):
            var_map[(i, j)] = var_id
            var_id += 1

    # Every action choose at most one corresponding state vector
    for i in range(num_actions):
        for j in range(len(Vectors[i])):
            for k in range(j + 1, len(Vectors[i])):
                solver.add_clause([-var_map[(i, j)], -var_map[(i, k)]])
    
    # Restrict the upper bound of the actions used
    for clause in CardEnc.atmost(var_map.values(), bound=max_actions):
        solver.add_clause(clause)
    
    # Every invalid truth is excluded by at least one observation
    for k in range(num_invalid_truths):
        clause = []
        for i in range(num_actions):
            for j in range(len(Vectors[i])):
                if Vectors[i][j][k]:
                    clause.append(var_map[(i, j)])
        solver.add_clause(clause)
    
    # Solve
    complete = solver.solve()
    observations = None
    if complete:
        model = solver.get_model()
        observations = dict()
        for i in range(num_actions):
            for j in range(len(Vectors[i])):
                if model[var_map[(i, j)] - 1] > 0:
                    observations[Actions[i]] = States[i][j]
                    break
    solver.delete()
    
    return complete, observations

def _is_duplicate(dataset, truths, actions, observations, ta_mapping):
    """
    Check if the data item is duplicated.
    """
    if len(dataset) == 0:
        return False
    for item in dataset:
        duplicate = True
        if set(item['truths']) != set(truths):
            continue
        if set(item['actions']) != set(actions):
            continue
        for action, state in item['observations'].items():
            if not action in observations:
                duplicate = False
            elif ta_mapping[action]["type"] == "float":
                assert isinstance(state, float)
                for possible_state in ta_mapping[action]["states"]:
                    if possible_state[0] <= state and possible_state[1] >= state:
                        if possible_state[0] > observations[action] or possible_state[1] < observations[action]:
                            duplicate = False
                        break
            else:
                if state != observations[action]:
                    duplicate = False
            if not duplicate:
                break
        if duplicate:
            return True
    return False


if __name__ == "__main__":
    
    args = HfArgumentParser((Data_Arguments)).parse_args_into_dataclasses()[0]
    env = get_env(args.domain)
    
    TRUTHS = env.all_truths
    ACTIONS = env.all_actions
    TAMAPPING = env.ta_mapping
    
    dataset_path = args.dataset_path
    dataset_dir = os.path.dirname(dataset_path)
    
    if not os.path.exists(dataset_dir):
        os.makedirs(dataset_dir)
        dataset = []
    else:
        if os.path.exists(dataset_path):    
            with open(dataset_path) as f:
                dataset = [json.loads(line) for line in f]
        else:
            dataset = []
    
    for i in tqdm(range(len(dataset),args.data_num)):
        random.seed(i)
        while True:
            complete, truths, actions, observations, valid_truths = generate_subset(
                TRUTHS, 
                ACTIONS, 
                TAMAPPING,
                num_truths=args.truth_num,
                num_valid_truths=args.valid_truth_num,
                num_actions=args.action_num,
                sample_mode="truth"
            )
            if not complete:
                continue
            if _is_duplicate(dataset, truths, actions, observations, TAMAPPING):
                continue

            item = {
                "truths": list(truths),
                "actions": list(actions),
                "observations": observations,
                'seed': i,
                'valid_truth': valid_truths
            }
            dataset.append(item)
            with open(dataset_path, "a") as f:
                f.write(json.dumps(item) + "\n")
            break