Truths = [
    'Soul', 'K-pop', 'Grunge', 'Baroque', 'World', 'Funk', 'J-pop', 'Experimental', 'Hip Hop', 
    'Indie', 'Reggae', 'Punk', 'Pop', 'Reggaeton', 'Industrial', 'Rap', 'Waltz', 'Bossa Nova', 
    'Electronic', 'Country', 'Avant-Garde', 'Latin', 'Drum and Bass', 'Blues', 'Opera', 'Swing', 
    'Classical', 'New Age', 'Ska', 'EDM', 'Dubstep', 'Ambient', 'Progressive Rock', 'Trance', 
    'Rock', 'Metal', 'Medieval', 'House', 'Psychedelic', 'Gospel', 'Techno', 'Dancehall', 'Jazz', 
    'R&B', 'Folk'
]

Actions = [
    "Analyze Tempo", "Examine Instrumentation", "Assess Lyrical Content", "Evaluate Vocal Style",
    "Determine Time Signature", "Analyze Harmonic Complexity", "Examine Song Structure", "Assess Cultural Influences",
    "Evaluate Production Techniques", "Examine Rhythm Patterns", "Analyze Use of Electronic Elements",
    "Assess Emotional Tone", "Evaluate Vocal Range", "Examine Language Used", "Analyze Use of Improvisation",
    "Assess Danceability", "Evaluate Historical Context", "Examine Use of Sampling", "Analyze Melody Line",
    "Assess Repetition", "Evaluate Dynamics", "Examine Key Signature", "Analyze Instrument Solos",
    "Assess Live Performance Elements", "Evaluate Use of Synthesizers", "Examine Background Vocals",
    "Analyze Acoustic vs. Electric Instruments", "Assess Use of Percussion", "Evaluate Genre Fusion Elements",
    "Examine Song Length", "Analyze Lyrics Theme", "Assess Orchestration", "Evaluate Vocal Harmonies",
    "Examine Use of Traditional Instruments", "Analyze Beat Patterns", "Assess Use of Auto-Tune",
    "Examine Audience Participation Elements", "Analyze Thematic Consistency", "Assess Album Concept"
]

