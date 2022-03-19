# Key Dictionary
key_dict = {'c': 1, 'd': 2, 'e': 3, 'f': 4, 'g': 5, 'a': 6,'b': 7}

# Extended Key Dictionary (w/ octave register)
key_dict_extend = {
    'c0': 0, 'd0': 1, 'e0': 2, 'f0': 3, 'g0': 4, 'a0': 5, 'b0': 6, 
    'c1': 7, 'd1': 8, 'e1': 9, 'f1': 10, 'g1': 11, 'a1': 12, 'b1': 13, 
    'c2': 14, 'd2': 15, 'e2': 16, 'f2': 17, 'g2': 18, 'a2': 19, 'b2': 20, 
    'c3': 21, 'd3': 22, 'e3': 23, 'f3': 24, 'g3': 25, 'a3': 26, 'b3': 27, 
    'c4': 28, 'd4': 29, 'e4': 30, 'f4': 31, 'g4': 32, 'a4': 33, 'b4': 34, 
    'c5': 35, 'd5': 36, 'e5': 37, 'f5': 38, 'g5': 39, 'a5': 40, 'b5': 41, 
    'c6': 42, 'd6': 43, 'e6': 44, 'f6': 45, 'g6': 46, 'a6': 47, 'b6': 48, 
    'c7': 49, 'd7': 50, 'e7': 51, 'f7': 52, 'g7': 53, 'a7': 54, 'b7': 55, 
    'c8': 56, 'd8': 57, 'e8': 58, 'f8': 59, 'g8': 60, 'a8': 61, 'b8': 62, 
    'c9': 63, 'd9': 64, 'e9': 65, 'f9': 66, 'g9': 67, 'a9': 68, 'b9': 69
}

# Input dictionary
input_dict = {
    1: 'cbb', 2: 'cb', 3: 'c', 4: 'c#', 5: 'c##', 
    6: 'dbb', 7: 'db', 8: 'd', 9: 'd#', 10: 'd##', 
    11: 'ebb', 12: 'eb', 13: 'e', 14: 'e#', 15: 'e##', 
    16: 'fbb', 17: 'fb', 18: 'f', 19: 'f#', 20: 'f##', 
    21: 'gbb', 22: 'gb', 23: 'g', 24: 'g#', 25: 'g##', 
    26: 'abb', 27: 'ab', 28: 'a', 29: 'a#', 30: 'a##', 
    31: 'bbb', 32: 'bb', 33: 'b', 34: 'b#', 35: 'b##'
}

input_dict_2 = {
    'cbb': 1, 'cb': 2, 'c': 3, 'c#': 4, 'c##': 5, 
    'dbb': 6, 'db': 7, 'd': 8, 'd#': 9, 'd##': 10, 
    'ebb': 11, 'eb': 12, 'e': 13, 'e#': 14, 'e##': 15, 
    'fbb': 16, 'fb': 17, 'f': 18, 'f#': 19, 'f##': 20, 
    'gbb': 21, 'gb': 22, 'g': 23, 'g#': 24, 'g##': 25, 
    'abb': 26, 'ab': 27, 'a': 28, 'a#': 29, 'a##': 40, 
    'bbb': 31, 'bb': 32, 'b': 33, 'b#': 34, 'b##': 35
}

# Interval dictionary
interval_dict = {
    0: 'unison', 1: 'second', 2: 'third', 3: 'fourth', 
    4: 'fifth', 5: 'sixth', 6: 'seventh', 7: 'octave'
}

# Benchmark dictionary (major and perfect)
benchmark_dict = {
    'unison': 0,    # Unison
    'second': 2,    # Major 2nd
    'third': 4,     # Major 3rd
    'fourth': 5,    # Perfect 4th
    'fifth': 7,     # Perfect 5th
    'sixth': 9,     # Major 6th
    'seventh': 11,  # Major 7th
    'octave': 12    # Octave
}

# Major/minor quality dictionary
major_quality_dict = {
    -5: 'quarduply diminished', 
    -4: 'triply diminished', 
    -3: 'doubly diminished', 
    -2: 'diminished', 
    -1: 'minor', 
    0: 'major', 
    1: 'augmented', 
    2: 'doubly augmented', 
    3: 'triply augmented',
    4: 'quardruply augmented'
}

# Perfect quality dictionary
perfect_quality_dict = {
    -5: 'quintuply diminished', 
    -4: 'quadruply diminished', 
    -3: 'triply diminished', 
    -2: 'doubly diminished', 
    -1: 'diminished', 
    0: 'perfect', 
    1: 'augmented', 
    2: 'doubly augmented', 
    3: 'triply augmented', 
    4: 'quadruply augmented', 
    5: 'quintuply augmented'
}

