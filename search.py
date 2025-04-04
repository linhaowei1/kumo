"""
The main script for calling search engines to produce golden trajectories for tasks from different domains.
See `./common/config.py` for detailed arguments definitions.
"""
import json
import os

from transformers import HfArgumentParser

from common.configs import Data_Arguments, Eval_Arguments
from common.utils import get_testcase

from env.engine import OracleSearchEngine, VanillaSearchEngine


if __name__ == '__main__':
    
    eval_args, data_args = HfArgumentParser((Eval_Arguments, Data_Arguments)).parse_args_into_dataclasses()
    testcase_generator = get_testcase(None, eval_args, data_args)
    
    result_file = os.path.join(
        eval_args.result_dir,
        'search',
        data_args.domain,
        f'truth_num={data_args.truth_num}+action_num={data_args.action_num}+valid_truth_num={data_args.valid_truth_num}',
        f'eval_times={eval_args.eval_times}.jsonl',
    )

    seed_list = [] # Used for resume evalution
    if os.path.exists(result_file):
        if eval_args.resume:
            with open(result_file, "r") as f:
                lines = f.readlines()
                data = [json.loads(line) for line in lines]
                seed_list = [int(d['seed']) for d in data]
                print("skip seeds: ", seed_list)
        else:
            os.remove(result_file)
    
    if not os.path.exists(os.path.dirname(result_file)):
        os.makedirs(os.path.dirname(result_file))
    
    for env, _ in testcase_generator:
        
        if env.env.seed in seed_list:
            continue
        
        truth_space = env.env.truth_space
        action_space = env.env.action_space
        ta_mapping = env.env.ta_mapping
        
        trajs = {
            'trajectories': [],
            'seed': env.env.seed,
        }
        
            
        traj = {
            'actions': [],
            'generated_text': [],
            'observations': [],
        }
        

        search_engine = OracleSearchEngine(truth_space, action_space, ta_mapping)
        
        last_obs = None
        last_action = None
        
        while True:
            
            last_action = search_engine.search_step(last_action, last_obs)    
            
            traj['actions'].append(last_action)
            traj['observations'].append(last_obs)
            traj['generated_text'].append(f'<ANSWER> {last_action} </ANSWER>')
            
            if last_action in env.env.truth_space:
                traj['actions'].append({'predicted_truth': last_action})
                successful_flag = bool(env.env.evaluate_answer(last_action))
                traj['action_num'] = len(traj['actions'])
                traj['successful'] = successful_flag
                break
            elif last_action in env.env.action_space:
                last_obs = env.env.get_observation(last_action)
            else:
                raise ValueError(f'Invalid action: {last_action}')
        
            
        print(f"Current correct: {successful_flag} | Current action number: {len(traj['actions'])}")
        
        trajs['trajectories'].append(traj)
        
        with open(result_file, 'a') as f:
            f.write(json.dumps(trajs) + '\n')