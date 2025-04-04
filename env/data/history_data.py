Truths = {'Mesolithic Era', 'Ancient Indus Valley', 'Harappan Civilization', 'Roman Empire', 'Great Depression', 'Age of Imperialism', 'Gilded Age', 'Ancient Egypt', 'Victorian Era', 'Classical Greece', 'Iron Age', 'Industrial Revolution', 'World War II', 'World War I', 'Sumerian Civilization', 'Stone Age', 'Cold War', 'Korean War', 'Aztec Empire', 'Mayan Civilization', 'Paleolithic Era', 'Vietnam War', 'Neolithic Period', 'Inca Empire', 'Russian Revolution', 'Colonial India', 'Ancient Mesopotamia', 'Renaissance', 'Bronze Age', 'Space Race', 'Age of Exploration', 'The Fall of the Berlin Wall', 'Prohibition Era'}
Actions = {
        'Carbon Dating', 'Artifact Examination', 'Dendrochronology', 'Stratigraphy', 
        'Radiocarbon Analysis', 'Pottery Analysis', 'Molecular Archaeology', 'Geoarchaeology'
    }
Outcomes = outcomes = {
    'Carbon Dating': {
        'type': 'float',
        'states': {
            (0, 1500): {'Space Race', 'Industrial Revolution', 'World War II', 'The Fall of the Berlin Wall', 'Vietnam War', 'World War I', 'Russian Revolution', 'Colonial India', 'Great Depression', 'Cold War', 'Prohibition Era', 'Korean War', 'Gilded Age', 'Victorian Era'},
            (1500, 2000): {'Classical Greece', 'Iron Age', 'Ancient Mesopotamia', 'Paleolithic Era', 'Bronze Age', 'Mesolithic Era', 'Ancient Indus Valley', 'Mayan Civilization', 'Neolithic Period', 'Harappan Civilization', 'Inca Empire', 'Roman Empire', 'Sumerian Civilization', 'Stone Age', 'Aztec Empire', 'Ancient Egypt'}
        }
    },
    'Dendrochronology': {
        'type': 'float',
        'states': {
            (0, 1000): {'Space Race', 'Industrial Revolution', 'World War II', 'World War I', 'Cold War', 'Prohibition Era', 'Gilded Age', 'Victorian Era'},
            (1000, 2000): {'Classical Greece', 'Iron Age', 'Ancient Mesopotamia', 'Paleolithic Era', 'Bronze Age', 'Mesolithic Era', 'Ancient Indus Valley', 'Mayan Civilization', 'Neolithic Period', 'Harappan Civilization', 'Inca Empire', 'Roman Empire', 'Sumerian Civilization', 'Stone Age', 'Aztec Empire', 'Ancient Egypt'}
        }
    },
    'Stratigraphy': {
        'type': 'str',
        'states': {
            'Deep Layer': {'Space Race', 'Industrial Revolution', 'World War II', 'World War I', 'Cold War', 'Prohibition Era', 'Gilded Age', 'Victorian Era'},
            'Shallow Layer': {'Classical Greece', 'Iron Age', 'Paleolithic Era', 'Bronze Age', 'Mesolithic Era', 'Neolithic Period', 'Roman Empire', 'Stone Age', 'Ancient Egypt'}
        }
    },
    'Artifact Examination': {
        'type': 'str',
        'states': {
            'Stone Tools': {'Renaissance', 'Space Race', 'Industrial Revolution', 'World War II', 'Age of Exploration', 'World War I', 'Cold War', 'Prohibition Era', 'Age of Imperialism', 'Gilded Age', 'Victorian Era'},
            'Iron Weapons': {'Paleolithic Era', 'Bronze Age', 'Mesolithic Era', 'Neolithic Period', 'Stone Age'}
        }
    },
    'Molecular Archaeology': {
        'type': 'str',
        'states': {
            'Ancient DNA': {'Space Race', 'World War II', 'World War I', 'Cold War', 'Great Depression', 'Vietnam War', 'Korean War', 'Gilded Age', 'Victorian Era', 'Prohibition Era', 'Roman Empire', 'Ancient Mesopotamia', 'Ancient Indus Valley'},
            'Isotopic Analysis': {'Stone Age', 'Bronze Age', 'Paleolithic Era', 'Iron Age', 'Neolithic Period', 'Mesolithic Era', 'Sumerian Civilization', 'Aztec Empire', 'Mayan Civilization', 'Inca Empire', 'Harappan Civilization'}
        }
    },
    'Geoarchaeology': {
        'type': 'str',
        'states': {
            'Soil Analysis': {'Space Race', 'World War II', 'Industrial Revolution', 'Victorian Era', 'Age of Imperialism', 'Gilded Age', 'Colonial India', 'World War I', 'Cold War'},
            'Sediment Core': {'Stone Age', 'Bronze Age', 'Iron Age', 'Mesolithic Era', 'Paleolithic Era', 'Neolithic Period', 'Sumerian Civilization', 'Roman Empire', 'Ancient Egypt', 'Classical Greece'}
        }
    }
}