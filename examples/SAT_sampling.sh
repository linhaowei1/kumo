#!/bin/bash

data_num=50
truth_num=(4 12)
action_num=(6 16)

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

    cmd="python SAT_sampling.py \
        --truth_num $truth_num \
        --action_num $action_num \
        --valid_truth_num $valid_truth_num \
        --data_num $data_num \
        --domain $domain"
    
    echo $cmd
    eval $cmd
done
done
wait
