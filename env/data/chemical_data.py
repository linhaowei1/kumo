Truths = [
    "Acetone", "Benzene", "Ethanol", "Methanol", "Isopropanol", "Toluene", "Hexane", "Heptane", "Octane", "Nonane",
    "Decane", "Ethylene", "Propylene", "Butadiene", "Styrene", "Chloroform", "CarbonTetrachloride", "Dichloromethane",
    "EthylAcetate", "EthyleneGlycol", "Glycerol", "Phenol", "Aniline", "Acetonitrile", "Dimethylformamide",
    "Dimethylsulfoxide", "Formaldehyde", "Acetaldehyde", "AceticAcid", "FormicAcid", "HydrochloricAcid",
    "SulfuricAcid", "NitricAcid", "Ammonia", "SodiumChloride", "PotassiumIodide", "CalciumCarbonate",
    "SodiumBicarbonate", "Glucose", "Fructose", "Sucrose", "LacticAcid", "CitricAcid", "Urea", "Thiourea",
    "BoricAcid", "HydrogenPeroxide", "AceticAnhydride", "Benzaldehyde"
]

Actions = [
    "pH test",
    "Boiling point measurement",
    "Melting point measurement",
    "Density measurement",
    "Refractive index measurement",
    "Flame color test",
    "Solubility in water",
    "Solubility in ethanol",
    "Reaction with sodium metal",
    "Reaction with Fehling's solution",
    "Reaction with bromine water",
    "Reaction with iodine solution",
    "Odor test",
    "UV-Vis absorption",
    "IR absorption band",
    "Conductivity test",
    "Titration with NaOH",
    "Titration with HCl",
    "Color observation",
    "Viscosity measurement",
    "Crystallization test",
    "Reaction with silver nitrate",
    "Reaction with Grignard reagent",
    "Flash point measurement",
    "Reaction with dilute acid",
    "Reaction with dilute base",
    "Paper chromatography Rf",
    "Polarimetry",
    "Mass spectrometry peak",
    "TLC Rf comparison"
]

