Truths = {'Ringwoodite', 'Hibonite', 'Daubréelite', 'Stishovite', 'Florenskyite', 'Majorite', 'Gupeiite', 'Cohenite', 'Osbornite', 'Schreibersite', 'Troilite', 'Oldhamite', 'Kamacite', 'Forsterite', 'Chromite', 'Panguite', 'Moissanite', 'Olivine', 'Wadsleyite', 'Pyroxene', 'Ferrosilite', 'Taenite', 'Enstatite', 'Tranquillityite', 'Sylvite', 'Lawrencite', 'Suessite', 'Allendeite', 'Murakamiite'}
Actions = {'Isotopic ratio mass spectrometry', 'X-ray diffraction analysis', 'Electron Microprobe Analysis', 'Scanning Electron Microscopy (SEM)', 'Raman Spectroscopy', 'Transmission Electron Microscopy (TEM)', 'Fourier-Transform Infrared Spectroscopy (FTIR)', 'Thermogravimetric Analysis (TGA)'}

Outcomes = {'X-ray diffraction analysis': {'type': 'str', 'states': {'Cubic crystal structure': {'Ferrosilite', 'Enstatite', 'Ringwoodite', 'Forsterite', 'Stishovite', 'Majorite', 'Olivine', 'Wadsleyite', 'Pyroxene'}, 'Hexagonal crystal structure': {'Taenite', 'Schreibersite', 'Cohenite', 'Chromite', 'Lawrencite', 'Troilite', 'Kamacite'}, 'Orthorhombic crystal structure': {'Sylvite', 'Daubréelite', 'Gupeiite', 'Oldhamite', 'Moissanite', 'Murakamiite', 'Osbornite'}, 'Monoclinic crystal structure': {'Tranquillityite', 'Hibonite', 'Florenskyite', 'Panguite', 'Suessite', 'Allendeite'}}}, 'Isotopic ratio mass spectrometry': {'type': 'float', 'states': {(0.0, 0.01): {'Enstatite', 'Forsterite', 'Stishovite', 'Majorite', 'Olivine', 'Pyroxene'}, (0.01, 0.1): {'Taenite', 'Chromite', 'Lawrencite', 'Troilite', 'Kamacite', 'Osbornite'}, (0.1, 1.0): {'Sylvite', 'Daubréelite', 'Gupeiite', 'Oldhamite', 'Murakamiite'}, (1.0, 10.0): {'Tranquillityite', 'Hibonite', 'Florenskyite', 'Panguite', 'Allendeite'}}},'Electron Microprobe Analysis': {
        'type': 'str',
        'states': {
            'Elemental Composition': {'Gupeiite', 'Murakamiite', 'Florenskyite', 'Panguite', 'Taenite', 'Moissanite', 'Schreibersite', 'Allendeite'},
            'Chemical Bonding': {'Forsterite', 'Stishovite', 'Enstatite', 'Wadsleyite', 'Olivine', 'Pyroxene', 'Ferrosilite', 'Tranquillityite', 'Sylvite', 'Kamacite', 'Cohenite', 'Osbornite'},
            'Mineral Identification': {'Hibonite', 'Majorite', 'Oldhamite', 'Troilite', 'Daubréelite', 'Lawrencite', 'Chromite'},
            'Surface Structure': {'Panguite', 'Schreibersite', 'Allendeite', 'Murakamiite', 'Florenskyite'}
        }
    },
    'Scanning Electron Microscopy (SEM)': {
        'type': 'str',
        'states': {
            'Surface Morphology': {'Gupeiite', 'Panguite', 'Moissanite', 'Allendeite'},
            'Crystallographic Texture': {'Stishovite', 'Wadsleyite', 'Majorite', 'Kamacite', 'Osbornite'},
            'Electron Interaction': {'Sylvite', 'Murakamiite', 'Troilite', 'Daubréelite'},
            'Topography and Surface Composition': {'Hibonite', 'Tranquillityite', 'Florenskyite', 'Cohenite', 'Taenite', 'Oldhamite'}
        }
    },
    'Raman Spectroscopy': {
        'type': 'str',
        'states': {
            'Vibrational Modes': {'Murakamiite', 'Tranquillityite', 'Moissanite', 'Sylvite'},
            'Crystal Symmetry and Defects': {'Cohenite', 'Kamacite', 'Schreibersite', 'Panguite'},
            'Spectral Characteristics': {'Hibonite', 'Florenskyite', 'Taenite', 'Chromite'},
            'Phonon Peaks': {'Daubréelite', 'Osbornite', 'Troilite', 'Oldhamite'}
        }
    },
    'Transmission Electron Microscopy (TEM)': {
        'type': 'str',
        'states': {
            'Atomic Resolution Imaging': {'Kamacite', 'Schreibersite', 'Moissanite', 'Taenite'},
            'Electron Diffraction Patterns': {'Murakamiite', 'Allendeite', 'Sylvite', 'Gupeiite'},
            'Nanostructure Characterization': {'Majorite', 'Olivine', 'Pyroxene', 'Stishovite'},
            'Crystal Defects': {'Ferrosilite', 'Enstatite', 'Wadsleyite', 'Forsterite'}
        }
    },
    'Fourier-Transform Infrared Spectroscopy (FTIR)': {
        'type': 'str',
        'states': {
            'Functional Group Identification': {'Murakamiite', 'Panguite', 'Moissanite', 'Allendeite'},
            'Absorption Peaks': {'Sylvite', 'Daubréelite', 'Kamacite', 'Cohenite'},
            'Bonding Types': {'Taenite', 'Schreibersite', 'Lawrencite', 'Oldhamite'},
            'Phase Transitions': {'Tranquillityite', 'Hibonite', 'Florenskyite', 'Osbornite'}
        }
    },
    'Thermogravimetric Analysis (TGA)': {
        'type': 'str',
        'states': {
            'Thermal Stability': {'Moissanite', 'Panguite', 'Schreibersite', 'Murakamiite'},
            'Mass Loss Behavior': {'Sylvite', 'Kamacite', 'Troilite', 'Oldhamite'},
            'Phase Transition Temperature': {'Enstatite', 'Forsterite', 'Stishovite', 'Pyroxene'},
            'Decomposition Kinetics': {'Tranquillityite', 'Hibonite', 'Allendeite', 'Chromite'}
        }
    }
}