Outcomes = {
    # Each outcome state rules out certain genres from being the correct one.
    # For example, if we find the tempo in a certain range, we eliminate genres not fitting that profile.
    "Analyze Tempo": {
        "type": "float",
        "states": {
            # If tempo is very slow (0-60 BPM), we rule out genres typically known for faster tempos or energetic rhythms.
            (0, 60): {"Punk", "Metal", "Drum and Bass", "EDM", "Trance", "Techno", "House", "Ska",
                      "Grunge", "Dancehall", "Dubstep", "Electronic", "Hip Hop"},
            # If tempo is slow-to-moderate (61-90 BPM), we still rule out similar genres known to favor faster tempos.
            (61, 90): {"Punk", "Drum and Bass", "EDM", "Trance", "Techno", "House", "Ska",
                       "Grunge", "Dancehall", "Dubstep"},
            # If tempo is moderate (91-120 BPM), we don't rule out any specific genres here, 
            # perhaps indicating this tempo is very common and doesn't exclude anything by itself.
            (91, 120): set(),
            # If tempo is faster (121-180 BPM), we rule out genres known for slower, more relaxed tempos.
            (121, 180): {"Classical", "Opera", "Ambient", "New Age", "Blues", "Soul", "Gospel",
                         "Bossa Nova", "Swing", "Baroque", "Medieval"},
            # If tempo is very fast (181-300 BPM), we also rule out traditionally slower genres.
            (181, 300): {"Classical", "Opera", "Ambient", "New Age", "Blues", "Soul", "Gospel",
                         "Bossa Nova", "Swing", "Baroque", "Medieval", "Folk", "Reggae"}
        }
    },

    # Instrumentation clues can exclude genres that rely on different instrument palettes.
    "Examine Instrumentation": {
        "type": "str",
        "states": {
            # Heavy Electric Guitar instrumentation rules out genres that rarely feature it prominently.
            "Heavy Electric Guitar": {"Classical", "Jazz", "Opera", "Ambient", "Hip Hop", "Reggae",
                                      "Bossa Nova", "New Age", "Folk"},
            # Acoustic Instruments detected excludes genres heavily associated with electronic instrumentation.
            "Acoustic Instruments": {"Electronic", "Hip Hop", "Techno", "House", "Trance", "Dubstep",
                                     "EDM", "Industrial"},
            # Synthesizers detected rules out genres known for more traditional acoustic lineups.
            "Synthesizers": {"Classical", "Folk", "Country", "Blues", "Jazz", "Opera", "Gospel",
                             "Bossa Nova", "Swing", "Baroque", "Medieval"},
            # Brass and Woodwind focus excludes genres known for electronic or heavy guitar-based music.
            "Brass and Woodwind": {"Electronic", "Hip Hop", "EDM", "Techno", "House", "Trance",
                                   "Dubstep", "Metal"}
        }
    },

    # Lyrical content clues exclude genres that don't align with the observed theme or approach.
    "Assess Lyrical Content": {
        "type": "str",
        "states": {
            # Instrumental-only content observed means we exclude genres known for prominent lyrics.
            "Instrumental": {"Hip Hop", "Rap", "Pop", "R&B", "Reggae", "Country", "K-pop", "J-pop",
                             "Gospel", "Soul", "Dancehall"},
            # Abstract Lyrics observed rules out genres known for more straightforward lyrical themes.
            "Abstract Lyrics": {"Country", "Blues", "Folk", "Pop", "R&B"},
            # Political Themes detected excludes genres that typically avoid political commentary.
            "Political Themes": {"Ambient", "New Age", "Classical", "EDM", "Trance", "Techno",
                                 "House", "Opera"},
            # Love and Relationships theme excludes more experimental, esoteric genres.
            "Love and Relationships": {"Metal", "Industrial", "Dubstep", "Experimental",
                                       "Psychedelic", "Avant-Garde"}
        }
    },

    # Vocal style clues exclude genres that do not match the observed vocal approach.
    "Evaluate Vocal Style": {
        "type": "str",
        "states": {
            # Rapped Vocals observed rules out genres known for purely sung or instrumental vocal styles.
            "Rapped Vocals": {"Classical", "Opera", "Jazz", "Blues", "Folk", "Country", "Metal",
                              "EDM", "Trance", "Techno", "House"},
            # Operatic Vocals observed rules out genres that rarely feature operatic singing.
            "Operatic Vocals": {"Hip Hop", "Rap", "Country", "R&B", "Reggae", "EDM", "Techno",
                                "House", "Trance", "Dubstep", "Punk", "Metal", "Grunge"},
            # Screamed Vocals observed excludes genres not associated with harsh or screamed vocals.
            "Screamed Vocals": {"Classical", "Jazz", "Opera", "Ambient", "New Age", "Blues", "Soul",
                                "Gospel", "Bossa Nova", "Swing", "Baroque", "Medieval", "Folk",
                                "Country"},
            # Melodic Singing observed is very common, so it might not rule out anything specifically.
            "Melodic Singing": set()
        }
    },

    # Time signatures can rule out genres commonly associated with other time signatures.
    "Determine Time Signature": {
        "type": "str",
        "states": {
            # 4/4 detected excludes genres known for other signatures.
            "4/4": {"Waltz", "Swing", "Bossa Nova"},
            # 3/4 detected excludes genres not typically found in triple meter.
            "3/4": {"Rock", "Hip Hop", "Rap", "Electronic", "Metal", "Reggae", "Punk"},
            # Complex Time Signatures exclude genres known for simpler rhythms.
            "Complex Time Signatures": {"Pop", "Country", "Blues", "R&B", "Gospel"}
        }
    },

    # Harmonic complexity clues exclude genres that don't fit the observed chordal density.
    "Analyze Harmonic Complexity": {
        "type": "float",
        "states": {
            # Very low complexity detected rules out harmonically complex genres.
            (0, 3): {"Jazz", "Classical", "Progressive Rock", "Experimental"},
            # Slightly more complexity rules out these sets.
            (4, 7): {"Ambient", "New Age", "Trance", "Techno", "House"},
            # Moderate complexity excludes these genres.
            (8, 12): {"Pop", "Country", "Folk", "Blues", "Reggae"},
            # Very high complexity excludes these.
            (13, 24): {"Hip Hop", "Rap", "EDM", "Dubstep", "Industrial"}
        }
    },

    # Song structure observations exclude genres not known for that structure.
    "Examine Song Structure": {
        "type": "str",
        "states": {
            # Verse-Chorus form found excludes genres that avoid this common structure.
            "Verse-Chorus": {"Classical", "Jazz", "Opera", "Ambient", "New Age"},
            # Through-Composed excludes these genres that rely on repetitive forms.
            "Through-Composed": {"Pop", "Rock", "Hip Hop", "Country", "Reggae"},
            # AABA form excludes genres known for loop-based structures.
            "AABA": {"Electronic", "Techno", "House", "Trance", "Dubstep", "Metal"}
        }
    },

    # Cultural influences might exclude genres not influenced by certain traditions.
    "Assess Cultural Influences": {
        "type": "str",
        "states": {
            "African": {"Classical", "Baroque", "Medieval", "Ambient", "New Age"},
            "Latin": {"Metal", "Grunge", "Punk", "Industrial", "EDM"},
            "Asian": {"Blues", "Country", "Gospel", "Soul", "R&B"}
        }
    },

    # Production techniques exclude genres that don't match the observed production style.
    "Evaluate Production Techniques": {
        "type": "str",
        "states": {
            "Lo-Fi": {"Classical", "Opera", "Jazz", "Blues", "Gospel", "Soul"},
            "High Production Value": {"Punk", "Grunge", "Indie"},
            "Live Recording": {"Electronic", "Techno", "House", "Trance", "Dubstep"}
        }
    },

    # Rhythm patterns exclude genres not known for these patterns.
    "Examine Rhythm Patterns": {
        "type": "str",
        "states": {
            "Syncopated": {"Classical", "Baroque", "Opera", "Ambient", "New Age"},
            "Straight Beat": {"Jazz", "Swing", "Bossa Nova", "Funk"},
            "Polyrhythms": {"Pop", "Country", "Folk", "Blues", "Reggae"}
        }
    },

    # Electronic element usage excludes genres that don't align with the observed electronic presence.
    "Analyze Use of Electronic Elements": {
        "type": "str",
        "states": {
            "Heavy Electronic": {"Classical", "Jazz", "Blues", "Folk", "Country", "Gospel"},
            "Minimal Electronic": {"EDM", "Trance", "Techno", "House", "Dubstep"},
            "No Electronic": {"Electronic", "Ambient", "New Age", "Industrial", "Experimental"}
        }
    },

    # Emotional tone observations exclude genres that don't typically match the observed mood.
    "Assess Emotional Tone": {
        "type": "str",
        "states": {
            "Happy": {"Metal", "Grunge", "Punk", "Blues"},
            "Melancholic": {"Pop", "Dancehall", "Reggae", "Hip Hop"},
            "Aggressive": {"Classical", "Opera", "Jazz", "Gospel", "Soul"}
        }
    },

    # Vocal range might exclude genres not known for the observed range.
    "Evaluate Vocal Range": {
        "type": "float",
        "states": {
            (0, 1): {"Opera", "Classical", "Jazz", "Gospel", "Soul"},
            (1, 2): {"Metal", "Punk", "Grunge", "Industrial"},
            (2, 3): {"Hip Hop", "Rap", "EDM", "Trance", "Techno", "House"},
            (3, 5): {"Pop", "Country", "Folk", "Blues", "R&B"}
        }
    },

    # Language used excludes genres known for different linguistic choices.
    "Examine Language Used": {
        "type": "str",
        "states": {
            "English": {"K-pop", "J-pop", "Latin", "World", "Reggaeton"},
            "Non-English": {"Country", "Blues", "Gospel", "Soul", "R&B"},
            "Instrumental": {"Hip Hop", "Rap", "Pop", "EDM", "Trance"}
        }
    },

    # Improvisation level excludes genres that don't match the observed improvisational tendencies.
    "Analyze Use of Improvisation": {
        "type": "str",
        "states": {
            "High Improvisation": {"Pop", "EDM", "Trance", "Techno", "House"},
            "Some Improvisation": {"Classical", "Opera", "Ambient", "New Age"},
            "No Improvisation": {"Jazz", "Blues", "Rock", "Metal", "Funk"}
        }
    },

    # Danceability excludes genres that don't fit the observed danceability level.
    "Assess Danceability": {
        "type": "float",
        "states": {
            (0, 3): {"Classical", "Opera", "Ambient", "New Age", "Experimental"},
            (4, 6): {"Rock", "Metal", "Grunge", "Punk", "Industrial"},
            (7, 10): {"Pop", "Hip Hop", "EDM", "Trance", "House", "Reggaeton", "Dancehall"}
        }
    },

    # Historical context excludes genres known for different historical roots.
    "Evaluate Historical Context": {
        "type": "str",
        "states": {
            "Modern": {"Baroque", "Medieval", "Classical", "Opera"},
            "Traditional": {"EDM", "Trance", "Techno", "House", "Dubstep"},
            "Mixed": {"Pop", "Rock", "Hip Hop", "Country", "Blues"}
        }
    },

    # Sampling usage excludes genres mismatched with the observed sampling approach.
    "Examine Use of Sampling": {
        "type": "str",
        "states": {
            "Heavy Sampling": {"Classical", "Jazz", "Blues", "Folk", "Country"},
            "No Sampling": {"Hip Hop", "Rap", "Electronic", "EDM", "House"}
        }
    },

    # Melody line complexity excludes genres not fitting the observed melodic style.
    "Analyze Melody Line": {
        "type": "str",
        "states": {
            "Complex Melody": {"Hip Hop", "Rap", "EDM", "Techno", "House"},
            "Simple Melody": {"Classical", "Opera", "Jazz", "Blues", "Folk"}
        }
    },

    # Repetition level excludes genres not aligning with the observed repetitive pattern.
    "Assess Repetition": {
        "type": "str",
        "states": {
            "Highly Repetitive": {"Classical", "Jazz", "Blues", "Folk", "Country"},
            "Moderate Repetition": {"Metal", "Grunge", "Punk", "Industrial"},
            "Low Repetition": {"EDM", "Trance", "Techno", "House", "Pop"}
        }
    },

    # Dynamics (volume variations) exclude genres not associated with the observed dynamic range.
    "Evaluate Dynamics": {
        "type": "str",
        "states": {
            "Wide Dynamics": {"EDM", "Trance", "Techno", "House", "Dubstep"},
            "Narrow Dynamics": {"Classical", "Opera", "Jazz", "Blues", "Folk"},
            "Moderate Dynamics": {"Pop", "Rock", "Hip Hop", "Country", "Reggae"}
        }
    },

    # Key signature excludes genres that don't match the observed key tendencies.
    "Examine Key Signature": {
        "type": "str",
        "states": {
            "Major Key": {"Metal", "Grunge", "Punk", "Industrial"},
            "Minor Key": {"Pop", "Hip Hop", "EDM", "Trance", "House"},
            "Modal Scales": {"Classical", "Jazz", "Blues", "Folk", "Country"}
        }
    },

    # Instrument solos detected exclude genres not known for such solo features.
    "Analyze Instrument Solos": {
        "type": "str",
        "states": {
            "Guitar Solo": {"Hip Hop", "Rap", "EDM", "Trance", "House"},
            "Saxophone Solo": {"Metal", "Grunge", "Punk", "Industrial"},
            "No Solos": {"Classical", "Opera", "Ambient", "New Age"}
        }
    },

    # Live performance elements exclude genres that don't match the observed performance style.
    "Assess Live Performance Elements": {
        "type": "str",
        "states": {
            "High Energy": {"Ambient", "New Age", "Classical", "Opera"},
            "Low Energy": {"Metal", "Grunge", "Punk", "Industrial"},
            "Audience Interaction": {"Electronic", "EDM", "Techno", "House", "Trance"}
        }
    },

    # Synthesizer use excludes genres that don't fit the observed synthesizer presence.
    "Evaluate Use of Synthesizers": {
        "type": "str",
        "states": {
            "Extensive Use": {"Classical", "Jazz", "Blues", "Folk", "Country"},
            "Minimal Use": {"EDM", "Trance", "Techno", "House", "Dubstep"},
            "No Use": {"Hip Hop", "Rap", "Pop", "Rock", "Metal"}
        }
    },

    # Background vocals usage excludes genres that don't match the observed backing vocal style.
    "Examine Background Vocals": {
        "type": "str",
        "states": {
            "Harmonized Background Vocals": {"Hip Hop", "Rap", "EDM", "Techno", "House"},
            "Call and Response": {"Classical", "Opera", "Jazz", "Blues", "Folk"},
            "No Background Vocals": {"Metal", "Grunge", "Punk", "Industrial"}
        }
    },

    # Acoustic vs. electric instrument balance excludes genres not aligning with the observed combination.
    "Analyze Acoustic vs. Electric Instruments": {
        "type": "str",
        "states": {
            "All Acoustic": {"Electronic", "EDM", "Techno", "House", "Trance"},
            "All Electric": {"Classical", "Jazz", "Blues", "Folk", "Country"},
            "Mix of Both": {"Pop", "Rock", "Hip Hop", "Reggae", "Metal"}
        }
    },

    # Percussion usage excludes genres that don't fit the observed percussion style.
    "Assess Use of Percussion": {
        "type": "str",
        "states": {
            "Heavy Percussion": {"Ambient", "New Age", "Classical", "Opera"},
            "Light Percussion": {"Metal", "Grunge", "Punk", "Industrial"},
            "Electronic Percussion": {"Jazz", "Blues", "Folk", "Country"}
        }
    },

    # Genre fusion elements exclude genres that don't match the complexity of genre mixing observed.
    "Evaluate Genre Fusion Elements": {
        "type": "str",
        "states": {
            "Genre Fusion": {"Classical", "Opera", "Jazz", "Blues", "Folk"},
            "Pure Genre": {"Pop", "Rock", "Hip Hop", "Country", "Reggae"}
        }
    },

    # Song length excludes genres not known for tracks of that duration.
    "Examine Song Length": {
        "type": "float",
        "states": {
            (0, 2): {"Classical", "Opera", "Jazz", "Ambient", "New Age"},
            (2, 4): {"Metal", "Grunge", "Punk", "Industrial"},
            (4, 10): {"Pop", "Rock", "Hip Hop", "Country", "Reggae"},
            (10, 60): {"EDM", "Trance", "Techno", "House", "Dubstep"}
        }
    },

    # Lyrics theme excludes genres not associated with such thematic content.
    "Analyze Lyrics Theme": {
        "type": "str",
        "states": {
            "Social Issues": {"EDM", "Trance", "Techno", "House", "Dubstep"},
            "Personal Experiences": {"Classical", "Opera", "Jazz", "Blues", "Folk"},
            "Fantasy": {"Hip Hop", "Rap", "Pop", "Rock", "Metal"}
        }
    },

    # Orchestration style excludes genres that don't match the observed orchestration.
    "Assess Orchestration": {
        "type": "str",
        "states": {
            "Full Orchestra": {"Hip Hop", "Rap", "EDM", "Techno", "House"},
            "String Sections": {"Metal", "Grunge", "Punk", "Industrial"},
            "No Orchestration": {"Classical", "Opera", "Jazz", "Blues", "Folk"}
        }
    },

    # Vocal harmonies exclude genres not known for the observed harmonic complexity in vocals.
    "Evaluate Vocal Harmonies": {
        "type": "str",
        "states": {
            "Complex Harmonies": {"Hip Hop", "Rap", "EDM", "Techno", "House"},
            "Simple Harmonies": {"Metal", "Grunge", "Punk", "Industrial"},
            "No Harmonies": {"Classical", "Opera", "Jazz", "Blues", "Folk"}
        }
    },

    # Use of traditional instruments excludes genres not aligned with the observed instrumentation.
    "Examine Use of Traditional Instruments": {
        "type": "str",
        "states": {
            "Traditional Instruments": {"Electronic", "EDM", "Techno", "House", "Trance"},
            "Modern Instruments": {"Classical", "Opera", "Jazz", "Blues", "Folk"},
            "Fusion Instruments": {"Pop", "Rock", "Hip Hop", "Reggae", "Metal"}
        }
    },

    # Beat patterns exclude genres that don't match the observed beat style.
    "Analyze Beat Patterns": {
        "type": "str",
        "states": {
            "Steady Beat": {"Classical", "Opera", "Jazz", "Blues", "Folk"},
            "Variable Beat": {"Metal", "Grunge", "Punk", "Industrial"},
            "Electronic Beat": {"Pop", "Rock", "Hip Hop", "Reggae", "EDM"}
        }
    },

    # Auto-Tune use excludes genres that don't match the observed vocal processing.
    "Assess Use of Auto-Tune": {
        "type": "str",
        "states": {
            "Heavy Auto-Tune": {"Classical", "Opera", "Jazz", "Blues", "Folk"},
            "No Auto-Tune": {"Hip Hop", "Rap", "Pop", "Rock", "Metal"}
        }
    },

    # Audience participation elements exclude genres that don't fit the observed interaction style.
    "Examine Audience Participation Elements": {
        "type": "str",
        "states": {
            "Call and Response": {"EDM", "Trance", "Techno", "House", "Dubstep"},
            "Sing-Alongs": {"Metal", "Grunge", "Punk", "Industrial"},
            "No Participation": {"Classical", "Opera", "Jazz", "Blues", "Folk"}
        }
    },

    # Thematic consistency excludes genres not aligning with the observed thematic pattern.
    "Analyze Thematic Consistency": {
        "type": "str",
        "states": {
            "High Consistency": {"Hip Hop", "Rap", "Pop", "Rock", "Metal"},
            "Low Consistency": {"Classical", "Opera", "Jazz", "Blues", "Folk"}
        }
    },

    # Album concept clues exclude genres not matching the observed conceptual approach.
    "Assess Album Concept": {
        "type": "str",
        "states": {
            "Concept Album": {"EDM", "Trance", "Techno", "House", "Dubstep"},
            "Non-Concept Album": {"Metal", "Grunge", "Punk", "Industrial"},
            "Singles Collection": {"Classical", "Opera", "Jazz", "Blues", "Folk"}
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