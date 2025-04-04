from .relic_env import RelicEnv
from .herb_env import HerbEnv
from .transdimensional_env import TransdimensionalEnv
from .sorcerer_env import SorcererEnv
from .quantum_env import QuantumEnv
from .astronomy_env import AstronomyEnv
from .musicgenres_env import MusicGenresEnv
from .cloud_env import CloudEnv
from .cuisine_env import CuisineEnv
from .plant_env import PlantEnv
from .historical_env import HistoricalEnv
from .gadget_env import GadgetEnv
from .timetravel_env import TimeTravelEnv
from .pollution_env import PollutionEnv
from .demographic_env import DemographicEnv
from .craftsman_env import CraftsmanEnv
from .starconstellation_env import StarConstellationEnv
from .mythicalcreature_env import MythicalCreatureEnv
from .artstyle_env import ArtStyleEnv
from .cooking_env import CookingEnv
from .historicalbattle_env import HistoricalBattleEnv
from .fungal_env import FungalEnv
from .cryptography_env import CryptographyEnv
from .storage_env import StorageEnv
from .rover_env import RoverEnv
from .fashion_env import FashionEnv
from .license_env import LicenseEnv
from .testing_env import TestingEnv
from .virusclassification_env import VirusClassificationEnv 
from .narrativedetect_env import NarrativeDetectEnv
from .renewableenergy_env import RenewableEnergyEnv
from .celestial_env import CelestialEnv
from .spice_env import SpiceEnv
from .wildlife_env import WildlifeEnv
from .vehicle_env import VehicleEnv
from .beverage_env import BeverageEnv
from .control_env import ControlEnv
from .currency_env import CurrencyEnv
from .marketing_env import MarketingEnv
from .architectural_env import ArchitecturalEnv
from .botanical_env import BotanicalEnv
from .circusact_env import CircusActEnv
from .audiodialect_env import AudioDialectEnv
from .leadership_env import LeadershipEnv
from .transport_env import TransportEnv
from .ecological_env import EcologicalEnv
from .mythic_env import MythicEnv
from .enzyme_env import EnzymeEnv
from .oskernel_env import OSKernelEnv
from .mineralclassification_env import MineralClassificationEnv
from .economic_env import EconomicEnv
from .detective_env import DetectiveEnv
from .chess_env import ChessEnv
from .mythical_env import MythicalEnv
from .chemicalcompounds_env import ChemicalCompoundsEnv
from .computation_env import ComputationEnv
from .machinepart_env import MachinePartEnv
from .literary_env import LiteraryEnv
from .marine_env import MarineEnv
from .philosophy_env import PhilosophyEnv
from .archaeological_env import ArchaeologicalEnv
from .gemstone_env import GemstoneEnv
from .genetic_env import GeneticEnv
from .microbiology_env import MicrobiologyEnv
from .scifi_env import SciFiEnv
from .hormone_env import HormoneEnv
from .sculptor_env import SculptorEnv
from .neuro_env import NeuroEnv
from .ocean_env import OceanEnv
from .mineral_env import MineralEnv
from .fish_env import FishEnv
from .martialarts_env import MartialArtsEnv
from .rocketfuel_env import RocketFuelEnv
from .ml_env import MLEnv
from .politicalmanifesto_env import PoliticalManifestoEnv
from .coffee_env import CoffeeEnv
from .motifanalysis_env import MotifAnalysisEnv
from .nutrition_env import NutritionEnv
from .malware_env import MalwareEnv
from .geological_env import GeologicalEnv
from .theatrical_env import TheatricalEnv
from .printingtechnique_env import PrintingTechniqueEnv
from .stellar_env import StellarEnv
from .soil_env import SoilEnv
from .software_env import SoftwareEnv
from .caridentification_env import CarIdentificationEnv
from .pharmaceutical_env import PharmaceuticalEnv
from .network_env import NetworkEnv
from .birdnest_env import BirdNestEnv
from .energy_env import EnergyEnv
from .language_env import LanguageEnv
from .algorithm_env import AlgorithmEnv
from .mathematical_env import MathematicalEnv
from .musical_env import MusicalEnv
from .inventor_env import InventorEnv
from common.registry import registry
from .medical_env import MedicalEnv
from .music_env import MusicEnv
from .fantasy_env import FantasyEnv
from .education_env import EducationEnv
from .chemical_env import ChemicalEnv
from .medical_ind_ood_env import MedicalINDEnv, MedicalOODEnv
from .medical_anonymous_env import MedicalAnonymousEnv


__all__ = [
    'RelicEnv',
    'HerbEnv',
    'TransdimensionalEnv',
    'SorcererEnv',
    'QuantumEnv',
    'AstronomyEnv',
    'MusicGenresEnv',
    'CloudEnv',
    'CuisineEnv',
    'PlantEnv',
    'HistoricalEnv',
    'GadgetEnv',
    'TimeTravelEnv',
    'PollutionEnv',
    'DemographicEnv',
    'CraftsmanEnv',
    'StarConstellationEnv',
    'MythicalCreatureEnv',
    'ArtStyleEnv',
    'CookingEnv',
    'HistoricalBattleEnv',
    'FungalEnv',
    'CryptographyEnv',
    'StorageEnv',
    'RoverEnv',
    'FashionEnv',
    'LicenseEnv',
    'VirusClassificationEnv',
    'TestingEnv',
    'NarrativeDetectEnv',
    'RenewableEnergyEnv',
    'CelestialEnv',
    'SpiceEnv',
    'WildlifeEnv',
    'VehicleEnv',
    'BeverageEnv',
    'ControlEnv',
    'CurrencyEnv',
    'MarketingEnv',
    'BotanicalEnv',
    'CircusActEnv',
    'AudioDialectEnv',
    'LeadershipEnv',
    'TransportEnv',
    'EcologicalEnv',
    'MythicEnv',
    'EnzymeEnv',
    'OSKernelEnv',
    'MineralClassificationEnv',
    'EconomicEnv',
    'DetectiveEnv',
    'ChessEnv',
    'MythicalEnv',
    'ChemicalCompoundsEnv',
    'ArchitecturalEnv',
    'ComputationEnv',
    'MachinePartEnv',
    'LiteraryEnv',
    'MarineEnv',
    'PhilosophyEnv',
    'ArchaeologicalEnv',
    'GemstoneEnv',
    'GeneticEnv',
    'MicrobiologyEnv',
    'SciFiEnv',
    'HormoneEnv',
    'SculptorEnv',
    'NeuroEnv',
    'OceanEnv',
    'MineralEnv',
    'FishEnv',
    'MartialArtsEnv',
    'RocketFuelEnv',
    'MLEnv',
    'PoliticalManifestoEnv',
    'CoffeeEnv',
    'MotifAnalysisEnv',
    'NutritionEnv',
    'MalwareEnv',
    'GeologicalEnv',
    'TheatricalEnv',
    'PrintingTechniqueEnv',
    'StellarEnv',
    'SoilEnv',
    'SoftwareEnv',
    'CarIdentificationEnv',
    'PharmaceuticalEnv',
    'NetworkEnv',
    'BirdNestEnv',
    'EnergyEnv',
    'LanguageEnv',
    'AlgorithmEnv',
    'MathematicalEnv',
    'MusicalEnv',
    'InventorEnv',
    'MedicalEnv',
    'MedicalINDEnv',
    'MedicalOODEnv',
    'MedicalAnonymousEnv',
    'ChemicalEnv',
    'EducationEnv',
    'FantasyEnv',
    'MusicEnv',
]

def load_env(name, datapoint=None):
    
    env = registry.get_environment_class(name)(datapoint)
    
    return env