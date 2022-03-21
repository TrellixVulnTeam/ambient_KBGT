from music21 import * 

stream1 = stream.Stream()

meter1 = meter.TimeSignature('4/4')

chord1 = chord.Chord(['c3', 'g4', 'c5', 'e5'], type='whole')

chord2 = chord.Chord(['f3', 'bb4', 'c5', 'f5'], type='whole')

chord3 = chord.Chord(['g3', 'bb4', 'd5', 'f5'], type='whole')

stream1.append([meter1, chord1, chord2, chord3])

# stream1.append(['c4', 'e4', 'g4'], ['d', 'f#', 'a'])

stream1.show()
