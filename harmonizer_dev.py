"""
This is a bass line harmonizer, version 1.0.
It takes bass line as input and automatically gengerate the chords.
Then export the as a MIDI file.
"""
from harmonizer_dict import note_accidental_range_to_midi
from harmonizer_dict import note_accidental_to_semitone
from harmonizer_dict import note_to_number, number_to_note
from harmonizer_dict import chord_quality_to_diatonic, chord_quality_to_semitone
from harmonizer_dict import semitone_to_accidental
from harmonizer_dict import pre_assign_register

from musx import Score, Seq, MidiFile, keynum, rhythm
from musx.midi.gm import ChurchOrgan
from musx.paint import brush

# from interval_calculator_3
import random

########################## INPUT ##########################

# Bass line function:
def get_input(question):
    answer = input(question).lower()
    splitted_answer = answer.split()
    return splitted_answer

# Get the bass line:
bass_line = get_input('\n' + 'Hello, please enter the bass line and separate by space: ')

# Test:
print('\n' + 'bass_line: ' + str(bass_line))

# Get the each note from the bass line:
i = 0
for i in range(len(bass_line)):
    exec("bass_%d = %s" % (i, repr(bass_line[i])))
    
# Test:
# i = 0
# for i in range(len(bass_line)):
#     print("element %d (bass_%d): %s" % (i, i, repr(bass_line[i])))

######################## BASS LINE ########################

# Decide first bass note register:
if bass_line[0] in ['a', 'b']:
    bass_0_range = bass_line[0] + '2'
else:
    bass_0_range = bass_line[0] + '3'

# Test:
# print('\n' + 'bass_0 w/ range (bass_0_register): ' + str(bass_0_range))

# Bass line function:
# def getBassline(first_bass_note):

# Set up the bass line result:
bass_line_result = [bass_0_range]

for i in range(1, len(bass_line)):
    # Add range to the next bass note
    option_1 = bass_line[i] + '3'
    option_2 = bass_line[i] + '2'
    # Test
    # print('\n' + 'option_1/option_2: ' + option_1 + ', ' + option_2)  
    # Get next bass note midi note number
    option_1_midi = note_accidental_range_to_midi[option_1]
    option_2_midi = note_accidental_range_to_midi[option_2]
    # Test
    # print('option_1_midi/option_2_midi: ' + str(option_1_midi) + ', ' + str(option_2_midi))
    # Get previous note midi note number
    previous_note_midi = note_accidental_range_to_midi[bass_line_result[i-1]]
    # Test
    # print('previous_note: ' + str(bass_line_result[i-1]))
    # print('previous_note_midi: ' + str(previous_note_midi))
    # If the current note is same as the previous note, continue to next loop
    if option_1 == bass_line_result[i-1]: 
        next_bass_note = option_1
        bass_line_result.append(next_bass_note)
        i += 1
        continue
    elif option_2 == bass_line_result[i-1]:
        next_bass_note = option_2
        bass_line_result.append(next_bass_note)
        i += 1
        continue
    # Get the distance (absolute value)
    option_1_distance = abs(previous_note_midi - option_1_midi)
    option_2_distance = abs(previous_note_midi - option_2_midi)
    # Test
    # print('option_1_distance/option_2_distance: ' + str(option_1_distance) + ', ' + str(option_2_distance))
    # Compare the distance
    if option_1_distance < option_2_distance:
        next_bass_note = option_1
    elif option_2_distance < option_1_distance:
        next_bass_note = option_2
    # Deal with tritone
    else: 
        # Set D3 (midi num 50) as boundary
        if previous_note_midi >= 50:
            # If note is high, go downward
            next_bass_note = option_2
        else:
            # If note is low, go upward
            next_bass_note = option_1
    # Test
    # print('next_bass_note: ' + next_bass_note)
    # Append the next bass note to the result
    bass_line_result.append(next_bass_note)
    # Update the counter
    i += 1
    # return bass_line_result

# Test
print('\n' + 'bass_line_result: ' + str(bass_line_result))

##################### CHORD QUALITY SCHEME #####################

# Set up the chord quality list:
chord_quality = ['', 'm', 'sus2', 'sus4', 'maj7','m7']

