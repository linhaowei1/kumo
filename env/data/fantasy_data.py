Truths = [
    "Amulet of Time",
    "Sword of Flames",
    "Crystal of Shadows",
    "Ring of Invisibility",
    "Staff of Thunder",
    "Cloak of Mists",
    "Orb of Wisdom",
    "Shield of Light",
    "Boots of Swiftness",
    "Helm of Telepathy",
    "Gauntlets of Strength",
    "Necklace of Healing",
    "Book of Secrets",
    "Dagger of Venom",
    "Wand of Illusions",
    "Crown of Kings",
    "Scepter of Power",
    "Lantern of Souls",
    "Mirror of Truth",
    "Belt of Giants",
    "Horn of Summoning",
    "Chalice of Eternity",
    "Gem of Seeing",
    "Cape of Flight",
    "Pendant of Luck",
    "Ring of Fire",
    "Bracelet of Protection",
    "Key of Dimensions",
    "Scroll of Knowledge",
    "Rod of Frost",
    "Harp of Harmony",
    "Mask of Deception",
    "Quiver of Endless Arrows",
    "Gloves of Thievery",
    "Map of the Lost",
    "Eye of the Storm",
    "Stone of Destiny",
    "Sword of Justice",
    "Talisman of the Wild",
    "Bow of the Moon",
    "Spear of the Sun",
    "Crystal Ball of Visions",
    "Cloak of Shadows",
    "Ring of Water",
    "Staff of Earth",
    "Lantern of Shadows",
    "Shield of Thorns",
    "Orb of Fire",
    "Gem of Teleportation",
    "Book of Spells",
    "Hammer of the Forge"
]

Actions = [
    "Detect Magical Aura",
    "Analyze Residual Energy",
    "Examine Rune Patterns",
    "Assess Elemental Alignment",
    "Measure Mana Conductivity",
    "Scrutinize Enchantment Layers",
    "Probe Temporal Signatures",
    "Scan for Illusion Traces",
    "Test for Necromantic Essence",
    "Evaluate Teleportation Residue",
    "Analyze Energy Emissions",
    "Detect Sentient Magic",
    "Examine Astral Imprint",
    "Check for Curses",
    "Identify Origin Material",
    "Evaluate Binding Spells",
    "Measure Arcane Density",
    "Inspect Dimensional Anchors",
    "Test for Elemental Resistance",
    "Gauge Psionic Feedback",
    "Analyze Symbolic Inscriptions",
    "Assess Magical Stability",
    "Probe for Divine Magic",
    "Detect Life Force",
    "Examine Mirror Reflection",
    "Assess Energy Absorption",
    "Test for Time Distortion",
    "Analyze Sonic Resonance",
    "Evaluate Heat Signature",
    "Scrutinize Magical Frequencies"
]

