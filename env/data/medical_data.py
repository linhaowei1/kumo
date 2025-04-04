
Diseases = [
'Emphysema',
'Hypertension',
'Colon Cancer',
'Tuberculosis',
'Rheumatoid Arthritis',
'Pre-Diabetes',
'Sepsis',
'Anemia of Chronic Disease',
"Inflammatory Bowel Disease (Crohn's Disease)",
'Non-Alcoholic Fatty Liver Disease',
'Heart Failure',
'Lung Cancer',
'Multiple Sclerosis',
'Hypothyroidism',
'Sarcoidosis',
'Epilepsy',
'Osteoporosis',
'Arrhythmia',
'Vitamin B12 Deficiency Anemia',
'Hepatitis C',
'Iron Deficiency Anemia',
'Valvular Heart Disease',
'HIV/AIDS',
'Depression',
'Diabetes Mellitus Type 1',
'Hyperthyroidism',
'Deep Vein Thrombosis',
'Diabetes Mellitus Type 2',
'Metabolic Syndrome',
'COVID-19',
'Chronic Obstructive Pulmonary Disease (COPD)',
'Bipolar Disorder',
'Leukemia',
'Brain Tumor',
'Peptic Ulcer Disease',
'Myocardial Infarction',
'Asthma',
'Interstitial Lung Disease',
'Unstable Angina',
'Stroke',
'Kidney Stones',
'Hepatitis B',
'Bacterial Infection',
'Fungal Infection',
'Chronic Bronchitis',
'Alcoholic Liver Disease',
'Aortic Stenosis',
'Urinary Tract Infection',
'Osteopenia',
'Nephrotic Syndrome',
'Systemic Lupus Erythematosus (SLE)',
'Gastroesophageal Reflux Disease (GERD)',
'Inflammatory Bowel Disease (Ulcerative Colitis)',
'Pulmonary Embolism',
'Thyroiditis',
'Viral Infection',
'Coronary Artery Disease',
'Vitamin D Deficiency',
'Influenza',
'Folate Deficiency Anemia',
'Pulmonary Fibrosis',
'Pneumonia',
'Anxiety Disorder',
'Stable Angina',
'Chronic Kidney Disease'
]

Diagnosis = [
    "COVID-19 PCR Test",
    "Influenza Rapid Antigen Test",
    "Complete Blood Count (CBC)",
    "Peripheral Blood Smear",
    "Iron Studies",
    "Vitamin B12 Level",
    "Folate Level",
    "Chest X-Ray",
    "Chest CT Scan",
    "Pulmonary Function Tests (Spirometry)",
    "Tuberculin Skin Test (Mantoux Test)",
    "Sputum Culture",
    "Blood Glucose Test",
    "HbA1c Test",
    "Lipid Profile",
    "Thyroid Function Tests (TSH, T3, T4)",
    "Rheumatoid Factor Test",
    "Anti-Nuclear Antibody (ANA) Test",
    "Erythrocyte Sedimentation Rate (ESR)",
    "C-Reactive Protein (CRP)",
    "Electrocardiogram (ECG)",
    "Echocardiogram",
    "Liver Function Tests",
    "Kidney Function Tests",
    "Urinalysis",
    "HIV Antibody Test",
    "Hepatitis B Surface Antigen (HBsAg) Test",
    "Hepatitis C Antibody (Anti-HCV) Test",
    "Upper Endoscopy",
    "Colonoscopy",
    "Brain MRI",
    "Electroencephalogram (EEG)",
    "Bone Mineral Density Test",
    "Vitamin D Level",
    "Depression Screening Questionnaire",
    "Anxiety Screening Questionnaire",
    "D-Dimer Test",
    "Troponin Levels",
    "Urine Culture",
    "Blood Culture"
]