# Set up the chord scheme:
chord_select = []

# Randomly select from quality list and create the scheme
chord_select = random.choices(chord_quality, k=len(bass_line))

# Test:
print('\n' + 'chord_select: ' + str(chord_select))

# Turn bass line list into upper case:
bass_line_upper = map(lambda i: i.capitalize(), bass_line)

# Merge the bass line and chord scheme:
chord_scheme = [i + j for i, j in zip(bass_line_upper, chord_select)]

# Test:
print('\n' + 'chord_scheme: ' + str(chord_scheme))

##################### SPELL THE CHORDS ##################### 

# Set up the list for all spelled chord:
all_chord_result = []

# Spell out the chord:
for i in range(len(bass_line)):
    # Get the root of the chord:
    chord_root = bass_line[i]
    # Get the standard chord semitone:
    standard_chord_semitone = chord_quality_to_semitone[chord_select[i]]
    # Get the chord bass number:
    chord_bass_number = note_to_number[bass_line[i][0]]
    # Test:
    # print('\n' + 'chord_bass_number: ' + str(chord_bass_number))
    # Get the chord quality diatonic distance:
    chord_diatonic_distance = chord_quality_to_diatonic[chord_select[i]]
    # Test:
    # print('chord_diatonic_distance: ' + str(chord_diatonic_distance))
    # Set up the chord number list:
    chord_number_list = []
    # Add diatonic distance one by one:
    for j in range(len(chord_diatonic_distance)):
        next_note_number = chord_bass_number + chord_diatonic_distance[j]
        # If out of range, substract 7
        if next_note_number > 7:
            next_note_number -= 7
        chord_number_list.append(next_note_number)
        j += 1
    # Test 
    # print('chord_number_list: ' + str(chord_number_list))
    # Set up chord diatonic list:
    chord_diatonic_list = []
    # Get chord diatonic list:
    for k in range(len(chord_number_list)):
        # Append the root as exact note
        if chord_diatonic_distance[k] == 0:
            chord_diatonic_list.append(chord_root)
            k += 1
            continue
        # Append other notes of the chord
        next_diatonic_note = number_to_note[chord_number_list[k]]
        chord_diatonic_list.append(next_diatonic_note)
        k += 1
    # Test:
    # print('chord_diatonic_list: ' + str(chord_diatonic_list))
    # Set up the diatonic chord semitone list:
    chord_semitone_list = []
    # Get the the diatonic chord semitone list:
    for i in range(len(chord_diatonic_list)):
        next_semitone_number = note_accidental_to_semitone[chord_diatonic_list[i]]
        # Make sure the each note number is greater than the root:
        if next_semitone_number < note_accidental_to_semitone[chord_diatonic_list[0]]:
            next_semitone_number += 12
        chord_semitone_list.append(next_semitone_number)
    # Make sure the list si in ascending order:
    for i in range(1, len(chord_semitone_list)):
        if chord_semitone_list[i] < chord_semitone_list[i-1]:
            chord_semitone_list[i] += 12
    # Test:
    # print('chord_semitone_list: ' + str(chord_semitone_list))
    # Set up the semitone distance list:
    semitone_distance_list = []
    # Calculate the distance between each semitone:
    for j in range(len(chord_semitone_list)):
        next_semitone_distance = chord_semitone_list[j] - chord_semitone_list[0]
        semitone_distance_list.append(next_semitone_distance)
        j += 1
    # Test
    # print('semitone_distance_list: ' + str(semitone_distance_list))
    # print('standard_chord_semitone: ' + str(standard_chord_semitone))
    # Set up the chord semitone difference list:
    semitone_difference_list = []
    # Calculate the difference with standard chord semitone list:
    for j in range(len(semitone_distance_list)):
        next_semitone_difference = standard_chord_semitone[j] - semitone_distance_list[j]
        semitone_difference_list.append(next_semitone_difference)
        j += 1
    # Test:
    # print('semitone_difference_list: ' + str(semitone_difference_list))
    # Set up the accidentals list:
    accidental_change_list = []
    # Create the accidentals list:
    for k in range(len(semitone_difference_list)):
        try:
            next_accidental = semitone_to_accidental[semitone_difference_list[k]]
            accidental_change_list.append(next_accidental)
            k += 1
        except:
            print('\n' + 'INVALID CHORD: TOO MUCH ACCIDENTALS' + '\n')
            exit()
    # Test:
    # print('accidental_change_list: ' + str(accidental_change_list))
    # Set up list for final result:
    chord_result = []
    # Append the accidentals:
    for i in range(len(accidental_change_list)):
        chord_result.append(chord_diatonic_list[i] + accidental_change_list[i])
        i += 1
    # Test:
    # print('\n' + 'chord_result: ' + str(chord_result))
    # Append the final result:
    all_chord_result.append(chord_result)

