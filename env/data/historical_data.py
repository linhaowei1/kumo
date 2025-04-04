Truths = {'Battle of Hastings', 'Battle of Manzikert', 'Battle of Thermopylae', 'Battle of Marathon', 'Battle of Adrianople', 'Battle of Agincourt'}
Actions = {'Inscription Translation', 'Carbon Dating', 'Weapon Material Analysis', 'Artifact Excavation', 'Historical Record Analysis', 'Topographical Survey', 'Battle Tactics Study', 'Climate Analysis'}
Outcomes = outcomes = {
    'Carbon Dating': {
        'type': 'float',
        'states': {
            (-500, 500): {'Battle of Manzikert', 'Battle of Hastings', 'Battle of Adrianople'},
            (500, 1000): {'Battle of Thermopylae', 'Battle of Marathon'},
            (1000, 1500): {'Battle of Thermopylae', 'Battle of Marathon'},
            (1500, 2000): {'Battle of Thermopylae', 'Battle of Marathon'},
        }
    },
    'Weapon Material Analysis': {
        'type': 'str',
        'states': {
            'Bronze': {'Battle of Hastings', 'Battle of Agincourt'},
            'Iron': {'Battle of Thermopylae', 'Battle of Marathon'},
            'Steel': {'Battle of Thermopylae', 'Battle of Marathon'},
            'Gunpowder-based': {'Battle of Hastings', 'Battle of Thermopylae', 'Battle of Marathon'},
            'Modern Alloys': {'Battle of Thermopylae', 'Battle of Marathon'},
            'Unknown': set()  # No exclusion for this action
        }
    },
    'Inscription Translation': {
        'type': 'str',
        'states': {
            'Greek': {'Battle of Hastings', 'Battle of Agincourt'},
            'Latin': {'Battle of Thermopylae', 'Battle of Marathon'},
            'Old English': {'Battle of Thermopylae', 'Battle of Marathon'},
            'Japanese': {'Battle of Hastings', 'Battle of Agincourt'},
            'Arabic': {'Battle of Hastings', 'Battle of Agincourt'},
            'Unknown': set()  # No exclusion for this action
        }
    },
    'Artifact Excavation': {
        'type': 'str',
        'states': {
            'No Artifacts Found': {'Battle of Agincourt', 'Battle of Hastings'},
            'Significant Artifacts Found': {'Battle of Manzikert', 'Battle of Adrianople', 'Battle of Thermopylae', 'Battle of Marathon'},
            'Unknown': set()  # No exclusion for this action
        }
    },
    'Historical Record Analysis': {
        'type': 'str',
        'states': {
            'Minimal Documentation': {'Battle of Thermopylae', 'Battle of Marathon'},
            'Extensive Documentation': {'Battle of Hastings', 'Battle of Agincourt', 'Battle of Adrianople', 'Battle of Manzikert'},
            'Unknown': set()  # No exclusion for this action
        }
    },
    'Topographical Survey': {
        'type': 'str',
        'states': {
            'Altered Terrain': {'Battle of Agincourt', 'Battle of Manzikert'},
            'Unchanged Terrain': {'Battle of Hastings', 'Battle of Thermopylae', 'Battle of Marathon', 'Battle of Adrianople'},
            'Unknown': set()  # No exclusion for this action
        }
    },
    'Battle Tactics Study': {
        'type': 'str',
        'states': {
            'Simple Tactics': {'Battle of Agincourt', 'Battle of Adrianople'},
            'Complex Tactics': {'Battle of Hastings', 'Battle of Manzikert', 'Battle of Thermopylae', 'Battle of Marathon'},
            'Unknown': set()  # No exclusion for this action
        }
    },
    'Climate Analysis': {
        'type': 'str',
        'states': {
            'No Relevant Climate Data': {'Battle of Agincourt', 'Battle of Hastings'},
            'Relevant Climate Data': {'Battle of Manzikert', 'Battle of Adrianople', 'Battle of Thermopylae', 'Battle of Marathon'},
            'Unknown': set()  # No exclusion for this action
        }
    }
}