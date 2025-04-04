Abilities = [
    "Critical Thinking",
    "Basic Arithmetic",
    "Problem-Solving",
    "Reading Comprehension",
    "Spatial Reasoning",
    "Memory Retention",
    "Verbal Communication",
    "Logical Reasoning",
    "Creativity",
    "Emotional Intelligence",
    "Attention to Detail",
    "Time Management",
    "Organization Skills",
    "Self-Motivation",
    "Adaptability",
    "Decision-Making",
    "Leadership",
    "Collaboration",
    "Digital Literacy",
    "Foreign Language Proficiency",
    "Analytical Skills",
    "Writing Skills",
    "Listening Skills",
    "Numeracy Skills",
    "Handwriting",
    "Typing Skills",
    "Research Skills",
    "Data Interpretation",
    "Scientific Reasoning",
    "Mechanical Reasoning",
    "Musical Ability",
    "Artistic Ability",
    "Physical Coordination",
    "Public Speaking",
    "Grammar and Syntax",
    "Vocabulary",
    "Concentration",
    "Study Skills",
    "Test-Taking Strategies",
    "Self-Discipline",
    "Empathy",
    "Conflict Resolution",
    "Initiative",
    "Perseverance",
    "Hypothesis Formulation",
    "Observation Skills",
    'Communication Skills',
    'Fine Motor Skills',
    'Confidence'
]

Tests = [
    "Math Test",
    "Critical Thinking Test",
    "Reading Test",
    "Spatial Reasoning Puzzle",
    "Memory Recall Test",
    "Verbal Communication Exercise",
    "Logic Puzzle",
    "Creativity Assessment",
    "Emotional Intelligence Survey",
    "Detail Observation Task",
    "Time Management Simulation",
    "Organizational Skills Task",
    "Self-Motivation Questionnaire",
    "Adaptability Challenge",
    "Decision-Making Scenario",
    "Leadership Role-Play",
    "Group Collaboration Project",
    "Computer Skills Test",
    "Foreign Language Exam",
    "Analytical Reasoning Test",
    "Essay Writing Assignment",
    "Listening Comprehension Test",
    "Numeracy Skills Assessment",
    "Handwriting Analysis",
    "Typing Speed Test",
    "Research Project",
    "Data Interpretation Exercise",
    "Science Experiment",
    "Mechanical Aptitude Test",
    "Musical Performance",
    "Art Project",
    "Physical Coordination Test",
    "Public Speaking Presentation",
    "Grammar Quiz",
    "Vocabulary Test",
    "Concentration Exercise",
    "Study Habits Survey",
    "Test-Taking Skills Assessment",
    "Self-Discipline Challenge",
    "Empathy Questionnaire"
]

