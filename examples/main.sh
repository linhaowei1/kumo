#!/bin/bash

agent_type=VanillaAgent
action_num_lst=(6 16)
truth_num_lst=(4 12)


# Alternate the loop conditions to evaluate on different domains
# Evaluate on the 5 domains that possess two difficulty settings: Hard and Easy
for domain in 'MedicalEnv' 'EducationEnv' 'MusicEnv' 'FantasyEnv' 'ChemicalEnv';
do
for id in 0 1;
do

# # Evaluate on the 95 domains that possess Easy setting
# for domain in 'HerbEnv' 'TransdimensionalEnv' 'SorcererEnv' 'QuantumEnv' 'AstronomyEnv' 'MusicGenresEnv' 'CloudEnv' 'CuisineEnv' 'PlantEnv' 'HistoricalEnv' 'GadgetEnv' 'TimeTravelEnv' 'PollutionEnv' 'DemographicEnv' 'CraftsmanEnv' 'StarConstellationEnv' 'MythicalCreatureEnv' 'ArtStyleEnv' 'CookingEnv' 'HistoricalBattleEnv' 'FungalEnv' 'CryptographyEnv' 'StorageEnv' 'RoverEnv' 'FashionEnv' 'LicenseEnv' 'VirusClassificationEnv' 'TestingEnv' 'NarrativeDetectEnv' 'RenewableEnergyEnv' 'CelestialEnv' 'SpiceEnv' 'WildlifeEnv' 'VehicleEnv' 'BeverageEnv' 'ControlEnv' 'CurrencyEnv' 'MarketingEnv' 'BotanicalEnv' 'CircusActEnv' 'AudioDialectEnv' 'LeadershipEnv' 'TransportEnv' 'EcologicalEnv' 'MythicEnv' 'EnzymeEnv' 'OSKernelEnv' 'MineralClassificationEnv' 'EconomicEnv' 'DetectiveEnv' 'ChessEnv' 'MythicalEnv' 'ChemicalCompoundsEnv' 'ArchitecturalEnv' 'ComputationEnv' 'MachinePartEnv' 'LiteraryEnv' 'MarineEnv' 'PhilosophyEnv' 'ArchaeologicalEnv' 'GemstoneEnv' 'GeneticEnv' 'MicrobiologyEnv' 'SciFiEnv' 'HormoneEnv' 'SculptorEnv' 'NeuroEnv' 'OceanEnv' 'MineralEnv' 'FishEnv' 'MartialArtsEnv' 'RocketFuelEnv' 'MLEnv' 'PoliticalManifestoEnv' 'CoffeeEnv' 'MotifAnalysisEnv' 'NutritionEnv' 'MalwareEnv' 'GeologicalEnv' 'TheatricalEnv' 'PrintingTechniqueEnv' 'StellarEnv' 'SoilEnv' 'SoftwareEnv' 'CarIdentificationEnv' 'PharmaceuticalEnv' 'NetworkEnv' 'BirdNestEnv' 'EnergyEnv' 'LanguageEnv' 'AlgorithmEnv' 'MathematicalEnv' 'MusicalEnv' 'InventorEnv' 'RelicEnv';
# do
# for id in 0;
# do

    action_num=${action_num_lst[$id]}
    truth_num=${truth_num_lst[$id]}
    valid_truth_num=1
    eval_times=5
    data_num=50
    load_type=OPENAI


    api_base=http://localhost:8001/v1 # api_base here
    api_key=EMPTY # api_key here
    model_name_or_path='EMPTY' # model name here


    cmd="python main.py \
    --agent_type $agent_type \
    --load_type $load_type \
    --action_num $action_num \
    --valid_truth_num $valid_truth_num \
    --api_base $api_base \
    --api_key $api_key \
    --model_name_or_path $model_name_or_path \
    --domain $domain \
    --truth_num $truth_num \
    --eval_times $eval_times \
    --data_num $data_num"

    echo $cmd
    eval $cmd &
done
done
wait