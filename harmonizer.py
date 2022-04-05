from harmonizer_dict import note_accidental_range_to_midi
from harmonizer_dict import note_accidental_to_semitone
from harmonizer_dict import note_to_number, number_to_note
from harmonizer_dict import chord_quality_to_diatonic, chord_quality_to_semitone
from harmonizer_dict import semitone_to_accidental

import random

###########################################################

# Bass line input:
def get_input(question):
    answer = input(question).lower()
    splitted_answer = answer.split()
    return splitted_answer

###########################################################

# Bass line function:
def get_bass_line(bass_line):
    # Decide first bass note register:
    if bass_line[0] in ['a', 'b']:
        bass_0_range = bass_line[0] + '2'
    else:
        bass_0_range = bass_line[0] + '3'
    # Set up the bass line result:
    bass_line_result = [bass_0_range]
    if len(bass_line) == 1:
        return bass_line_result
    # Iteration:
    for i in range(1, len(bass_line)):
        # Add range to the next bass note
        option_1 = bass_line[i] + '3'
        option_2 = bass_line[i] + '2'
        # Get next bass note midi note number
        option_1_midi = note_accidental_range_to_midi[option_1]
        option_2_midi = note_accidental_range_to_midi[option_2]
        # Get previous note midi note number
        previous_note_midi = note_accidental_range_to_midi[bass_line_result[i-1]]
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
        # Append the next bass note to the result
        bass_line_result.append(next_bass_note)
        # Update the counter
    i += 1
    return bass_line_result

###########################################################

# Select the chord quality:
def chord_quality_scheme(bass_line):
    # Set up the chord quality list:
    chord_quality = ['', 'm', 'sus2', 'sus4', 'm7']
    # Give open chord simpler quality:
    open_chord_quality = ['', 'm', 'm7']
    # Set up the chord scheme:
    chord_select = []
    # Randomly select from quality list and create the scheme:
    for i in range(len(bass_line)):
        if i == 0:
            # Select the quality for starting chord:
            start_quality = random.choice(open_chord_quality)
            # Append to the result:
            chord_select.append(start_quality)
        else:
            # Select the quality for other chords:
            temp_quality = random.choice(chord_quality)
            # Check if the current quality equal to previous quality:
            if temp_quality == chord_select[-1]:
                # Remove the previous quality from the list:
                chord_quality.remove(chord_select[-1])
                # Excute the selection again:
                temp_quality = random.choice(chord_quality)
                # Append to the result:
                chord_select.append(temp_quality)
            else:
                # Append to the result:
                chord_select.append(temp_quality)
        # Restore the variable:
        chord_quality = ['', 'm', 'sus2', 'sus4', 'maj7','m7']
    # Turn bass line list into upper case:
    bass_line_upper = map(lambda i: i.capitalize(), bass_line)
    # Merge the bass line and chord scheme:
    chord_scheme = [i + j for i, j in zip(bass_line_upper, chord_select)]
    return chord_select, chord_scheme

###########################################################

# Spell the chord according to scheme:
def spell_chord(bass_line, chord_select):
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
        # Get the chord quality diatonic distance:
        chord_diatonic_distance = chord_quality_to_diatonic[chord_select[i]]
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
        # Set up the semitone distance list:
        semitone_distance_list = []
        # Calculate the distance between each semitone:
        for j in range(len(chord_semitone_list)):
            next_semitone_distance = chord_semitone_list[j] - chord_semitone_list[0]
            semitone_distance_list.append(next_semitone_distance)
            j += 1
        # Set up the chord semitone difference list:
        semitone_difference_list = []
        # Calculate the difference with standard chord semitone list:
        for j in range(len(semitone_distance_list)):
            next_semitone_difference = standard_chord_semitone[j] - semitone_distance_list[j]
            semitone_difference_list.append(next_semitone_difference)
            j += 1
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
        # Set up list for final result:
        chord_result = []
        # Append the accidentals:
        for i in range(len(accidental_change_list)):
            chord_result.append(chord_diatonic_list[i] + accidental_change_list[i])
            i += 1
        # Append the final result:
        all_chord_result.append(chord_result)
    return all_chord_result

###########################################################

# Extract each chord and gengerate all the possible combinations:
def note_combination(all_chord_result):
    # Container:
    all_combination = []
    for i in range(len(all_chord_result)):
        # Run through each combination:
        selected_chord = all_chord_result[i]
        selected_chord_0 = [selected_chord[0], selected_chord[1], selected_chord[2], selected_chord[3]]
        selected_chord_1 = [selected_chord[0], selected_chord[1], selected_chord[3], selected_chord[2]]
        selected_chord_2 = [selected_chord[0], selected_chord[2], selected_chord[1], selected_chord[3]]
        selected_chord_3 = [selected_chord[0], selected_chord[2], selected_chord[3], selected_chord[1]]
        selected_chord_4 = [selected_chord[0], selected_chord[3], selected_chord[1], selected_chord[2]]
        selected_chord_5 = [selected_chord[0], selected_chord[3], selected_chord[2], selected_chord[1]]
        chord_combination = [selected_chord_0, selected_chord_1, selected_chord_2, selected_chord_3, selected_chord_4, selected_chord_5]
        # Append to the container:
        all_combination.append(chord_combination)
    return all_combination

###########################################################