from music21 import * 

score = stream.Score()
part_1 = stream.Part()
part_2 = stream.Part()

meters = meter.TimeSignature('4/4')
treble = clef.TrebleClef()
bass = clef.BassClef()

chord1 = chord.Chord(['c3', 'g4', 'c5', 'e5'], type='whole')
chord2 = chord.Chord(['f3', 'bb4', 'c5', 'f5'], type='whole')
chord3 = chord.Chord(['g3', 'bb4', 'd5', 'f5'], type='whole')

part_1.append([treble, meters, chord1, chord2, chord3])
part_2.append([bass, meters, chord1[0], chord2[0], chord3[0]])

score.insert(0, part_1)
score.insert(0, part_2)
score.show()