Outcomes = {
    "Math Test": {
        "type": "float",
        "states": {
            (90, 100): {"Basic Arithmetic", "Problem-Solving", "Numeracy Skills"},
            (70, 89): {"Problem-Solving"},
            (0, 69): set(),
        }
    },
    "Critical Thinking Test": {
        "type": "str",
        "states": {
            "Excellent": {"Critical Thinking", "Logical Reasoning", "Analytical Skills"},
            "Good": {"Logical Reasoning"},
            "Poor": set(),
        }
    },
    "Reading Test": {
        "type": "float",
        "states": {
            (85, 100): {"Reading Comprehension", "Vocabulary", "Grammar and Syntax"},
            (60, 84): {"Vocabulary"},
            (0, 59): set(),
        }
    },
    "Spatial Reasoning Puzzle": {
        "type": "str",
        "states": {
            "Completed Quickly": {"Spatial Reasoning", "Problem-Solving"},
            "Completed Slowly": set(),
            "Incomplete": set(),
        }
    },
    "Memory Recall Test": {
        "type": "float",
        "states": {
            (90, 100): {"Memory Retention", "Attention to Detail"},
            (70, 89): {"Attention to Detail"},
            (0, 69): set(),
        }
    },
    "Verbal Communication Exercise": {
        "type": "str",
        "states": {
            "Outstanding": {"Verbal Communication", "Public Speaking"},
            "Satisfactory": {"Verbal Communication"},
            "Needs Improvement": set(),
        }
    },
    "Logic Puzzle": {
        "type": "str",
        "states": {
            "Solved Quickly": {"Logical Reasoning", "Problem-Solving"},
            "Solved Slowly": {"Problem-Solving"},
            "Unsolved": set(),
        }
    },
    "Creativity Assessment": {
        "type": "str",
        "states": {
            "Highly Creative": {"Creativity", "Artistic Ability"},
            "Moderately Creative": {"Creativity"},
            "Not Creative": set(),
        }
    },
    "Emotional Intelligence Survey": {
        "type": "float",
        "states": {
            (80, 100): {"Emotional Intelligence", "Empathy", "Conflict Resolution"},
            (60, 79): {"Empathy"},
            (0, 59): set(),
        }
    },
    "Detail Observation Task": {
        "type": "str",
        "states": {
            "Noticed All Details": {"Attention to Detail", "Observation Skills"},
            "Missed Some Details": {"Observation Skills"},
            "Missed Many Details": set(),
        }
    },
    "Time Management Simulation": {
        "type": "float",
        "states": {
            (85, 100): {"Time Management", "Organization Skills", "Self-Discipline"},
            (60, 84): {"Time Management"},
            (0, 59): set(),
        }
    },
    "Organizational Skills Task": {
        "type": "str",
        "states": {
            "Highly Organized": {"Organization Skills"},
            "Moderately Organized": {"Organization Skills"},
            "Disorganized": set(),
        }
    },
    "Self-Motivation Questionnaire": {
        "type": "float",
        "states": {
            (80, 100): {"Self-Motivation", "Perseverance", "Initiative"},
            (50, 79): {"Self-Motivation"},
            (0, 49): set(),
        }
    },
    "Adaptability Challenge": {
        "type": "str",
        "states": {
            "Adapted Easily": {"Adaptability", "Self-Motivation"},
            "Struggled to Adapt": set(),
            "Did Not Adapt": set(),
        }
    },
    "Decision-Making Scenario": {
        "type": "str",
        "states": {
            "Made Effective Decisions": {"Decision-Making", "Problem-Solving", "Analytical Skills"},
            "Indecisive": set(),
            "Made Poor Decisions": set(),
        }
    },
    "Leadership Role-Play": {
        "type": "float",
        "states": {
            (90, 100): {"Leadership", "Collaboration", "Verbal Communication"},
            (70, 89): {"Leadership"},
            (0, 69): set(),
        }
    },
    "Group Collaboration Project": {
        "type": "str",
        "states": {
            "Excellent Team Player": {"Collaboration", "Communication Skills", "Empathy"},
            "Average Team Player": {"Collaboration"},
            "Poor Team Player": set(),
        }
    },
    "Computer Skills Test": {
        "type": "str",
        "states": {
            "Advanced": {"Digital Literacy", "Typing Skills"},
            "Intermediate": {"Digital Literacy"},
            "Beginner": set(),
        }
    },
    "Foreign Language Exam": {
        "type": "float",
        "states": {
            (85, 100): {"Foreign Language Proficiency", "Memory Retention"},
            (60, 84): {"Foreign Language Proficiency"},
            (0, 59): set(),
        }
    },
    "Analytical Reasoning Test": {
        "type": "float",
        "states": {
            (90, 100): {"Analytical Skills", "Critical Thinking", "Logical Reasoning"},
            (70, 89): {"Analytical Skills"},
            (0, 69): set(),
        }
    },
    "Essay Writing Assignment": {
        "type": "str",
        "states": {
            "Excellent": {"Writing Skills", "Grammar and Syntax", "Critical Thinking"},
            "Good": {"Writing Skills"},
            "Needs Improvement": set(),
        }
    },
    "Listening Comprehension Test": {
        "type": "float",
        "states": {
            (85, 100): {"Listening Skills", "Concentration", "Memory Retention"},
            (60, 84): {"Listening Skills"},
            (0, 59): set(),
        }
    },
    "Numeracy Skills Assessment": {
        "type": "str",
        "states": {
            "Advanced": {"Numeracy Skills", "Basic Arithmetic", "Problem-Solving"},
            "Intermediate": {"Numeracy Skills"},
            "Beginner": set(),
        }
    },
    "Handwriting Analysis": {
        "type": "str",
        "states": {
            "Legible and Neat": {"Handwriting", "Fine Motor Skills"},
            "Legible": {"Handwriting"},
            "Illegible": set(),
        }
    },
    "Typing Speed Test": {
        "type": "float",
        "states": {
            (60, 100): {"Typing Skills", "Digital Literacy"},
            (30, 59): {"Typing Skills"},
            (0, 29): set(),
        }
    },
    "Research Project": {
        "type": "str",
        "states": {
            "Thorough and Insightful": {"Research Skills", "Critical Thinking", "Writing Skills"},
            "Adequate": {"Research Skills"},
            "Insufficient": set(),
        }
    },
    "Data Interpretation Exercise": {
        "type": "float",
        "states": {
            (85, 100): {"Data Interpretation", "Analytical Skills", "Numeracy Skills"},
            (60, 84): {"Data Interpretation"},
            (0, 59): set(),
        }
    },
    "Science Experiment": {
        "type": "str",
        "states": {
            "Successful and Accurate": {"Scientific Reasoning", "Observation Skills", "Hypothesis Formulation"},
            "Partially Successful": {"Scientific Reasoning"},
            "Unsuccessful": set(),
        }
    },
    "Mechanical Aptitude Test": {
        "type": "float",
        "states": {
            (80, 100): {"Mechanical Reasoning", "Problem-Solving", "Spatial Reasoning"},
            (50, 79): {"Mechanical Reasoning"},
            (0, 49): set(),
        }
    },
    "Musical Performance": {
        "type": "str",
        "states": {
            "Outstanding": {"Musical Ability", "Creativity", "Memory Retention"},
            "Satisfactory": {"Musical Ability"},
            "Needs Improvement": set(),
        }
    },
    "Art Project": {
        "type": "str",
        "states": {
            "Highly Creative": {"Artistic Ability", "Creativity", "Attention to Detail"},
            "Moderately Creative": {"Artistic Ability"},
            "Not Creative": set(),
        }
    },
    "Physical Coordination Test": {
        "type": "float",
        "states": {
            (90, 100): {"Physical Coordination", "Concentration"},
            (70, 89): {"Physical Coordination"},
            (0, 69): set(),
        }
    },
    "Public Speaking Presentation": {
        "type": "str",
        "states": {
            "Engaging and Clear": {"Public Speaking", "Verbal Communication", "Confidence"},
            "Average": {"Public Speaking"},
            "Poor": set(),
        }
    },
    "Grammar Quiz": {
        "type": "float",
        "states": {
            (85, 100): {"Grammar and Syntax", "Writing Skills"},
            (60, 84): {"Grammar and Syntax"},
            (0, 59): set(),
        }
    },
    "Vocabulary Test": {
        "type": "float",
        "states": {
            (85, 100): {"Vocabulary", "Reading Comprehension"},
            (60, 84): {"Vocabulary"},
            (0, 59): set(),
        }
    },
    "Concentration Exercise": {
        "type": "float",
        "states": {
            (90, 100): {"Concentration", "Attention to Detail"},
            (70, 89): {"Concentration"},
            (0, 69): set(),
        }
    },
    "Study Habits Survey": {
        "type": "str",
        "states": {
            "Excellent Habits": {"Study Skills", "Time Management", "Self-Discipline"},
            "Good Habits": {"Study Skills"},
            "Poor Habits": set(),
        }
    },
    "Test-Taking Skills Assessment": {
        "type": "float",
        "states": {
            (85, 100): {"Test-Taking Strategies", "Concentration"},
            (60, 84): {"Test-Taking Strategies"},
            (0, 59): set(),
        }
    },
    "Self-Discipline Challenge": {
        "type": "str",
        "states": {
            "Highly Disciplined": {"Self-Discipline", "Perseverance"},
            "Moderately Disciplined": {"Self-Discipline"},
            "Lacks Discipline": set(),
        }
    },
    "Empathy Questionnaire": {
        "type": "float",
        "states": {
            (80, 100): {"Empathy", "Emotional Intelligence"},
            (50, 79): {"Empathy"},
            (0, 49): set(),
        }
    }
}

# truths_new = set()
# for key, value in Outcomes.items():
#     for v in value["states"].values():
#         #print(v)
#         truths_new.update(v)
#         #print(truths_new)
# outcomes_keys = Outcomes.keys()
# print(set(Abilities)==truths_new)
# print(set(Abilities)-truths_new)
# print(truths_new-set(Abilities))
# in_actions_not_in_outcomes = set(Tests) - set(outcomes_keys)
# in_outcomes_not_in_actions = set(outcomes_keys) - set(Tests)
# print(in_actions_not_in_outcomes)
# print(in_outcomes_not_in_actions)
# print(len(Abilities))
# print(len(Tests))
# print(len(Outcomes))