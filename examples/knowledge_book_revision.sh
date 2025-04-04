#!/bin/bash

# Alternate the loop conditions to evaluate on different domains
# Evaluate on the 5 domains that possess two difficulty settings: Hard and Easy
for domain in 'MedicalEnv' 'EducationEnv' 'MusicEnv' 'FantasyEnv' 'ChemicalEnv';
do

# # Evaluate on the 95 domains that possess Easy setting
# for domain in 'HerbEnv' 'TransdimensionalEnv' 'SorcererEnv' 'QuantumEnv' 'AstronomyEnv' 'MusicGenresEnv' 'CloudEnv' 'CuisineEnv' 'PlantEnv' 'HistoricalEnv' 'GadgetEnv' 'TimeTravelEnv' 'PollutionEnv' 'DemographicEnv' 'CraftsmanEnv' 'StarConstellationEnv' 'MythicalCreatureEnv' 'ArtStyleEnv' 'CookingEnv' 'HistoricalBattleEnv' 'FungalEnv' 'CryptographyEnv' 'StorageEnv' 'RoverEnv' 'FashionEnv' 'LicenseEnv' 'VirusClassificationEnv' 'TestingEnv' 'NarrativeDetectEnv' 'RenewableEnergyEnv' 'CelestialEnv' 'SpiceEnv' 'WildlifeEnv' 'VehicleEnv' 'BeverageEnv' 'ControlEnv' 'CurrencyEnv' 'MarketingEnv' 'BotanicalEnv' 'CircusActEnv' 'AudioDialectEnv' 'LeadershipEnv' 'TransportEnv' 'EcologicalEnv' 'MythicEnv' 'EnzymeEnv' 'OSKernelEnv' 'MineralClassificationEnv' 'EconomicEnv' 'DetectiveEnv' 'ChessEnv' 'MythicalEnv' 'ChemicalCompoundsEnv' 'ArchitecturalEnv' 'ComputationEnv' 'MachinePartEnv' 'LiteraryEnv' 'MarineEnv' 'PhilosophyEnv' 'ArchaeologicalEnv' 'GemstoneEnv' 'GeneticEnv' 'MicrobiologyEnv' 'SciFiEnv' 'HormoneEnv' 'SculptorEnv' 'NeuroEnv' 'OceanEnv' 'MineralEnv' 'FishEnv' 'MartialArtsEnv' 'RocketFuelEnv' 'MLEnv' 'PoliticalManifestoEnv' 'CoffeeEnv' 'MotifAnalysisEnv' 'NutritionEnv' 'MalwareEnv' 'GeologicalEnv' 'TheatricalEnv' 'PrintingTechniqueEnv' 'StellarEnv' 'SoilEnv' 'SoftwareEnv' 'CarIdentificationEnv' 'PharmaceuticalEnv' 'NetworkEnv' 'BirdNestEnv' 'EnergyEnv' 'LanguageEnv' 'AlgorithmEnv' 'MathematicalEnv' 'MusicalEnv' 'InventorEnv' 'RelicEnv';
# do
    load_type=OPENAI
    api_key=EMPTY
    api_base=http://localhost:8001/v1
    model_name_or_path=EMPTY

    cmd="python knowledge_book_revision.py \
    --load_type $load_type \
    --api_base $api_base \
    --model_name_or_path $model_name_or_path \
    --api_key $api_key \
    --domain $domain \
    --revision_template_path ./templates/revision_template.md"
    echo $cmd
    eval $cmd &
done
wait