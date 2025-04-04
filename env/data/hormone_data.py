Truths = {'Calcidiol', 'TSH', 'Dihydrotestosterone (DHT)', 'Somatostatin', 'Growth Hormone (GH)', 'Human Chorionic Gonadotropin (hCG)', 'Thyrotropin-releasing Hormone (TRH)', 'Follicle Stimulating Hormone (FSH)', 'Aldosterone', 'Glucagon', 'Vitamin D (Calcitriol)', 'Antidiuretic Hormone (ADH)', 'Progesterone', 'Luteinizing Hormone (LH)', 'Testosterone', 'Cortisone', 'Histamine', 'Cortisol', 'Triiodothyronine (T3)', 'Epinephrine', 'Serotonin', '17-Hydroxyprogesterone', 'Erythropoietin (EPO)', 'Dopamine', 'Insulin', 'Insulin-like Growth Factor 1 (IGF-1)', 'Estradiol', 'Thyroxine (T4)', 'Parathyroid Hormone (PTH)', 'TRH', 'Prolactin', 'Gonadotropin-releasing Hormone (GnRH)', 'Calcifediol', 'Melatonin', 'Androgens', 'Angiotensin II', 'Oxytocin', 'Renin', 'C-peptide', 'Vasopressin', 'Corticotropin-releasing Hormone (CRH)', 'Thyroid-Stimulating Hormone (TSH)', 'Norepinephrine', 'Adrenocorticotropic Hormone (ACTH)', 'Calcitonin'}
Actions = ['ACTH Stimulation Test', 'Dexamethasone Suppression Test', 'Oral Glucose Tolerance Test', 'Thyroid Function Test', 'Growth Hormone Suppression Test', 'Insulin Tolerance Test', 'Water Deprivation Test', 'Cosyntropin Stimulation Test', 'LH and FSH Level Test', 'Prolactin Level Test', 'Renin-Aldosterone Profile', 'Parathyroid Hormone Level Test', 'Calcium Level Test', 'Cortisol Level Test', 'GnRH Stimulation Test', 'hCG Stimulation Test', 'Glucagon Stimulation Test', 'Overnight Dexamethasone Suppression Test', 'IGF-1 Level Test', 'ACTH Level Test', '17-Hydroxyprogesterone Level Test', 'Free Androgen Index Test', 'Testosterone Level Test', 'Estrogen Level Test', 'Progesterone Level Test', 'Vasopressin Level Test', 'Catecholamine Tests', '5-HIAA Urine Test', 'Calcitonin Level Test', 'Melatonin Level Test', 'Gonadotropin Levels', 'Serum Vitamin D Level Test', 'Glucose Level Test', 'Osmolality Serum Test', 'Erythropoietin Level Test', 'Angiotensin II Level Test', 'Aldosterone Level Test', 'C-Peptide Test', 'Serum Serotonin Level Test', 'Catecholamine Clonidine Suppression Test']
Outcomes = {
    'ACTH Stimulation Test': {
        'type': 'float',
        'states': {
            (18, 1000): {'Cortisol', 'Cortisone'},
            (-1000, 18): {'Adrenocorticotropic Hormone (ACTH)'}
        }
    },
    'Dexamethasone Suppression Test': {
        'type': 'float',
        'states': {
            (-1000, 5): {'Cortisol'},
            (5, 1000): {'Adrenocorticotropic Hormone (ACTH)', 'Corticotropin-releasing Hormone (CRH)'}
        }
    },
    'Oral Glucose Tolerance Test': {
        'type': 'str',
        'states': {
            'Normal': {'Insulin', 'Glucagon'},
            'Impaired': {'Somatostatin'},
            'Diabetic': {'Insulin'}
        }
    },
    'Thyroid Function Test': {
        'type': 'str',
        'states': {
            'Normal': {'TRH', 'TSH', 'Triiodothyronine (T3)', 'Thyroxine (T4)'},
            'Hyperthyroid': {'Thyroid-Stimulating Hormone (TSH)', 'Thyrotropin-releasing Hormone (TRH)'},
            'Hypothyroid': {'Triiodothyronine (T3)', 'Thyroxine (T4)'}
        }
    },
    'Growth Hormone Suppression Test': {
        'type': 'float',
        'states': {
            (-1000, 1): {'Somatostatin', 'Growth Hormone (GH)'},
            (1, 1000): {'Insulin-like Growth Factor 1 (IGF-1)'}
        }
    },
    'Insulin Tolerance Test': {
        'type': 'float',
        'states': {
            (0, 5): {'Growth Hormone (GH)', 'Adrenocorticotropic Hormone (ACTH)'},
            (5, 1000): {'Insulin'}
        }
    },
    'Water Deprivation Test': {
        'type': 'str',
        'states': {
            'Concentrated Urine': {'Antidiuretic Hormone (ADH)', 'Vasopressin'},
            'Dilute Urine': {'Aldosterone'}
        }
    },
    'Cosyntropin Stimulation Test': {
        'type': 'float',
        'states': {
            (18, 1000): {'Cortisol'},
            (-1000, 18): {'Adrenocorticotropic Hormone (ACTH)'}
        }
    },
    'LH and FSH Level Test': {
        'type': 'float',
        'states': {
            (0, 15): {'Luteinizing Hormone (LH)', 'Follicle Stimulating Hormone (FSH)'},
            (15, 1000): {'Gonadotropin-releasing Hormone (GnRH)'}
        }
    },
    'Prolactin Level Test': {
        'type': 'float',
        'states': {
            (0, 20): {'Prolactin'},
            (20, 1000): {'Dopamine'}
        }
    },
    'Renin-Aldosterone Profile': {
        'type': 'str',
        'states': {
            'High Aldosterone, Low Renin': {'Renin'},
            'Low Aldosterone, High Renin': {'Aldosterone'},
            'Normal': set()
        }
    },
    'Parathyroid Hormone Level Test': {
        'type': 'float',
        'states': {
            (0, 65): {'Parathyroid Hormone (PTH)'},
            (65, 1000): {'Calcitonin'}
        }
    },
    'Calcium Level Test': {
        'type': 'float',
        'states': {
            (0, 8.5): {'Parathyroid Hormone (PTH)', 'Vitamin D (Calcitriol)'},
            (8.5, 10.5): set(),
            (10.5, 1000): {'Calcitonin'}
        }
    },
    'Cortisol Level Test': {
        'type': 'float',
        'states': {
            (-1000, 5): {'Cortisol'},
            (5, 25): set(),
            (25, 1000): {'Adrenocorticotropic Hormone (ACTH)', 'Corticotropin-releasing Hormone (CRH)'}
        }
    },
    'GnRH Stimulation Test': {
        'type': 'float',
        'states': {
            (0, 5): {'Gonadotropin-releasing Hormone (GnRH)'},
            (5, 1000): {'Luteinizing Hormone (LH)', 'Follicle Stimulating Hormone (FSH)'}
        }
    },
    'hCG Stimulation Test': {
        'type': 'float',
        'states': {
            (0, 5): {'Human Chorionic Gonadotropin (hCG)'},
            (5, 1000): {'Testosterone', 'Estradiol'}
        }
    },
    'Glucagon Stimulation Test': {
        'type': 'float',
        'states': {
            (0, 150): {'Glucagon'},
            (150, 1000): {'Insulin'}
        }
    },
    'Overnight Dexamethasone Suppression Test': {
        'type': 'float',
        'states': {
            (-1000, 5): {'Cortisol'},
            (5, 1000): {'Adrenocorticotropic Hormone (ACTH)'}
        }
    },
    'IGF-1 Level Test': {
        'type': 'float',
        'states': {
            (0, 200): {'Insulin-like Growth Factor 1 (IGF-1)'},
            (200, 1000): {'Growth Hormone (GH)'}
        }
    },
    'ACTH Level Test': {
        'type': 'float',
        'states': {
            (0, 10): {'Adrenocorticotropic Hormone (ACTH)'},
            (10, 1000): {'Corticotropin-releasing Hormone (CRH)'}
        }
    },
    '17-Hydroxyprogesterone Level Test': {
        'type': 'float',
        'states': {
            (-1000, 200): {'17-Hydroxyprogesterone'},
            (200, 1000): {'Cortisol'}
        }
    },
    'Free Androgen Index Test': {
        'type': 'float',
        'states': {
            (0, 10): {'Androgens'},
            (10, 1000): {'Testosterone', 'Dihydrotestosterone (DHT)'}
        }
    },
    'Testosterone Level Test': {
        'type': 'float',
        'states': {
            (0, 300): {'Testosterone'},
            (300, 1000): {'Luteinizing Hormone (LH)', 'Follicle Stimulating Hormone (FSH)'}
        }
    },
    'Estrogen Level Test': {
        'type': 'float',
        'states': {
            (0, 50): {'Estradiol'},
            (50, 1000): {'Luteinizing Hormone (LH)', 'Follicle Stimulating Hormone (FSH)'}
        }
    },
    'Progesterone Level Test': {
        'type': 'float',
        'states': {
            (0, 5): {'Progesterone'},
            (5, 1000): {'Luteinizing Hormone (LH)', 'Follicle Stimulating Hormone (FSH)'}
        }
    },
    'Vasopressin Level Test': {
        'type': 'float',
        'states': {
            (0, 1): {'Antidiuretic Hormone (ADH)'},
            (1, 1000): {'Oxytocin'}
        }
    },
    'Catecholamine Tests': {
        'type': 'float',
        'states': {
            (0, 100): {'Dopamine', 'Norepinephrine', 'Epinephrine'},
            (100, 1000): set()
        }
    },
    '5-HIAA Urine Test': {
        'type': 'float',
        'states': {
            (0, 6): {'Serotonin'},
            (6, 1000): {'Histamine'}
        }
    },
    'Calcitonin Level Test': {
        'type': 'float',
        'states': {
            (0, 10): {'Calcitonin'},
            (10, 1000): {'Parathyroid Hormone (PTH)'}
        }
    },
    'Melatonin Level Test': {
        'type': 'float',
        'states': {
            (0, 20): {'Melatonin'},
            (20, 1000): set()
        }
    },
    'Gonadotropin Levels': {
        'type': 'float',
        'states': {
            (0, 15): {'Gonadotropin-releasing Hormone (GnRH)'},
            (15, 1000): {'Luteinizing Hormone (LH)', 'Follicle Stimulating Hormone (FSH)'}
        }
    },
    'Serum Vitamin D Level Test': {
        'type': 'float',
        'states': {
            (0, 20): {'Vitamin D (Calcitriol)'},
            (20, 50): set(),
            (50, 1000): {'Calcidiol', 'Calcifediol'}
        }
    },
    'Glucose Level Test': {
        'type': 'float',
        'states': {
            (0, 70): {'Glucagon'},
            (70, 100): set(),
            (100, 1000): {'Insulin'}
        }
    },
    'Osmolality Serum Test': {
        'type': 'float',
        'states': {
            (0, 280): {'Antidiuretic Hormone (ADH)'},
            (280, 295): set(),
            (295, 1000): {'Aldosterone'}
        }
    },
    'Erythropoietin Level Test': {
        'type': 'float',
        'states': {
            (0, 9): {'Erythropoietin (EPO)'},
            (9, 1000): {'Renin'}
        }
    },
    'Angiotensin II Level Test': {
        'type': 'float',
        'states': {
            (0, 20): {'Angiotensin II'},
            (20, 1000): {'Renin'}
        }
    },
    'Aldosterone Level Test': {
        'type': 'float',
        'states': {
            (0, 20): {'Aldosterone'},
            (20, 1000): {'Angiotensin II'}
        }
    },
    'C-Peptide Test': {
        'type': 'float',
        'states': {
            (0, 0.5): {'Insulin'},
            (0.5, 2.0): set(),
            (2.0, 1000): {'C-peptide'}
        }
    },
    'Serum Serotonin Level Test': {
        'type': 'float',
        'states': {
            (0, 120): {'Serotonin'},
            (120, 1000): {'Melatonin'}
        }
    },
    'Catecholamine Clonidine Suppression Test': {
        'type': 'str',
        'states': {
            'Suppressed': {'Norepinephrine', 'Epinephrine'},
            'Not Suppressed': {'Dopamine'}
        }
    }
}