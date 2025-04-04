from dataclasses import dataclass, field
from typing import List, Optional, Literal
from transformers import HfArgumentParser


@dataclass
class LLM_Arguments:
    load_type: Literal["OPENAI", "ANTHROPIC"] = field(
        default='OPENAI',
        metadata={
            "help": "Type of LLM loading method (OPENAI or ANTHROPIC)",
            "choices": ["OPENAI", "ANTHROPIC"]
        }
    )
    model_name_or_path: str = field(
        default='EMPTY',
        metadata={"help": "Path or name of the model"}
    )
    
    # openai parameters
    api_base: str = field(
        default='http://localhost:8001/v1',
        metadata={"help": "Base URL for API"}
    )
    api_key: str = field(
        default='EMPTY',
        metadata={"help": "API key for authentication"}
    )

@dataclass
class Data_Arguments:
    truth_num: int = field(
        default=4,
        metadata={"help": "Number of truth items"}
    )
    action_num: int = field(
        default=6,
        metadata={"help": "Number of action items"}
    )
    valid_truth_num: int = field(
        default=1,
        metadata={"help": "Number of valid truth items"}
    )
    data_num: int = field(
        default=50,
        metadata={"help": "Total number of data items"}
    )
    domain: str = field(
        default='MedicalEnv',
        metadata={"help": "Domain of the environment"}
    )
    dataset_path: Optional[str] = field(
        default=None,
        metadata={"help": "Path to the dataset file"}
    )
    knowledge_book_dir: Optional[str] = field(
        default=None,
        metadata={"help": "Directory for knowledge book"}
    )

    
    def __post_init__(self):
        if self.dataset_path is None:
            self.dataset_path = (
                f'env/{self.domain}/'
                f'truth_num={self.truth_num}+'
                f'action_num={self.action_num}+'
                f'valid_truth_num={self.valid_truth_num}.jsonl'
            )
        
        if self.knowledge_book_dir is None:
            self.knowledge_book_dir = (
                f'env/{self.domain}/knowledge_book/'
                f'truth_num={self.truth_num}+'
                f'action_num={self.action_num}+'
                f'valid_truth_num={self.valid_truth_num}'
            )


@dataclass
class Eval_Arguments:
    agent_type: str = field(
        default='VanillaAgent',
        metadata={"help": "Type of agent to evaluate"}
    )
    eval_times: int = field(
        default=5,
        metadata={"help": "Number of evaluation iterations"}
    )
    max_steps: int = field(
        default=50,
        metadata={"help": "Maximum steps per evaluation"}
    )
    result_dir: str = field(
        default='./results',
        metadata={"help": "Directory to store results"}
    )
    resume: bool = field(
        default=False,
        metadata={
            "help": "Whether to resume from previous run"
        }
    )


@dataclass
class Config_Generate_Arguments:
    data_path: str = field(
        default="./templates/config_generation.jsonl",
        metadata={
            "help": ""
        }
    )
    template_path: str = field(
        default="./template/config_generation_template.md",
        metadata={
            "help": "Path to the markdown template for calling LLM to generate config"
        }
    )
    example_path: str = field(
        default="./templates/example.py.txt",
        metadata={
            "help":""
        }
    )


@dataclass
class Knowledge_Book_Revision_Arguments:
    revision_template_path: str = field(
        default="./templates/revision_template.md",
        metadata={
            "help":""
        }
    )