Outcomes = {
    "COVID-19 PCR Test": {
        "type": "str",
        "states": {
            "positive": set(),
            "negative": {"COVID-19"}
        }
    },
    "Influenza Rapid Antigen Test": {
        "type": "str",
        "states": {
            "positive": set(),
            "negative": {"Influenza"}
        }
    },
    "Complete Blood Count (CBC)": {
        "type": "str",
        "states": {
            "normal": {
                "Iron Deficiency Anemia",
                "Vitamin B12 Deficiency Anemia",
                "Folate Deficiency Anemia",
                "Anemia of Chronic Disease",
                "Leukemia",
                "Bacterial Infection",
                "Viral Infection",
                "Fungal Infection",
                "Sepsis"
            },
            "anemia": set(),
            "leukocytosis": set(),
            "leukopenia": set(),
            "thrombocytopenia": set()
        }
    },
    "Peripheral Blood Smear": {
        "type": "str",
        "states": {
            "normal": {
            "Iron Deficiency Anemia",
            "Vitamin B12 Deficiency Anemia",
            "Folate Deficiency Anemia",
            "Anemia of Chronic Disease",
            "Leukemia",
            },
            "microcytic_hypochromic": {
                "Vitamin B12 Deficiency Anemia",
                "Folate Deficiency Anemia",
                "Leukemia"
            },
            "macrocytic": {
                "Iron Deficiency Anemia",
                "Anemia of Chronic Disease",
                "Leukemia"
            },
            "sickle_cells": {
                "Iron Deficiency Anemia",
                "Vitamin B12 Deficiency Anemia",
                "Folate Deficiency Anemia",
                "Anemia of Chronic Disease",
                "Leukemia"
            },
            "blast_cells": {
                "Iron Deficiency Anemia",
                "Vitamin B12 Deficiency Anemia",
                "Folate Deficiency Anemia",
                "Anemia of Chronic Disease"
            }
        }
    },
    "Iron Studies": {
        "type": "str",
        "states": {
            "normal": {
                "Iron Deficiency Anemia"
            },
            "iron_deficiency": set(),
            "anemia_of_chronic_disease": set()
        }
    },
    "Vitamin B12 Level": {
        "type": "float",
        "states": {
            (0, 200): set(),
            (200, 300): set(),
            (300, 2000): {"Vitamin B12 Deficiency Anemia"}
        }
    },
    "Folate Level": {
        "type": "float",
        "states": {
            (0, 3): set(),
            (3, 5): set(),
            (5, 50): {"Folate Deficiency Anemia"}
        }
    },
    "Chest X-Ray": {
        "type": "str",
        "states": {
            "normal": {
                "Pneumonia",
                "Tuberculosis",
                "Lung Cancer",
                "Sarcoidosis",
                "Interstitial Lung Disease",
                "Pulmonary Fibrosis"
            },
            "infiltrates": {
                "Asthma",
                "Chronic Obstructive Pulmonary Disease (COPD)"
            },
            "consolidation": {
                "Asthma",
                "Chronic Obstructive Pulmonary Disease (COPD)"
            },
            "cavitation": {
                "Asthma",
                "Chronic Obstructive Pulmonary Disease (COPD)"
            },
            "mass": {
                "Asthma",
                "Chronic Obstructive Pulmonary Disease (COPD)",
                "Pneumonia"
            },
            "pleural_effusion": {
                "Asthma",
                "Chronic Obstructive Pulmonary Disease (COPD)"
            },
            "interstitial_pattern": {
                "Asthma",
                "Chronic Obstructive Pulmonary Disease (COPD)"
            },
            "hilar_adenopathy": {
                "Asthma",
                "Chronic Obstructive Pulmonary Disease (COPD)"
            }
        }
    },
    "Chest CT Scan": {
        "type": "str",
        "states": {
            "normal": {
                "Lung Cancer",
                "Pulmonary Embolism",
                "Sarcoidosis",
                "Interstitial Lung Disease",
                "Pulmonary Fibrosis"
            },
            "nodule": {
                "Pulmonary Fibrosis"
            },
            "ground_glass_opacity": {
                "Lung Cancer",
                "Pulmonary Embolism"
            },
            "mass": {
                "Pulmonary Fibrosis",
                "Pulmonary Embolism"
            },
            "fibrosis": {
                "Sarcoidosis",
                "Pulmonary Embolism"
            },
            "lymphadenopathy": {
                "Pulmonary Embolism"
            }
        }
    },
    "Pulmonary Function Tests (Spirometry)": {
        "type": "str",
        "states": {
            "normal": {
                "Asthma",
                "Chronic Obstructive Pulmonary Disease (COPD)",
                "Chronic Bronchitis",
                "Emphysema",
                "Interstitial Lung Disease"
            },
            "obstructive_pattern": {
                "Interstitial Lung Disease"
            },
            "restrictive_pattern": {
                "Asthma",
                "Chronic Bronchitis",
                "Emphysema"
            },
            "mixed_pattern": set()
        }
    },
    "Tuberculin Skin Test (Mantoux Test)": {
        "type": "str",
        "states": {
            "positive": set(),
            "negative": {"Tuberculosis"}
        }
    },
    "Sputum Culture": {
        "type": "str",
        "states": {
            "normal_flora": {"Pneumonia"},
            "pathogen_identified": {
                "Asthma",
                "Chronic Obstructive Pulmonary Disease (COPD)",
                "Interstitial Lung Disease",
                "Pulmonary Fibrosis"
            },
            "acid_fast_bacilli": {"Pneumonia"},
            "fungal_elements": set()
        }
    },
    "Blood Glucose Test": {
    "type": "float",
    "states": {
        (0, 99): {
            "Diabetes Mellitus Type 1",
            "Diabetes Mellitus Type 2",
            "Pre-Diabetes",
            "Metabolic Syndrome"
        },
        (100, 125): {
            "Diabetes Mellitus Type 1",
            "Diabetes Mellitus Type 2"
        },
        (126, 500): {
            "Pre-Diabetes",
        }
        }
    },
    "HbA1c Test": {
        "type": "float",
        "states": {
            (0.0, 5.6): {
                "Diabetes Mellitus Type 1",
                "Diabetes Mellitus Type 2",
                "Pre-Diabetes",
                "Metabolic Syndrome"
            },
            (5.7, 6.4): {
                "Diabetes Mellitus Type 1",
                "Diabetes Mellitus Type 2"
            },
            (6.5, 15.0): {"Pre-Diabetes"}
        }
    },
    "Lipid Profile": {
        "type": "str",
        "states": {
            "normal": {
                "Metabolic Syndrome",
                "Coronary Artery Disease"
            },
            "elevated_cholesterol": set(),
            "elevated_triglycerides": set(),
            "low_hdl": set()
        }
    },
    "Thyroid Function Tests (TSH, T3, T4)": {
        "type": "str",
        "states": {
            "normal": {
                "Hypothyroidism",
                "Hyperthyroidism",
                "Thyroiditis"
            },
            "hypothyroidism": {
                "Hyperthyroidism"
            },
            "hyperthyroidism": {
                "Hypothyroidism"
            },
            "thyroiditis": set()
        }
    },
    "Rheumatoid Factor Test": {
        "type": "str",
        "states": {
            "positive": set(),
            "negative": {"Rheumatoid Arthritis"}
        }
    },
    "Anti-Nuclear Antibody (ANA) Test": {
        "type": "str",
        "states": {
            "positive": set(),
            "negative": {"Systemic Lupus Erythematosus (SLE)"}
        }
    },
    "Erythrocyte Sedimentation Rate (ESR)": {
        "type": "float",
        "states": {
            (0, 20): {
                "Bacterial Infection",
                "Viral Infection",
                "Fungal Infection",
                "Anemia of Chronic Disease",
                "Rheumatoid Arthritis",
                "Systemic Lupus Erythematosus (SLE)"
            },
            (21, 100): set()
        }
    },
    "C-Reactive Protein (CRP)": {
        "type": "float",
        "states": {
            (0, 5): {
                "Bacterial Infection",
                "Viral Infection",
                "Fungal Infection",
                "Anemia of Chronic Disease",
                "Rheumatoid Arthritis",
                "Systemic Lupus Erythematosus (SLE)"
            },
            (6, 200): set()
        }
    },
    "Electrocardiogram (ECG)": {
        "type": "str",
        "states": {
            "normal": {
                "Arrhythmia",
                "Myocardial Infarction",
                "Unstable Angina",
                "Stable Angina"
            },
            "arrhythmia": set(),
            "ischemic_changes": set(),
            "left_ventricular_hypertrophy": set(),
            "myocardial_infarction_pattern": set()
        }
    },
    "Echocardiogram": {
        "type": "str",
        "states": {
            "normal": {
                "Heart Failure",
                "Valvular Heart Disease",
                "Aortic Stenosis"
            },
            "reduced_ejection_fraction": set(),
            "valve_abnormalities": set(),
            "hypertrophy": set()
        }
    },
    "Liver Function Tests": {
        "type": "str",
        "states": {
            "normal": {
                "Non-Alcoholic Fatty Liver Disease",
                "Alcoholic Liver Disease"
            },
            "elevated_enzymes": set(),
            "low_albumin": set()
        }
    },
    "Kidney Function Tests": {
        "type": "float",
        "states": {
            (0, 1.1): {
                "Chronic Kidney Disease",
                "Hypertension",
                "Nephrotic Syndrome"
            },
            (1.2, 10.0): set()
        }
    },
    "Urinalysis": {
        "type": "str",
        "states": {
            "normal": {
                "Urinary Tract Infection",
                "Kidney Stones",
                "Nephrotic Syndrome"
            },
            "proteinuria": set(),
            "hematuria": set()
        }
    },
    "HIV Antibody Test": {
        "type": "str",
        "states": {
            "positive": set(),
            "negative": {"HIV/AIDS"}
        }
    },
    "Hepatitis B Surface Antigen (HBsAg) Test": {
        "type": "str",
        "states": {
            "positive": set(),
            "negative": {"Hepatitis B"}
        }
    },
    "Hepatitis C Antibody (Anti-HCV) Test": {
        "type": "str",
        "states": {
            "positive": set(),
            "negative": {"Hepatitis C"}
        }
    },
    "Upper Endoscopy": {
        "type": "str",
        "states": {
            "normal": {
                "Peptic Ulcer Disease",
                "Gastroesophageal Reflux Disease (GERD)"
            },
            "esophagitis": set(),
            "gastric_ulcer": set(),
            "duodenal_ulcer": set()
        }
    },
    "Colonoscopy": {
        "type": "str",
        "states": {
            "normal": {
                "Inflammatory Bowel Disease (Crohn's Disease)",
                "Inflammatory Bowel Disease (Ulcerative Colitis)",
                "Colon Cancer"
            },
            "polyps": set(),
            "diverticulosis": set(),
            "inflammatory_changes": set(),
            "tumor": set()
        }
    },
    "Brain MRI": {
        "type": "str",
        "states": {
            "normal": {
                "Brain Tumor",
                "Multiple Sclerosis",
                "Stroke",
                "Epilepsy"
            },
            "brain_lesions": set(),
            "white_matter_changes": set(),
            "infarct": set()
        }
    },
    "Electroencephalogram (EEG)": {
        "type": "str",
        "states": {
            "normal": {"Epilepsy"},
            "epileptiform_activity": set()
        }
    },
    "Bone Mineral Density Test": {
        "type": "float",
        "states": {
            (-4.0, -2.5): {"Osteopenia"},
            (-2.5, -1.0): {"Osteoporosis"},
            (-1.0, 4.0): {
                "Osteoporosis",
                "Osteopenia"
            }
        }
    },
    "Vitamin D Level": {
        "type": "float",
        "states": {
            (0, 20): set(),
            (20, 30): set(),
            (30, 100): {"Vitamin D Deficiency"}
        }
    },
    "Depression Screening Questionnaire": {
        "type": "str",
        "states": {
            "positive": set(),
            "negative": {
                "Depression",
                "Anxiety Disorder",
                "Bipolar Disorder"
                }
        }
    },
    "Anxiety Screening Questionnaire": {
        "type": "str",
        "states": {
            "positive": set(),
            "negative": {
                "Anxiety Disorder",
                "Depression",
                "Bipolar Disorder"
                }
        }
    },
    "D-Dimer Test": {
        "type": "str",
        "states": {
            "normal": {"Pulmonary Embolism", "Deep Vein Thrombosis"},
            "elevated": set()
        }
    },
    "Troponin Levels": {
        "type": "str",
        "states": {
            "normal": {"Myocardial Infarction", "Unstable Angina"},
            "elevated": set()
        }
    },
    "Urine Culture": {
        "type": "str",
        "states": {
            "no_growth": {"Urinary Tract Infection"},
            "bacterial_growth": set()
        }
    },
    "Blood Culture": {
        "type": "str",
        "states": {
            "no_growth": {
                "Sepsis",
                "Bacterial Infection",
                "Fungal Infection",
                "Viral Infection"
            },
            "bacterial_growth": set()
        }
    }
}
