from music21 import * 
from main import main

score = stream.Score()
part_1 = stream.Part()
part_2 = stream.Part()

# Assign clef and time signatures:
treble = clef.TrebleClef()
bass = clef.BassClef()
meters = meter.TimeSignature('4/4')

# Add to the parts:
part_1.append([treble, meters])
part_2.append([bass, meters])

# Take the input:
user_input = main()

# Get the output:
chord_progression = user_input[0]
bass_line = user_input[1]

# Convert into Music21 chord format:
for i in range(len(chord_progression)):
    part_1.append(chord.Chord(chord_progression[i], type='whole'))

# Convert into Music21 note format:
for j in range(len(bass_line)):
    part_2.append(note.Note(bass_line[j], type='whole'))

# chord1 = chord.Chord(['c3', 'g4', 'c5', 'e5'], type='whole')
# chord2 = chord.Chord(['f3', 'bb4', 'c5', 'f5'], type='whole')
# chord3 = chord.Chord(['g3', 'bb4', 'd5', 'f5'], type='whole')

score.insert(0, part_1)
score.insert(0, part_2)
score.show()