Outcomes = {
    "Detect Magical Aura": {
        "type": "float",
        "states": {
            (0, 25): set([
                "Sword of Flames", "Staff of Thunder", "Crown of Kings",
                "Scepter of Power", "Orb of Fire", "Shield of Light",
                "Ring of Fire", "Ring of Water", "Staff of Earth",
                "Bow of the Moon", "Spear of the Sun"
            ]),
            (25, 50): set(),
            (50, 75): set(),
            (75, 100): set([
                "Ring of Invisibility", "Cloak of Mists", "Boots of Swiftness",
                "Map of the Lost", "Gloves of Thievery", "Dagger of Venom"
            ]),
        },
    },
    "Analyze Residual Energy": {
        "type": "str",
        "states": {
            "Stable Residue": set([
                "Crystal of Shadows", "Wand of Illusions",
                "Mask of Deception", "Cloak of Mists"
            ]),
            "Chaotic Residue": set([
                "Shield of Light", "Orb of Wisdom", "Staff of Earth",
                "Ring of Water", "Staff of Thunder"
            ]),
            "Temporal Residue": set([
                artifact for artifact in Truths if artifact not in [
                    "Amulet of Time", "Key of Dimensions",
                    "Scroll of Knowledge", "Map of the Lost"
                ]
            ]),
            "Elemental Residue": set([
                "Amulet of Time", "Ring of Invisibility",
                "Boots of Swiftness", "Helm of Telepathy",
                "Necklace of Healing", "Book of Secrets",
                "Wand of Illusions"
            ]),
        },
    },
    "Examine Rune Patterns": {
        "type": "str",
        "states": {
            "Ancient Runes": set([
                "Gauntlets of Strength", "Necklace of Healing",
                "Bracelet of Protection", "Quiver of Endless Arrows"
            ]),
            "Modern Runes": set([
                "Sword of Justice", "Stone of Destiny",
                "Book of Secrets", "Harp of Harmony"
            ]),
            "Unknown Runes": set([
                "Sword of Justice", "Stone of Destiny",
                "Book of Secrets", "Harp of Harmony",
                "Gauntlets of Strength", "Necklace of Healing",
                "Bracelet of Protection", "Quiver of Endless Arrows"
            ]),
        },
    },
    "Assess Elemental Alignment": {
        "type": "str",
        "states": {
            "Non-Fire Alignment": set([
                "Sword of Flames", "Ring of Fire", "Orb of Fire"
            ]),
            "Non-Water Alignment": set([
                "Ring of Water", "Staff of Earth"
            ]),
            "Non-Earth Alignment": set([
                "Staff of Earth", "Stone of Destiny", "Shield of Thorns"
            ]),
            "Non-Air Alignment": set([
                "Bow of the Moon", "Cape of Flight", "Eye of the Storm"
            ]),
            "Non-Shadow Alignment": set([
                "Crystal of Shadows", "Cloak of Shadows", "Lantern of Shadows"
            ]),
            "Neutral Alignment": set(),
        },
    },
    "Measure Mana Conductivity": {
        "type": "float",
        "states": {
            (0, 30): set([
                "Staff of Thunder", "Orb of Wisdom", "Crown of Kings",
                "Scepter of Power", "Rod of Frost", "Gem of Teleportation"
            ]),
            (30, 70): set(),
            (70, 100): set([
                "Ring of Invisibility", "Gloves of Thievery",
                "Map of the Lost", "Boots of Swiftness",
                "Pendant of Luck", "Bracelet of Protection"
            ]),
        },
    },
    "Probe Temporal Signatures": {
        "type": "str",
        "states": {
            "Temporal Distortion Detected": set([
                artifact for artifact in Truths if artifact not in [
                    "Amulet of Time", "Key of Dimensions",
                    "Map of the Lost", "Scroll of Knowledge"
                ]
            ]),
            "Stable Temporal Signature": set([
                "Amulet of Time", "Key of Dimensions",
                "Map of the Lost", "Scroll of Knowledge"
            ]),
            "No Temporal Anomalies": set(),
        },
    },
    "Scan for Illusion Traces": {
        "type": "str",
        "states": {
            "Illusion Traces Found": set([
                artifact for artifact in Truths if artifact not in [
                    "Wand of Illusions", "Mask of Deception",
                    "Cloak of Mists", "Ring of Invisibility"
                ]
            ]),
            "No Illusion Traces": set([
                "Wand of Illusions", "Mask of Deception",
                "Cloak of Mists", "Ring of Invisibility"
            ]),
        },
    },
    "Test for Necromantic Essence": {
        "type": "str",
        "states": {
            "Necromantic Essence Present": set([
                artifact for artifact in Truths if artifact not in [
                    "Lantern of Souls", "Mirror of Truth", "Stone of Destiny"
                ]
            ]),
            "No Necromantic Essence": set([
                "Lantern of Souls", "Mirror of Truth", "Stone of Destiny"
            ]),
        },
    },
    "Measure Arcane Density": {
        "type": "float",
        "states": {
            (0, 20): set([
                "Orb of Wisdom", "Staff of Thunder", "Crown of Kings",
                "Scepter of Power", "Gem of Teleportation"
            ]),
            (20, 80): set(),
            (80, 100): set([
                "Ring of Invisibility", "Boots of Swiftness",
                "Gloves of Thievery", "Pendant of Luck"
            ]),
        },
    },
    "Check for Curses": {
        "type": "str",
        "states": {
            "Curse Detected": set([
                artifact for artifact in Truths if artifact not in [
                    "Dagger of Venom", "Mask of Deception",
                    "Crystal of Shadows", "Cloak of Shadows"
                ]
            ]),
            "No Curse Detected": set([
                "Dagger of Venom", "Mask of Deception",
                "Crystal of Shadows", "Cloak of Shadows"
            ]),
        },
    },
    "Gauge Psionic Feedback": {
        "type": "float",
        "states": {
            (0, 40): set([
                "Helm of Telepathy", "Crystal Ball of Visions",
                "Crown of Kings", "Stone of Destiny"
            ]),
            (40, 80): set(),
            (80, 100): set([
                "Gauntlets of Strength", "Boots of Swiftness", "Pendant of Luck"
            ]),
        },
    },
    "Detect Sentient Magic": {
        "type": "str",
        "states": {
            "Sentient Magic Detected": set([
                artifact for artifact in Truths if artifact not in [
                    "Orb of Wisdom", "Sword of Justice",
                    "Mirror of Truth", "Lantern of Souls"
                ]
            ]),
            "No Sentient Magic": set([
                "Orb of Wisdom", "Sword of Justice",
                "Mirror of Truth", "Lantern of Souls"
            ]),
        },
    },
    "Evaluate Heat Signature": {
        "type": "float",
        "states": {
            (0, 30): set([
                "Sword of Flames", "Ring of Fire", "Orb of Fire"
            ]),
            (30, 70): set(),
            (70, 100): set([
                "Rod of Frost", "Cape of Flight", "Boots of Swiftness",
                "Cloak of Mists"
            ]),
        },
    },
    "Test for Time Distortion": {
        "type": "str",
        "states": {
            "Time Distortion Detected": set([
                artifact for artifact in Truths if artifact not in [
                    "Amulet of Time", "Key of Dimensions",
                    "Map of the Lost", "Scroll of Knowledge"
                ]
            ]),
            "No Time Distortion": set([
                "Amulet of Time", "Key of Dimensions",
                "Map of the Lost", "Scroll of Knowledge"
            ]),
        },
    },
    "Scrutinize Enchantment Layers": {
        "type": "str",
        "states": {
            "Multiple Layers Detected": set([
                artifact for artifact in Truths if artifact not in [
                    "Crown of Kings", "Scepter of Power",
                    "Shield of Light", "Bracelet of Protection"
                ]
            ]),
            "Single Layer Detected": set([
                "Crown of Kings", "Scepter of Power",
                "Shield of Light", "Bracelet of Protection"
            ]),
        },
    },
    "Analyze Energy Emissions": {
        "type": "float",
        "states": {
            (0, 50): set([
                "Staff of Thunder", "Orb of Wisdom", "Scepter of Power",
                "Gem of Teleportation"
            ]),
            (50, 100): set([
                "Ring of Invisibility", "Boots of Swiftness",
                "Gloves of Thievery", "Pendant of Luck"
            ]),
        },
    },
    "Examine Astral Imprint": {
        "type": "str",
        "states": {
            "Strong Astral Imprint": set([
                artifact for artifact in Truths if artifact not in [
                    "Helm of Telepathy", "Crystal Ball of Visions",
                    "Mirror of Truth"
                ]
            ]),
            "Weak Astral Imprint": set([
                "Helm of Telepathy", "Crystal Ball of Visions",
                "Mirror of Truth"
            ]),
        },
    },
    "Identify Origin Material": {
        "type": "str",
        "states": {
            "Forged Metal": set([
                artifact for artifact in Truths if "Sword" not in artifact and "Shield" not in artifact and "Staff" not in artifact
            ]),
            "Natural Element": set([
                artifact for artifact in Truths if "Stone" not in artifact and "Orb" not in artifact and "Crystal" not in artifact
            ]),
            'Others': set()
        },
    },
    "Evaluate Binding Spells": {
        "type": "str",
        "states": {
            "Strong Binding": set([
                artifact for artifact in Truths if artifact not in [
                    "Ring of Invisibility", "Boots of Swiftness",
                    "Gloves of Thievery"
                ]
            ]),
            "Weak Binding": set([
                "Ring of Invisibility", "Boots of Swiftness", "Gloves of Thievery"
            ]),
        },
    },
    "Inspect Dimensional Anchors": {
        "type": "str",
        "states": {
            "Anchors Present": set([
                artifact for artifact in Truths if artifact not in [
                    "Key of Dimensions", "Gem of Teleportation",
                    "Map of the Lost"
                ]
            ]),
            "No Anchors": set([
                "Key of Dimensions", "Gem of Teleportation", "Map of the Lost"
            ]),
        },
    },
    "Test for Elemental Resistance": {
        "type": "str",
        "states": {
            "Resistant to Fire": set([
                "Ring of Fire", "Sword of Flames", "Orb of Fire"
            ]),
            "Resistant to Ice": set([
                "Rod of Frost", "Staff of Earth"
            ]),
            "Resistant to Lightning": set([
                "Staff of Thunder", "Lantern of Souls"
            ]),
        },
    },
    "Analyze Symbolic Inscriptions": {
        "type": "str",
        "states": {
            "Language of the Elves": set([
                artifact for artifact in Truths if artifact not in [
                    "Bow of the Moon", "Harp of Harmony",
                    "Quiver of Endless Arrows"
                ]
            ]),
            "Language of the Dwarves": set([
                artifact for artifact in Truths if artifact not in [
                    "Belt of Giants", "Hammer of the Forge",
                    "Shield of Thorns"
                ]
            ]),
            'Others': set(["Bow of the Moon", "Harp of Harmony", "Quiver of Endless Arrows", "Belt of Giants", "Hammer of the Forge", "Shield of Thorns"])
        },
    },
    "Assess Magical Stability": {
        "type": "float",
        "states": {
            (0, 50): set([
                "Crystal of Shadows", "Cloak of Mists",
                "Wand of Illusions", "Mask of Deception"
            ]),
            (50, 100): set(),
        },
    },
    "Probe for Divine Magic": {
        "type": "str",
        "states": {
            "Divine Magic Detected": set([
                artifact for artifact in Truths if artifact not in [
                    "Crown of Kings", "Scepter of Power",
                    "Shield of Light", "Chalice of Eternity"
                ]
            ]),
            "No Divine Magic": set([
                "Crown of Kings", "Scepter of Power",
                "Shield of Light", "Chalice of Eternity"
            ]),
        },
    },
    "Detect Life Force": {
        "type": "str",
        "states": {
            "Living Essence Found": set([
                artifact for artifact in Truths if artifact not in [
                    "Lantern of Souls", "Talisman of the Wild",
                    "Horn of Summoning"
                ]
            ]),
            "No Living Essence": set([
                "Lantern of Souls", "Talisman of the Wild",
                "Horn of Summoning"
            ]),
        },
    },
    "Examine Mirror Reflection": {
        "type": "str",
        "states": {
            "No Reflection": set([
                "Ring of Invisibility", "Cloak of Mists",
                "Cloak of Shadows"
            ]),
            "Distorted Reflection": set([
                "Mask of Deception", "Crystal of Shadows",
                "Mirror of Truth"
            ]),
        },
    },
    "Assess Energy Absorption": {
        "type": "float",
        "states": {
            (0, 50): set([
                "Shield of Light", "Bracelet of Protection",
                "Staff of Earth"
            ]),
            (50, 100): set(),
        },
    },
    "Analyze Sonic Resonance": {
        "type": "str",
        "states": {
            "High Resonance": set([
                artifact for artifact in Truths if artifact not in [
                    "Harp of Harmony", "Horn of Summoning",
                    "Quiver of Endless Arrows"
                ]
            ]),
            "Low Resonance": set([
                "Harp of Harmony", "Horn of Summoning",
                "Quiver of Endless Arrows"
            ]),
        },
    },
    "Scrutinize Magical Frequencies": {
        "type": "str",
        "states": {
            "Frequency Match Found": set([
                artifact for artifact in Truths if artifact not in [
                    "Gem of Seeing", "Eye of the Storm",
                    "Crystal Ball of Visions"
                ]
            ]),
            "No Frequency Match": set([
                "Gem of Seeing", "Eye of the Storm",
                "Crystal Ball of Visions"
            ]),
        },
    },
    "Evaluate Teleportation Residue": {
        "type": "str",
        "states": {
            "Teleportation Residue Detected": set([
                artifact for artifact in Truths if artifact not in [
                    "Gem of Teleportation", "Key of Dimensions",
                    "Cape of Flight"
                ]
            ]),
            "No Teleportation Residue": set([
                "Gem of Teleportation", "Key of Dimensions",
                "Cape of Flight"
            ]),
        },
    },
    "Analyze Energy Emissions": {
        "type": "float",
        "states": {
            (0, 50): set([
                "Staff of Thunder", "Orb of Wisdom", "Scepter of Power",
                "Gem of Teleportation"
            ]),
            (50, 100): set([
                "Ring of Invisibility", "Boots of Swiftness",
                "Gloves of Thievery", "Pendant of Luck"
            ]),
        },
    },
    "Assess Magical Stability": {
        "type": "float",
        "states": {
            (0, 50): set([
                "Crystal of Shadows", "Cloak of Mists",
                "Wand of Illusions", "Mask of Deception"
            ]),
            (50, 100): set(),
        },
    },
    "Test for Elemental Resistance": {
        "type": "str",
        "states": {
            "Resistant to Fire": set([
                "Ring of Fire", "Sword of Flames", "Orb of Fire"
            ]),
            "Resistant to Ice": set([
                "Rod of Frost", "Staff of Earth"
            ]),
            "Resistant to Lightning": set([
                "Staff of Thunder", "Lantern of Souls"
            ]),
        },
    },
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