# Test:
print('\n' + 'all_chord_result: ' + str(all_chord_result) + '\n')

##################### WRITE OUT THE CHORDS ####################

# Extract each chord and gengerate all the possible combinations:
for i in range(len(all_chord_result)):
    selected_chord = all_chord_result[i]
    selected_chord_0 = [selected_chord[0], selected_chord[1], selected_chord[2], selected_chord[3]]
    selected_chord_1 = [selected_chord[0], selected_chord[1], selected_chord[3], selected_chord[2]]
    selected_chord_2 = [selected_chord[0], selected_chord[2], selected_chord[1], selected_chord[3]]
    selected_chord_3 = [selected_chord[0], selected_chord[2], selected_chord[3], selected_chord[1]]
    selected_chord_4 = [selected_chord[0], selected_chord[3], selected_chord[1], selected_chord[2]]
    selected_chord_5 = [selected_chord[0], selected_chord[3], selected_chord[2], selected_chord[1]]
    chord_combination = [selected_chord_0, selected_chord_1, selected_chord_2, selected_chord_3, selected_chord_4, selected_chord_5]
    i += 1
    # Test
    print('chord_combination: ' + str(chord_combination) + '\n')

######################## PLAY AND TEST ########################

# Temporary method to assign the register:
# for i in range(len(all_chord_result)):
#     # Set up counter for second level list
#     for j in range(len(all_chord_result[i])):
#         if j == 0:
#             # Append '3' for the root of the chord
#             all_chord_result[i][0] += '3'
#             j += 1
#         else:
#             # Append '4' for other notes
#             all_chord_result[i][j] += '4'
#             j += 1
#     # Update the counter
#     i += 1

# # Test:
# print('all_chord_result (register): ' + str(all_chord_result) + '\n')

# Define the melody:
# melody = keynum(all_chord_result)

# # Main function:
# if __name__ == '__main__':
#     # Meta track:
#     track0 = MidiFile.metatrack()
#     # Track holds the composition:
#     track1 = Seq()
#     # Create the score:
#     score = Score(out = track1)
#     # Compose the score:
#     score.compose(brush(
#         score, 
#         length=len(melody), 
#         pitch=melody, 
#         rhythm=rhythm(1, tempo=60),
#         # duration=0.2, 
#         amplitude=0.9, 
#         instrument=ChurchOrgan,
#         ))
#     # Create the Midi file:
#     file = MidiFile('harmonizer_test.mid', [track0, track1]).write()
#     # Test: 
#     print(f"{file.pathname} finished!" + '\n')

###########################################################

# Call the function:
# bass_line = get_input('\n' + 'Hello, please enter the bass line and separate by space: ')

# Test:
# print('\n' + 'bass_line: ' + str(bass_line))

###########################################################

# Call the function:
# bass_line_result = get_bass_line(bass_line)

# Test:
# print('\n' + 'bass_line_result: ' + str(bass_line_result))

###########################################################

# Call the function:
# chord_select = chord_quality_scheme(bass_line)[0]
# chord_scheme = chord_quality_scheme(bass_line)[1]

# Test:
# print('\n' + 'chord_select: ' + str(chord_select))
# print('\n' + 'chord_scheme: ' + str(chord_scheme))

###########################################################

# Call the function:
# all_chord_result = spell_chord(bass_line)

# Test:
# print('\n' + 'all_chord_result: ' + str(all_chord_result) + '\n')

###########################################################

# Call the function:
# chord_combination = note_combination(all_chord_result)

# Test:
# print('chord_combination: ' + str(chord_combination) + '\n')

###########################################################