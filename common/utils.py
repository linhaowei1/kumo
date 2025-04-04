import os
import json

from llm import load_llm
from agents import load_agent
from env import load_env

def load_dataset(data_args):
    """ Obtain a generator returning (datapoint, knowledge_book) pairs """
    with open(data_args.dataset_path) as f:
        dataset = [json.loads(line) for line in f][:data_args.data_num]
    for i, datapoint in enumerate(dataset):
        knowledge_book_path = os.path.join(data_args.knowledge_book_dir, f"seed={i}.txt")
        if not os.path.exists(knowledge_book_path):
            yield datapoint, None
        else:
            with open(knowledge_book_path, "r", encoding="utf-8") as f:
                knowledge_book = f.read()
            yield datapoint, knowledge_book
            
                
def get_llm(llm_config):
    """ Obtain a LLM instance """
    return load_llm(llm_config.load_type, llm_config)

def get_env(domain):
    """ Obtain a domain specialized env """
    return load_env(domain, None)

def get_testcase(llm_model=None, eval_args=None, data_args=None):
    """ Obtain a generator returning (env, agent) pairs """
    env = load_env(data_args.domain, None)
    test_generator = load_dataset(data_args)
    agent = None
    for datapoint, book in test_generator:
        env.reset(datapoint)
        if llm_model is None:
            yield env, None
        else:
            if agent is not None:
                agent.reset(datapoint['truths'], datapoint['actions'], book, env.get_system_prompt(book, eval_args.agent_type))
            else:
                agent = load_agent(eval_args.agent_type, datapoint['truths'], datapoint['actions'], book, llm_model, env.get_system_prompt(book, eval_args.agent_type))
            yield env, agent
            