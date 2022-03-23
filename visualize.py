from music21 import clef, meter, chord, note, stream
# from main_multi_solution import main
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

# Remove the bass line from chord progression:
temp_chord = []
bass_line_removed = []
for i in range(len(chord_progression)):
    temp_chord = chord_progression[i]
    temp_chord.pop(0)
    bass_line_removed.append(temp_chord)

# Convert into Music21 chord format:
for j in range(len(chord_progression)):
    part_1.append(chord.Chord(bass_line_removed[j], type='whole'))

# Convert into Music21 note format:
for k in range(len(bass_line)):
    part_2.append(note.Note(bass_line[k], type='whole'))

# Visualize the score:
score.insert(0, part_1)
score.insert(0, part_2)
# score.show()