from harmonizer import get_input, get_bass_line, chord_quality_scheme
from harmonizer import spell_chord, note_combination
from combination import note_range_zip, ascending_order, voice_range, remove_double
from combination import ideal_chord, find_structure, start_chord
from voicing import check_same_direction, check_voice_overlap
from voicing import check_direct_motion, check_parallel_motion
from voicing import count_step, error_check, error_check_lite

import harmonizer_dict
import random

from interval_def import interval
from distance_def import distance
from step_def import step

from harmonizer_dict import note_accidental_range_to_midi as midi_num
from harmonizer_dict import close_structure_dict as close_dict
from harmonizer_dict import pre_assign_register as pre

def main():
    # Output container:
    chord_progression = []
    # harmonizer functions:
    bass_line = get_input('\n' + 'Hello, please enter the bass line and separate by space: ')
    # print(bass_line)
    bass_line_result = get_bass_line(bass_line)
    # print(bass_line_result)
    scheme = chord_quality_scheme(bass_line)
    chord_select = scheme[0]
    chord_scheme = scheme[1]
    print('\nchord_select: ' + str(chord_select))
    print('\nchord_scheme: ' + str(chord_scheme))
    all_chord_result = spell_chord(bass_line, chord_select)
    print('\nall_chord_result: ' + str(all_chord_result))
    all_combination = note_combination(all_chord_result)
    # print(all_combination)
    # combination functions:
    register = pre
    for i in range(len(all_combination)):
        chord = all_combination[i]
        full_list = note_range_zip(chord, register)
        # print(full_list)
        full_list_result = ascending_order(full_list)
        # print(full_list_result)
        screened_result = voice_range(full_list_result)
        print('\nscreened_result: ' + str(screened_result))
        if i == 0:
            screened_result_2 = remove_double(screened_result)
            # print(screened_result_2)
            good_chord = ideal_chord(screened_result_2)
            # print(good_chord)
            close_chord = find_structure(good_chord)[0]
            # print(close_chord)
            open_chord = find_structure(good_chord)[1]
            # print(open_chord)
            first_chord = start_chord(good_chord)
            print('\nfirst_chord: ' + str(first_chord))
            chord_progression.append(first_chord)
            continue
        else:
            screened_result_2 = remove_double(screened_result)
            # print(screened_result_2)
            good_chord = ideal_chord(screened_result_2)
            # print(good_chord)
        # voicing function:
        candidate_chord = []
        for j in range(len(screened_result)):
            connection = [chord_progression[-1], screened_result[j]]
            if error_check_lite(connection) == True:
                candidate_chord.append(screened_result[j])
        print('\ncandidate_chord:' + str(candidate_chord))
        print(len(candidate_chord))
        # Get the next chord:
        if len(candidate_chord) > 1:
            temp_best = candidate_chord[0]
            list = candidate_chord
        else:
            temp_best = good_chord[0]
            list = good_chord
        previous_chord = chord_progression[-1]
        for k in range(1, len(list)):
            if count_step(previous_chord, list[k]) < count_step (previous_chord, temp_best):
                temp_best = list[k]
        chord_progression.append(temp_best)
    print('\nchord_progression: ' + str(chord_progression) + '\n')
    return chord_progression

if __name__ == '__main__':
    main()