# Octave dictionary:
octave_dict = {
    1: '', 
    2: 'double ', 
    3: 'triple ', 
    4: 'quardruple ', 
    5: 'quintuple ', 
    6: 'sextuple ', 
    7: 'septuple ', 
    8: 'eightfold ', 
    9: 'ninefold '
}

# Semitone dictionary
semitone_dict = {
    'cbb': 10, 'cb': 11, 'c': 0, 'c#': 1, 'c##': 2, 
    'dbb': 0, 'db': 1, 'd': 2, 'd#': 3, 'd##': 4, 
    'ebb': 2, 'eb': 3, 'e': 4, 'e#': 5, 'e##': 6,
    'fbb': 3, 'fb': 4, 'f': 5, 'f#': 6, 'f##': 7, 
    'gbb': 5, 'gb': 6, 'g': 7, 'g#': 8, 'g##': 9, 
    'abb': 7, 'ab': 8, 'a': 9, 'a#': 10, 'a##': 11, 
    'bbb': 9, 'bb': 10, 'b': 11, 'b#': 0, 'b##': 1
}

# Chord quality dictionary
quality_dict_1 = {
    (0, 4, 7): 'major', (0, 3, 8): 'first inversion of major', (0, 5, 9): 'second inversion of major', 
    (0, 3, 7): 'minor', (0, 4, 9): 'first inversion of minor', (0, 5, 8): 'second inversion of minor', 
    (0, 3, 6): 'diminished', (0, 3, 9): 'first inversion of diminished', (0, 6, 9): 'second inversion of diminished',
    (0, 4, 7, 10): 'major minor 7th', (0, 3, 6, 8): 'first inversion of major minor 7th', (0, 3, 5, 9): 'second inversion of major minor 7th', (0, 2, 6, 9): 'third inversion of major minor 7th', 
    (0, 3, 7, 10): 'minor minor 7th', (0, 4, 7, 9): 'first inversion of minor minor 7th', (0, 4, 6, 9): 'second inversion of minor minor 7th', (0, 2, 5, 9): 'third inversion of minor minor 7th', 
    (0, 4, 7, 11): 'major major 7th', (0, 3, 7, 8): 'first inversion of major major 7th', (0, 4, 5, 9): 'second inversion of major major 7th', (0, 1, 5, 8): 'third inversion of major major 7th', 
    (0, 3, 7, 11): 'minor major 7th', (0, 4, 8, 9): 'first inversion of minor major 7th', (0, 4, 5, 8): 'second inversion of minor major 7th', (0, 1, 4, 8): 'third inversion of minor major 7th', 
    (0, 3, 6, 10): 'half diminished 7th', (0, 3, 7, 9): 'first inversion of half diminished 7th', (0, 4, 6, 9): 'second inversion of half diminished 7th', (0, 2, 5, 8): 'third inversion of half diminished 7th'
}

quality_dict_2 = {
    (0, 2, 4): 'augmented', (0, 2, 5): 'first inversion of augmented', (0, 3, 5): 'second inversion of augmented', 
    (0, 2, 4, 6): 'fully diminished 7th', (0, 2, 4, 5): 'first inversion of fully diminished 7th', (0, 2, 3, 5): 'second inversion of fully diminished 7th', (0, 1, 3, 5): 'third inversion of fully diminished 7th'
}

