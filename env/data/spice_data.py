Truths = {'Safflower', 'Bay Leaves', 'Kaffir Lime Leaves', 'Cinnamon', 'Anise Seeds', 'Fennel Seeds', 'Gumbo File', 'Sage', 'Galangal', 'Ajwain Seeds', 'Allspice', 'Nigella Seeds', 'Cayenne Pepper', 'Cardamom', 'Mustard Seeds', 'Paprika', 'Tarragon', 'Asafoetida', 'Vanilla Bean', 'Licorice Root', 'White Pepper', 'Sumac', 'Ginger', 'Star Anise', 'Basil', 'Saffron', 'Rosemary', 'Fenugreek', 'Garlic Powder', 'Mace', 'Dill Seeds', 'Black Pepper', 'Coriander Seeds', 'Oregano', 'Thyme', 'Cumin', 'Nutmeg', 'Dried Chiles', 'Horseradish', 'Turmeric', 'Marjoram', 'Wasabi', 'Curry Leaves', 'Onion Powder', 'Szechuan Peppercorns', 'Annatto Seeds', 'Cloves'}
Actions = {
    'Heat Level Measurement', 'Taste Testing', 'Aroma Analysis', 
    'Color Evaluation', 'Texture Analysis', 'Moisture Content Testing', 
    'Chemical Composition Analysis', 'Flavor Profiling'
}
Outcomes = Outcomes = {
    'Aroma Analysis': {
        'type': 'str',
        'states': {
            'Floral Aroma': {
                'Dried Chiles', 'Mustard Seeds', 'Horseradish', 'Black Pepper',
                'Turmeric', 'Wasabi', 'Onion Powder', 'Asafoetida',
                'Ajwain Seeds', 'Cumin', 'Ginger', 'Cayenne Pepper',
                'Garlic Powder'
            },
            'Citrus Aroma': {
                'Mace', 'Mustard Seeds', 'Horseradish', 'Paprika',
                'Black Pepper', 'Turmeric', 'Wasabi', 'Asafoetida',
                'Cinnamon', 'Allspice', 'Cumin', 'Nutmeg',
                'Cayenne Pepper', 'Cloves', 'Garlic Powder'
            },
            'Earthy Aroma': {
                'Curry Leaves', 'Marjoram', 'Kaffir Lime Leaves',
                'Cinnamon', 'Tarragon', 'Vanilla Bean', 'Oregano',
                'Sage', 'Galangal', 'Allspice', 'Basil',
                'Thyme', 'Saffron', 'Nutmeg', 'Rosemary', 'Cloves'
            },
            'Pungent Aroma': {
                'Mace', 'Dill Seeds', 'Cardamom', 'Safflower',
                'Cinnamon', 'Fennel Seeds', 'Vanilla Bean',
                'Licorice Root', 'Gumbo File', 'Allspice',
                'Saffron', 'Annatto Seeds', 'Nutmeg', 'Cloves'
            }
        }
    },
    'Taste Testing': {
        'type': 'str',
        'states': {
            'Spicy Taste': {
                'Safflower', 'Bay Leaves', 'Mace', 'Kaffir Lime Leaves',
                'Vanilla Bean', 'Oregano', 'Licorice Root', 'Sumac',
                'Sage', 'Galangal', 'Basil', 'Thyme', 'Saffron',
                'Annatto Seeds', 'Rosemary'
            },
            'Sweet Taste': {
                'Dried Chiles', 'Mustard Seeds', 'Horseradish', 'Paprika',
                'Black Pepper', 'Wasabi', 'Onion Powder', 'Asafoetida',
                'Ajwain Seeds', 'Nigella Seeds', 'Cayenne Pepper',
                'Garlic Powder'
            },
            'Bitter Taste': {
                'Mace', 'Cardamom', 'Cinnamon', 'Anise Seeds',
                'Fennel Seeds', 'Vanilla Bean', 'Licorice Root',
                'Gumbo File', 'Sumac', 'Allspice', 'Saffron',
                'Nutmeg', 'Cloves', 'Fenugreek'
            },
            'Umami Taste': {
                'Mace', 'Cardamom', 'Cinnamon', 'Anise Seeds',
                'Fennel Seeds', 'Vanilla Bean', 'Allspice',
                'Star Anise', 'Szechuan Peppercorns', 'Saffron',
                'Nutmeg', 'Cloves'
            }
        }
    },
    'Heat Level Measurement': {
        'type': 'float',
        'states': {
            (0, 1000): {
                'Dried Chiles', 'Paprika', 'Black Pepper',
                'Szechuan Peppercorns', 'Cayenne Pepper'
            },
            (1001, 10000): {
                'Mace', 'Cardamom', 'Turmeric', 'Cinnamon',
                'Anise Seeds', 'Fennel Seeds', 'Vanilla Bean',
                'Allspice', 'Star Anise', 'Saffron', 'Nutmeg', 'Cloves'
            },
            (10001, 50000): {
                'Mace', 'Turmeric', 'Black Pepper', 'Coriander Seeds',
                'Cinnamon', 'Anise Seeds', 'Fennel Seeds',
                'Vanilla Bean', 'White Pepper', 'Allspice',
                'Saffron', 'Cumin', 'Nutmeg', 'Cloves'
            },
            (50001, 1000000): {
                'Cinnamon', 'Anise Seeds', 'Fennel Seeds',
                'Allspice', 'Mustard Seeds', 'Asafoetida',
                'Vanilla Bean', 'White Pepper', 'Saffron',
                'Garlic Powder', 'Fenugreek', 'Mace',
                'Black Pepper', 'Coriander Seeds', 'Cumin',
                'Nutmeg', 'Turmeric', 'Onion Powder', 'Cloves'
            }
        }
    },
    'Color Evaluation': {
        'type': 'str',
        'states': {
            'Red': {
                'Paprika', 'Cayenne Pepper', 'Dried Chiles', 'Turmeric'
            },
            'Brown': {
                'Cinnamon', 'Cloves', 'Allspice', 'Nutmeg'
            },
            'Yellow': {
                'Turmeric', 'Saffron', 'Mustard Seeds', 'Curry Leaves'
            },
            'Green': {
                'Basil', 'Oregano', 'Thyme', 'Sage', 'Kaffir Lime Leaves'
            },
            'Orange': {
                'Paprika', 'Annatto Seeds', 'Cayenne Pepper'
            },
            'White': {
                'Garlic Powder', 'Onion Powder', 'Asafoetida', 'White Pepper'
            },
            'Black': {
                'Black Pepper', 'Nigella Seeds', 'Fennel Seeds'
            },
            'Other': set()  # For colors that don't fit above categories
        }
    },
    'Texture Analysis': {
        'type': 'str',
        'states': {
            'Powdery': {
                'Garlic Powder', 'Onion Powder', 'Black Pepper',
                'Cumin', 'Coriander Seeds', 'Turmeric', 'Paprika'
            },
            'Coarse': {
                'Mustard Seeds', 'Fennel Seeds', 'Nigella Seeds',
                'Anise Seeds', 'Fenugreek', 'Ajwain Seeds'
            },
            'Smooth': {
                'Vanilla Bean', 'Licorice Root', 'Gumbo File'
            },
            'Grainy': {
                'Sumac', 'Asafoetida', 'Szechuan Peppercorns'
            },
            'Oily': set(),  # If any truths have oily texture
            'Other': set()  # For textures that don't fit above categories
        }
    },
    'Moisture Content Testing': {
        'type': 'str',
        'states': {
            'Low Moisture': {
                'Dried Chiles', 'Mustard Seeds', 'Nigella Seeds',
                'Fennel Seeds', 'Anise Seeds', 'Fenugreek'
            },
            'Medium Moisture': {
                'Turmeric', 'Cinnamon', 'Cloves', 'Allspice',
                'Cumin', 'Paprika', 'Black Pepper'
            },
            'High Moisture': {
                'Vanilla Bean', 'Licorice Root', 'Gumbo File',
                'Asafoetida', 'White Pepper', 'Garlic Powder'
            }
        }
    },
    'Chemical Composition Analysis': {
        'type': 'dict',
        'states': {
            'Essential Oils Content': {
                'Basil', 'Oregano', 'Thyme', 'Sage', 'Rosemary'
            },
            'Alkaloids Presence': {
                'Black Pepper', 'Cayenne Pepper', 'Mustard Seeds',
                'Wasabi', 'Szechuan Peppercorns'
            },
            'Phenolic Compounds': {
                'Cinnamon', 'Cloves', 'Allspice', 'Nutmeg'
            },
            'Flavonoids': {
                'Sumac', 'Fenugreek', 'Dill Seeds'
            },
            'Other': set()  # For chemical properties not covered above
        }
    },
    'Flavor Profiling': {
        'type': 'str',
        'states': {
            'Sweet': {
                'Vanilla Bean', 'Licorice Root', 'Allspice', 'Nutmeg'
            },
            'Salty': set(),  # Assuming no salty truths
            'Sour': {
                'Sumac', 'Kaffir Lime Leaves', 'Curry Leaves'
            },
            'Bitter': {
                'Fenugreek', 'Mustard Seeds', 'Asafoetida'
            },
            'Umami': {
                'Mace', 'Cardamom', 'Cinnamon', 'Anise Seeds',
                'Fennel Seeds', 'Allspice', 'Star Anise',
                'Szechuan Peppercorns', 'Saffron', 'Nutmeg', 'Cloves'
            }
        }
    }
}