Outcomes = {
    "pH test": {
        "type": "float",
        "states": {
            (0, 3): {
                "SodiumChloride", "PotassiumIodide", "CalciumCarbonate", "SodiumBicarbonate",
                "Ammonia", "Hexane", "Heptane", "Octane", "Nonane", "Decane"
            },
            (3, 7): {
                "HydrochloricAcid", "SulfuricAcid", "NitricAcid", "Ammonia", "SodiumChloride",
                "PotassiumIodide", "CalciumCarbonate", "SodiumBicarbonate", "EthyleneGlycol", "Glycerol"
            },
            (7, 14): {
                "AceticAcid", "FormicAcid", "LacticAcid", "CitricAcid", "BoricAcid", 
                "Phenol", "Aniline", "Acetonitrile"
            }
        }
    },

    "Boiling point measurement": {
        "type": "float",
        "states": {
            (0, 50): {
                "EthyleneGlycol", "Glycerol", "Phenol", "Dimethylformamide", "Dimethylsulfoxide",
                "AceticAcid", "FormicAcid", "HydrogenPeroxide", "Benzaldehyde"
            },
            (50, 150): {
                "Methanol", "Ethanol", "Acetone", "Benzene", "Chloroform", "Hexane", "Heptane",
                "Toluene", "Acetonitrile", "Formaldehyde", "Acetaldehyde"
            },
            (150, 300): {
                "Nonane", "Decane", "Styrene", "CarbonTetrachloride", "Dichloromethane",
                "EthylAcetate", "Isopropanol", "Propylene", "Ethylene"
            }
        }
    },

    "Melting point measurement": {
        "type": "float",
        "states": {
            (-100, 0): {
                # Extremely low MP excludes substances known to have much higher MP
                "Glucose", "Fructose", "Sucrose", "Urea", "Thiourea",
                "CalciumCarbonate", "SodiumBicarbonate"
            },
            (0, 100): {
                # Moderate MP range excludes those with known very high or characteristic higher MP
                # Removed Urea here to prevent it from always being excluded.
                "BoricAcid", "CitricAcid", "LacticAcid", "AceticAcid",
                "FormicAcid", "Aniline", "Phenol"
            }
        }
    },

    "Density measurement": {
        "type": "float",
        "states": {
            (0.5, 0.8): {
                "Phenol", "Aniline", "AceticAcid", "Dimethylsulfoxide",
                "Dimethylformamide", "AceticAnhydride", "Benzaldehyde"
            },
            (0.8, 1.0): {
                "CarbonTetrachloride", "Chloroform", "Dichloromethane", "SodiumChloride",
                "PotassiumIodide", "CalciumCarbonate"
            },
            (1.0, 1.5): {
                "Hexane", "Heptane", "Octane", "Nonane", "Decane",
                "Styrene", "Toluene", "Benzene"
            }
        }
    },

    "Refractive index measurement": {
        "type": "float",
        "states": {
            # (1.3, 1.4): If observed RI is low, exclude compounds known to have RI much higher than 1.4
            (1.3, 1.4): {
                "Benzene",      # RI ~1.501
                "Styrene",      # RI ~1.546
                "Aniline",      # RI ~1.586
                "Phenol",       # RI ~1.539
                "Toluene",      # RI ~1.4969
                "Dimethylsulfoxide", # RI ~1.479
                "Dimethylformamide"  # RI ~1.4305
            },
            # (1.4, 1.5): RI in this moderate range excludes those with RI well below 1.4 or above 1.5
            (1.4, 1.5): {
                # Below 1.4 (too low)
                "Methanol",     # RI ~1.328
                "Ethanol",      # RI ~1.361
                "Acetone",      # RI ~1.358
                "Isopropanol",  # RI ~1.377
                "Acetaldehyde", # RI ~1.331 approx
                "Formaldehyde", # Aqueous sol ~1.33 approx
                "EthylAcetate", # RI ~1.372

                # Above 1.5 (too high)
                "Benzene",      # RI ~1.501
                "Styrene",      # RI ~1.546
                "Aniline",      # RI ~1.586
                "Phenol",       # RI ~1.539
            },
            (1.5, 1.6): {
                "Methanol",     # RI ~1.328
                "Ethanol",      # RI ~1.361
                "Acetone",      # RI ~1.358
                "Isopropanol",  # RI ~1.377
                "Acetaldehyde", # RI ~1.331 approx
                "Formaldehyde", # Aqueous sol ~1.33 approx
                "EthylAcetate", # RI ~1.372
                "Toluene",      # RI ~1.4969
                "Dimethylsulfoxide", # RI ~1.479
                "Dimethylformamide"  # RI ~1.4305
            }
        }
    },

    "Flame color test": {
        "type": "str",
        "states": {
            "no_color": {
                "SodiumChloride", "PotassiumIodide", "CalciumCarbonate"
            },
            "yellow": {
                "Chloroform", "CarbonTetrachloride", "Dichloromethane"
            },
            "green": {
                "Hexane", "Heptane", "Octane", "Nonane", "Decane", "Toluene", "Benzene"
            }
        }
    },

    "Solubility in water": {
        "type": "str",
        "states": {
            "soluble": {
                "Benzene", "Toluene", "Hexane", "Heptane", "Octane", "Nonane", "Decane", "Styrene"
            },
            "partially_soluble": {
                "SodiumChloride", "PotassiumIodide", "CalciumCarbonate", "SulfuricAcid",
                "NitricAcid", "HydrochloricAcid"
            },
            "insoluble": {
                "Ethanol", "Methanol", "Isopropanol", "Glycerol", "EthyleneGlycol",
                "Dimethylsulfoxide", "Dimethylformamide"
            }
        }
    },

    "Solubility in ethanol": {
        "type": "str",
        "states": {
            "soluble": {
                "SodiumChloride", "CalciumCarbonate", "SodiumBicarbonate"
            },
            "insoluble": {
                "Acetone", "Benzene", "Toluene", "Hexane", "Heptane",
                "Octane", "Nonane", "Decane"
            }
        }
    },

    "Reaction with sodium metal": {
        "type": "str",
        "states": {
            "vigorous_reaction": {
                "Benzene", "Toluene", "Styrene", "Chloroform", "CarbonTetrachloride"
            },
            "no_reaction": {
                "Ethanol", "Methanol", "Isopropanol", "AceticAcid", "FormicAcid", "LacticAcid"
            }
        }
    },

    "Reaction with Fehling's solution": {
        "type": "str",
        "states": {
            "red_precipitate": {
                "Benzene", "Toluene", "Hexane", "Heptane", "Octane", "Nonane", "Decane",
                "Chloroform", "CarbonTetrachloride"
            },
            "no_change": {
                "Glucose", "Fructose", "Formaldehyde", "Acetaldehyde"
            }
        }
    },

    "Reaction with bromine water": {
        "type": "str",
        "states": {
            "decolorization": {
                "Methanol", "Ethanol", "Isopropanol", "Acetone", "Chloroform", "Hexane"
            },
            "no_change": {
                "Ethylene", "Propylene", "Butadiene", "Styrene"
            }
        }
    },

    "Reaction with iodine solution": {
        "type": "str",
        "states": {
            "iodoform_test_positive": {
                "Benzene", "Toluene", "Hexane", "Heptane", "Octane"
            },
            "no_reaction": {
                "Ethanol", "Acetone", "Acetaldehyde"
            }
        }
    },

    "Odor test": {
        "type": "str",
        "states": {
            "pungent": {
                "SodiumChloride", "PotassiumIodide", "CalciumCarbonate", "Glucose", "Fructose", "Sucrose"
            },
            "sweet": {
                "Aniline", "Thiourea", "Ammonia"
            },
            "odorless": {
                "AceticAcid", "FormicAcid", "Benzaldehyde", "Phenol"
            }
        }
    },

    "UV-Vis absorption": {
        "type": "float",
        "states": {
            (200, 250): {
                "Styrene", "Benzene", "Aniline", "Phenol"
            },
            (250, 300): {
                "SodiumChloride", "PotassiumIodide", "CalciumCarbonate"
            }
        }
    },

    "IR absorption band": {
        "type": "str",
        "states": {
            "broad_OH_band": {
                "Hexane", "Heptane", "Octane", "Nonane", "Decane",
                "Toluene", "Benzene", "Chloroform", "CarbonTetrachloride"
            },
            "C=O_stretch": {
                "Benzene", "Toluene", "Heptane", "Hexane", "Propylene", "Ethylene"
            },
            "no_specific_bands": {
                "Ethanol", "Methanol", "Phenol", "AceticAcid", "FormicAcid",
                "Glycerol", "EthyleneGlycol"
            }
        }
    },

    "Conductivity test": {
        "type": "float",
        "states": {
            (0, 10): {
                "SodiumChloride", "PotassiumIodide", "HydrochloricAcid", "SulfuricAcid", "NitricAcid"
            },
            (10, 100): {
                "Benzene", "Toluene", "Hexane", "Heptane", "Octane", "Nonane"
            }
        }
    },

    "Titration with NaOH": {
        "type": "str",
        "states": {
            "requires_large_volume": {
                "Benzene", "Toluene", "Hexane", "Heptane", "Octane", "Nonane", "Decane",
                "Chloroform", "CarbonTetrachloride"
            },
            "no_significant_change": {
                "AceticAcid", "FormicAcid", "CitricAcid", "LacticAcid", "HydrochloricAcid", "NitricAcid"
            }
        }
    },

    "Titration with HCl": {
        "type": "str",
        "states": {
            # "significant_neutralization": indicates the sample neutralizes acid significantly.
            # If this happens, it means the sample is basic. Exclude non-basic (neutral) organics.
            "significant_neutralization": {
                "Benzene", "Toluene", "Hexane", "Heptane", "Octane", "Nonane", "Decane",
                "Chloroform", "CarbonTetrachloride"
            },
            # "no_reaction": No neutralization. This rules out bases and carbonates that would have reacted.
            "no_reaction": {
                "Ammonia", "SodiumBicarbonate", "CalciumCarbonate"
            }
        }
    },

    "Color observation": {
        "type": "str",
        "states": {
            "colorless": {
                "Benzaldehyde", "Phenol", "Aniline", "Styrene"
            },
            "pale_yellow": {
                "Benzene", "Toluene", "Chloroform", "CarbonTetrachloride", "Acetone", "Methanol"
            },
            "dark_brown": {
                "Ethanol", "Isopropanol", "Hexane", "Heptane", "Octane",
                "Glycerol", "EthyleneGlycol"
            }
        }
    },

    "Viscosity measurement": {
        "type": "float",
        "states": {
            (0, 1): {
                "Glycerol", "EthyleneGlycol", "Dimethylsulfoxide", "Phenol"
            },
            (1, 5): {
                "Acetone", "Methanol", "Ethanol", "Isopropanol", "Chloroform"
            }
        }
    },

    "Crystallization test": {
        "type": "str",
        "states": {
            "easy_crystallization": {
                "Acetone", "Ethanol", "Methanol", "Isopropanol", "Benzene", "Toluene"
            },
            "no_crystals": {
                "Glucose", "Fructose", "Sucrose", "Urea", "Thiourea"
            }
        }
    },

    "Reaction with silver nitrate": {
        "type": "str",
        "states": {
            "precipitate": {
                "Benzene", "Toluene", "Hexane", "Heptane", "Octane",
                "Nonane", "Decane", "Phenol"
            },
            "no_precipitate": {
                "Chloroform", "CarbonTetrachloride", "Dichloromethane", "PotassiumIodide"
            }
        }
    },

    "Reaction with Grignard reagent": {
        "type": "str",
        "states": {
            "vigorous_gas_evolution": {
                "AceticAcid", "FormicAcid", "LacticAcid", "CitricAcid", "Phenol", "Aniline"
            },
            "mild_reaction": {
                "Benzene", "Toluene", "Hexane", "Heptane", "Octane", "Nonane"
            }
        }
    },

    "Flash point measurement": {
        "type": "float",
        "states": {
            (-50, 0): {
                "Glycerol", "Dimethylsulfoxide", "Dimethylformamide", "EthyleneGlycol"
            },
            (0, 50): {
                "Hexane", "Heptane", "Octane", "Nonane", "Decane"
            },
            (50, 150): {
                "Acetone", "Methanol", "Ethanol", "Isopropanol", "Chloroform"
            }
        }
    },

    "Reaction with dilute acid": {
        "type": "str",
        "states": {
            "effervescence": {
                "Benzene", "Toluene", "Hexane", "Heptane", "Octane"
            },
            "no_effervescence": {
                "CalciumCarbonate", "SodiumBicarbonate"
            }
        }
    },

    "Reaction with dilute base": {
        "type": "str",
        "states": {
            "salt_formation": {
                "Benzene", "Toluene", "Hexane", "Heptane", "Octane",
                "Nonane", "Decane", "Chloroform"
            },
            "no_reaction": {
                "AceticAcid", "FormicAcid", "LacticAcid", "CitricAcid", "Phenol"
            }
        }
    },

    "Paper chromatography Rf": {
        "type": "float",
        "states": {
            (0.0, 0.3): {
                "Hexane", "Heptane", "Octane", "Nonane", "Decane",
                "Benzene", "Toluene"
            },
            (0.3, 0.7): {
                "Dimethylsulfoxide", "Dimethylformamide", "Glycerol", "EthyleneGlycol"
            }
        }
    },

    "Polarimetry": {
        "type": "float",
        "states": {
            (-10, 0): {
                "Benzene", "Toluene", "Hexane", "Heptane", "Octane", "Chloroform"
            },
            (0, 10): {
                "SodiumChloride", "PotassiumIodide", "CalciumCarbonate", "Sucrose"
            }
        }
    },

    "Mass spectrometry peak": {
        "type": "str",
        "states": {
            "m_z_31_abundant": {
                "Benzene", "Toluene", "Styrene", "Chloroform", "CarbonTetrachloride"
            },
            "no_distinct_peaks": {
                "Acetone", "Ethanol", "Methanol", "Acetaldehyde"
            }
        }
    },

    "TLC Rf comparison": {
        "type": "float",
        "states": {
            (0.0, 0.4): {
                "Hexane", "Heptane", "Octane", "Nonane", "Decane"
            },
            (0.4, 0.8): {
                "Glycerol", "EthyleneGlycol", "FormicAcid", "AceticAcid"
            }
        }
    }
}

# keys = []
# for key, value in Outcomes.items():
#     # check if one state will be always ruled out for some action
#     for truth in Truths:
#         flag = True
#         for state in value["states"].values():
#             if truth not in state:
#                 flag = False
#                 break
#         if flag:
#             print(f'{truth} will be always ruled out for {key}')
            
#             keys.append(key)

# print(set(keys))

# truths_new = set()
# for key, value in Outcomes.items():
#     for v in value["states"].values():
#         #print(v)
#         truths_new.update(v)
#         #print(truths_new)
# outcomes_keys = Outcomes.keys()
# print(f'truth: {truths_new}')
# print(set(Truths)==truths_new)
# print(set(Truths) - truths_new)
# print(truths_new - set(Truths))
# in_actions_not_in_outcomes = set(Actions) - set(outcomes_keys)
# in_outcomes_not_in_actions = set(outcomes_keys) - set(Actions)
# print(in_actions_not_in_outcomes)
# print(in_outcomes_not_in_actions)
# #print(f'actions"{outcomes_keys}')
# print(len(Truths))
# print(len(Actions))
# print(len(Outcomes))