# Cross check dictionary (quality and distance)
cross_check_dict = {
    'major': (0, 2, 4), 'first inversion of major': (0, 2, 5), 'second inversion of major': (0, 3, 5), 
    'minor': (0, 2, 4), 'first inversion of minor': (0, 2, 5), 'second inversion of minor': (0, 3, 5), 
    'diminished': (0, 2, 4), 'first inversion of diminished': (0, 2, 5), 'second inversion of diminished': (0, 3, 5), 
    'augmented': (0, 2, 4), 'first inversion of augmented': (0, 2, 5), 'second inversion of augmented': (0, 3, 5), 
    'major minor 7th': (0, 2, 4, 6), 'first inversion of major minor 7th': (0, 2, 4, 5), 'second inversion of major minor 7th': (0, 2, 3, 5), 'third inversion of major minor 7th': (0, 1, 3, 5), 
    'minor minor 7th': (0, 2, 4, 6), 'first inversion of minor minor 7th': (0, 2, 4, 5), 'second inversion of minor minor 7th': (0, 2, 3, 5), 'third inversion of minor minor 7th': (0, 1, 3, 5), 
    'major major 7th': (0, 2, 4, 6), 'first inversion of major major 7th': (0, 2, 4, 5), 'second inversion of major major 7th': (0, 2, 3, 5), 'third inversion of major major 7th': (0, 1, 3, 5), 
    'minor major 7th': (0, 2, 4, 6), 'first inversion of minor major 7th': (0, 2, 4, 5), 'second inversion of minor major 7th': (0, 2, 3, 5), 'third inversion of minor major minor 7th': (0, 1, 3, 5), 
    'half diminished 7th': (0, 2, 4, 6), 'first inversion of half diminished 7th': (0, 2, 4, 5), 'second inversion of half diminished 7th': (0, 2, 3, 5), 'third inversion of half diminished 7th': (0, 1, 3, 5), 
    'fully diminished 7th': (0, 2, 4, 6), 'first inversion of fully diminished 7th': (0, 2, 4, 5), 'second inversion of fully diminished 7th': (0, 2, 3, 5), 'third inversion of fully diminished 7th': (0, 1, 3, 5), 
}

