from music21 import clef, meter, bar, chord, note, stream
from main_multi_solution import main
# from main import main

score = stream.Score()
part_1 = stream.Part()
part_2 = stream.Part()

# Assign clef and time signatures:
treble = clef.TrebleClef()
bass = clef.BassClef()
meters = meter.TimeSignature('4/4')

# Assign Double barline:
barline = bar.Barline(type='final', location='right')

# Add to the parts:
part_1.append([treble, meters])
part_2.append([bass, meters])

# Take the input:
user_input = main()

# Get the output:
chord_progression = user_input[0]
bass_line = user_input[1]
# chord_progression = [
#     [['c3', 'g4', 'c5', 'eb5'], ['d3', 'f#4', 'a4', 'd5'], ['a2', 'e4', 'g#4', 'c#5'], ['b2', 'd#4', 'f#4', 'b4']], 
#     [['c4', 'g4', 'c5', 'eb5'], ['d3', 'f#4', 'a4', 'd5'], ['a2', 'e4', 'g#4', 'c#5'], ['b2', 'd#4', 'f#4', 'b4']], 
#     [['c3', 'eb4', 'g4', 'c5'], ['d3', 'd4', 'f#4', 'a4'], ['a2', 'e4', 'g#4', 'c#5'], ['b2', 'd#4', 'f#4', 'b4']]
# ]

# Insert the double barline:
# for i in range(len(chord_progression)):
#     # Get to know where to insert the barline:
#     location = len(chord_progression[0][0])
#     # Insert the barline:
#     part_1.insert(location * i, barline)

# Flatten the chord_progression:
flatten_chord_progression = [item for sublist in chord_progression for item in sublist]
print('\nflatten_chord_progression: ' + str(flatten_chord_progression))

# Extract the bass line from the chord progression: 
temp_chord = []
bass_line = []
for i in range(len(flatten_chord_progression)):
    temp_chord = flatten_chord_progression[i]
    bass_line.append(temp_chord[0])
print('\nbass_line: ' + str(bass_line))
print(len(bass_line))

# Remove the bass line from chord progression:
temp_chord = []
bass_line_removed = []
for i in range(len(flatten_chord_progression)):
    temp_chord = flatten_chord_progression[i]
    temp_chord.pop(0)
    bass_line_removed.append(temp_chord)
print('\nbass_line_removed: ' + str(bass_line_removed))
print(len(bass_line_removed)) 

# Convert into Music21 chord format - part 1:
for j in range(len(bass_line_removed)):
    part_1.append(chord.Chord(bass_line_removed[j], type='whole'))

# Convert into Music21 note format - part 2:
for k in range(len(bass_line)):
    part_2.append(note.Note(bass_line[k], type='whole'))

# Visualize the score:
score.insert(0, part_1)
score.insert(0, part_2)
score.show()