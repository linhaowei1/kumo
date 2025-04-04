from common.registry import registry
from .medical_env import MedicalEnv

@registry.register_environment("MedicalINDEnv")
class MedicalINDEnv(MedicalEnv):
    
    def __init__(self, datapoint=None):
        from .data.medical_ind_data import Diseases, Diagnosis, Outcomes
        self.all_truths = Diseases      
        self.all_actions = Diagnosis    
        self.ta_mapping = Outcomes
    
        self.env = None
        
        if datapoint is not None:
            self.reset(datapoint)

@registry.register_environment("MedicalOODEnv")
class MedicalOODEnv(MedicalEnv):
    
    def __init__(self, datapoint=None):
        from .data.medical_ood_data import Diseases, Diagnosis, Outcomes
        self.all_truths = Diseases      
        self.all_actions = Diagnosis    
        self.ta_mapping = Outcomes
    
        self.env = None
        
        if datapoint is not None:
            self.reset(datapoint)