# Midi note dictionary:
midi_dict = {
    'cbb0': 10, 'cb0': 11, 'c0': 12, 'c#0': 13, 'c##0': 14, 'dbb0': 12, 'db0': 13, 'd0': 14, 'd#0': 15, 'd##0': 16, 'ebb0': 14, 'eb0': 15, 'e0': 16, 'e#0': 17, 'e##0': 18, 'fbb0': 15, 'fb0': 16, 'f0': 17, 'f#0': 18, 'f##0': 19, 'gbb0': 17, 'gb0': 18, 'g0': 19, 'g#0': 20, 'g##0': 21, 'abb0': 19, 'ab0': 20, 'a0': 21, 'a#0': 22, 'a##0': 23, 'bbb0': 21, 'bb0': 22, 'b0': 23, 'b#0': 24, 'b##0': 25, 
    'cbb1': 22, 'cb1': 23, 'c1': 24, 'c#1': 25, 'c##1': 26, 'dbb1': 24, 'db1': 25, 'd1': 26, 'd#1': 27, 'd##1': 28, 'ebb1': 26, 'eb1': 27, 'e1': 28, 'e#1': 29, 'e##1': 30, 'fbb1': 27, 'fb1': 28, 'f1': 29, 'f#1': 30, 'f##1': 31, 'gbb1': 29, 'gb1': 30, 'g1': 31, 'g#1': 32, 'g##1': 33, 'abb1': 31, 'ab1': 32, 'a1': 33, 'a#1': 34, 'a##1': 35, 'bbb1': 33, 'bb1': 34, 'b1': 35, 'b#1': 36, 'b##1': 37, 
    'cbb2': 34, 'cb2': 35, 'c2': 36, 'c#2': 37, 'c##2': 38, 'dbb2': 36, 'db2': 37, 'd2': 38, 'd#2': 39, 'd##2': 40, 'ebb2': 38, 'eb2': 39, 'e2': 40, 'e#2': 41, 'e##2': 42, 'fbb2': 39, 'fb2': 40, 'f2': 41, 'f#2': 42, 'f##2': 43, 'gbb2': 41, 'gb2': 42, 'g2': 43, 'g#2': 44, 'g##2': 45, 'abb2': 43, 'ab2': 44, 'a2': 45, 'a#2': 46, 'a##2': 47, 'bbb2': 45, 'bb2': 46, 'b2': 47, 'b#2': 48, 'b##2': 49, 
    'cbb3': 46, 'cb3': 47, 'c3': 48, 'c#3': 49, 'c##3': 50, 'dbb3': 48, 'db3': 49, 'd3': 50, 'd#3': 51, 'd##3': 52, 'ebb3': 50, 'eb3': 51, 'e3': 52, 'e#3': 53, 'e##3': 54, 'fbb3': 51, 'fb3': 52, 'f3': 53, 'f#3': 54, 'f##3': 55, 'gbb3': 53, 'gb3': 54, 'g3': 55, 'g#3': 56, 'g##3': 57, 'abb3': 55, 'ab3': 56, 'a3': 57, 'a#3': 58, 'a##3': 59, 'bbb3': 57, 'bb3': 58, 'b3': 59, 'b#3': 60, 'b##3': 61, 
    'cbb4': 58, 'cb4': 59, 'c4': 60, 'c#4': 61, 'c##4': 62, 'dbb4': 60, 'db4': 61, 'd4': 62, 'd#4': 63, 'd##4': 64, 'ebb4': 62, 'eb4': 63, 'e4': 64, 'e#4': 65, 'e##4': 66, 'fbb4': 63, 'fb4': 64, 'f4': 65, 'f#4': 66, 'f##4': 67, 'gbb4': 65, 'gb4': 66, 'g4': 67, 'g#4': 68, 'g##4': 69, 'abb4': 67, 'ab4': 68, 'a4': 69, 'a#4': 70, 'a##4': 71, 'bbb4': 69, 'bb4': 70, 'b4': 71, 'b#4': 72, 'b##4': 73, 
    'cbb5': 70, 'cb5': 71, 'c5': 72, 'c#5': 73, 'c##5': 74, 'dbb5': 72, 'db5': 73, 'd5': 74, 'd#5': 75, 'd##5': 76, 'ebb5': 74, 'eb5': 75, 'e5': 76, 'e#5': 77, 'e##5': 78, 'fbb5': 75, 'fb5': 76, 'f5': 77, 'f#5': 78, 'f##5': 79, 'gbb5': 77, 'gb5': 78, 'g5': 79, 'g#5': 80, 'g##5': 81, 'abb5': 79, 'ab5': 80, 'a5': 81, 'a#5': 82, 'a##5': 83, 'bbb5': 81, 'bb5': 82, 'b5': 83, 'b#5': 84, 'b##5': 85, 
    'cbb6': 82, 'cb6': 83, 'c6': 84, 'c#6': 85, 'c##6': 86, 'dbb6': 84, 'db6': 85, 'd6': 86, 'd#6': 87, 'd##6': 88, 'ebb6': 86, 'eb6': 87, 'e6': 88, 'e#6': 89, 'e##6': 90, 'fbb6': 87, 'fb6': 88, 'f6': 89, 'f#6': 90, 'f##6': 91, 'gbb6': 89, 'gb6': 90, 'g6': 91, 'g#6': 92, 'g##6': 93, 'abb6': 91, 'ab6': 92, 'a6': 93, 'a#6': 94, 'a##6': 95, 'bbb6': 93, 'bb6': 94, 'b6': 95, 'b#6': 96, 'b##6': 97, 
    'cbb7': 94, 'cb7': 95, 'c7': 96, 'c#7': 97, 'c##7': 98, 'dbb7': 96, 'db7': 97, 'd7': 98, 'd#7': 99, 'd##7': 100, 'ebb7': 98, 'eb7': 99, 'e7': 100, 'e#7': 101, 'e##7': 102, 'fbb7': 99, 'fb7': 100, 'f7': 101, 'f#7': 102, 'f##7': 103, 'gbb7': 101, 'gb7': 102, 'g7': 103, 'g#7': 104, 'g##7': 105, 'abb7': 103, 'ab7': 104, 'a7': 105, 'a#7': 106, 'a##7': 107, 'bbb7': 105, 'bb7': 106, 'b7': 107, 'b#7': 108, 'b##7': 109, 
    'cbb8': 106, 'cb8': 107, 'c8': 108, 'c#8': 109, 'c##8': 110, 'dbb8': 108, 'db8': 109, 'd8': 110, 'd#8': 111, 'd##8': 112, 'ebb8': 110, 'eb8': 111, 'e8': 112, 'e#8': 113, 'e##8': 114, 'fbb8': 111, 'fb8': 112, 'f8': 113, 'f#8': 114, 'f##8': 115, 'gbb8': 113, 'gb8': 114, 'g8': 115, 'g#8': 116, 'g##8': 117, 'abb8': 115, 'ab8': 116, 'a8': 117, 'a#8': 118, 'a##8': 119, 'bbb8': 117, 'bb8': 118, 'b8': 119, 'b#8': 120, 'b##8': 121, 
    'cbb9': 118, 'cb9': 119, 'c9': 120, 'c#9': 121, 'c##9': 122, 'dbb9': 120, 'db9': 121, 'd9': 122, 'd#9': 123, 'd##9': 124, 'ebb9': 122, 'eb9': 123, 'e9': 124, 'e#9': 125, 'e##9': 126, 'fbb9': 123, 'fb9': 124, 'f9': 125, 'f#9': 126, 'f##9': 127, 'gbb9': 125, 'gb9': 126, 'g9': 127, 'g#9': 128, 'g##9': 129, 'abb9': 127, 'ab9': 128, 'a9': 129, 'a#9': 130, 'a##9': 131, 'bbb9': 129, 'bb9': 130, 'b9': 131, 'b#9': 132, 'b##9': 133
}