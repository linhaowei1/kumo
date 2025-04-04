import json
import os

from transformers import HfArgumentParser
from tqdm import tqdm

from common.configs import Data_Arguments, LLM_Arguments
from common.utils import get_env, get_llm


    
if __name__ == "__main__":

    llm_args, data_args = HfArgumentParser((LLM_Arguments, Data_Arguments)).parse_args_into_dataclasses()
    
    dataset_path = data_args.dataset_path
    data_num = data_args.data_num
    kb_dir = data_args.knowledge_book_dir
    
    # Load env
    env = get_env(data_args.domain)
    
    # Load datapoints
    with open(dataset_path) as f:
        dataset = [json.loads(line) for line in f]
        dataset = dataset[:data_num]
    if len(dataset) < data_num:
        print(f"Dataset size is smaller than {data_num}. Plz generate more datapoints.")
        exit()
        
    # Get LLM
    llm = get_llm(llm_args)
    
    # generate knowledge book for each datapoint in the dataset
    for i, d in tqdm(enumerate(dataset), total=len(dataset)):
        path = os.path.join(kb_dir, f"seed={d['seed']}.txt")
        dir_of_path = os.path.dirname(path)
        
        if not os.path.exists(dir_of_path):
            os.makedirs(dir_of_path)
            
        if os.path.exists(path):
            continue
        
        seen_observations = {action: env.ta_mapping[action]['states'] for action in d['actions']}
        
        for k, v in seen_observations.items():
            new_v = {
                state: {value for value in v[state] if value in d['truths']}
                for state in v
            }
            seen_observations[k] = new_v
        
        messages = [
            {"role":"user", "content":env.get_knowledge_book_prompt(d['truths'], d['actions'], seen_observations)}
        ]
        book = llm.call_llm(messages)
        with open(path, "w") as f:
            f.write(book)