from harmonizer_dict import note_accidental_range_to_midi as midi_num
from harmonizer_dict import close_structure_dict as close_dict
from harmonizer_dict import pre_assign_register as pre
from distance_def import distance

import random

###########################################################

# Zip note and range together:
def note_range_zip(chord, register):
    # Container:
    temp_chord = []
    temp_range = []
    temp_list = []
    full_list = []
    # Iteration:
    for i in range(len(chord)):
        temp_chord = chord[i]
        for j in range(len(register)):
            temp_range = register[j]
            temp_list = [m + n for m, n in zip(temp_chord, temp_range)]
            full_list.append(temp_list)
            j += 1
        i += 1
    return full_list

###########################################################

# Latter note should higher than previous note:
def ascending_order(full_list):
    # Container:
    chord_for_test = []
    full_list_result = []
    # Iteration:
    for i in range(len(full_list)):
        chord_for_test = full_list[i]
        for j in range(1,len(chord_for_test)):
            last_note = midi_num[chord_for_test[j]]
            previous_note = midi_num[chord_for_test[j - 1]]
            if last_note >= previous_note:
                if j == len(chord_for_test) - 1:
                    full_list_result.append(chord_for_test)
            else:
                break
    return full_list_result

###########################################################

# Screen the by SATB range:
def voice_range(full_list_result):
    # Container:
    temp_chord = []
    temp_note_midi = []
    screened_result = []
    # Iteration:
    for i in range(len(full_list_result)):
        temp_chord = full_list_result[i]
        for j in range(len(temp_chord)):
            temp_note_midi = midi_num[temp_chord[j]]
            if j == 0 and temp_note_midi in range(midi_num['a2'], midi_num['c4'] + 1):
                temp_note_midi = midi_num[temp_chord[j + 1]] 
                j += 1
                if j == 1 and temp_note_midi in range(midi_num['e3'], midi_num['c5'] + 1):
                    temp_note_midi = midi_num[temp_chord[j + 1]]
                    j += 1
                    if j == 2 and temp_note_midi in range(midi_num['g3'], midi_num['e5'] + 1):
                        temp_note_midi = midi_num[temp_chord[j + 1]]
                        j += 1
                        if j == 3 and temp_note_midi in range(midi_num['c4'], midi_num['b5'] + 1):
                            screened_result.append(temp_chord)
                            break
            else:
                break
    return screened_result

###########################################################

# [FIRST CHORD ONLY] Remove the chord have doubles:
def remove_double(screened_result):
    # Container:
    temp_chord = []
    screened_result_2 = []
    # Iteration:
    for i in range(len(screened_result)):
        temp_chord = screened_result[i]
        if len(temp_chord) == len(set(temp_chord)):
            screened_result_2.append(temp_chord)
        else:
            continue
    return screened_result_2

###########################################################

# [FIRST CHORD ONLY] Select the good chords:
def ideal_chord(screened_result_2):
    temp_chord = []
    good_chord = []
    # Set up the dict:
    good_chord_distance = {
        'third', 'fourth', 'fifth', 'sixth'
    }
    # Iteration:
    for i in range(len(screened_result_2)):
        temp_chord = screened_result_2[i]
        if distance(str(temp_chord[1]), str(temp_chord[2])) in good_chord_distance:
            if distance(str(temp_chord[2]), str(temp_chord[3])) in good_chord_distance:
                good_chord.append(temp_chord)
        else:
            continue
    return good_chord

###########################################################

# [FIRST CHORD ONLY] Distinguish the open and close spacing:
def find_structure(good_chord):
    temp_chord = []
    close_chord = []
    open_chord = []
    # Iteration:
    for i in range(len(good_chord)):
        temp_chord = good_chord[i]
        if distance(temp_chord[1], temp_chord[3]) in close_dict:
            close_chord.append(temp_chord)
        else:
            open_chord.append(temp_chord)
    return close_chord, open_chord

###########################################################

# [FIRST CHORD ONLY] Select the starting chord:
def start_chord(good_chord):
    first_chord = random.choice(good_chord)
    return first_chord

###########################################################