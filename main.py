from harmonizer import get_input, get_bass_line, chord_quality_scheme
from harmonizer import spell_chord, note_combination
from combination import note_range_zip, ascending_order, voice_range, sat_octave
from combination import remove_double, ideal_chord, find_structure, start_chord
from voicing import count_step, error_check_lite, error_check

from harmonizer_dict import pre_assign_register as pre

def main():
    # Output container:
    chord_progression = []
    # harmonizer functions:
    bass_line = get_input('\n' + 'Hello, please enter the bass line and separate by space: ')
    bass_line_result = get_bass_line(bass_line)
    scheme = chord_quality_scheme(bass_line)
    chord_select = scheme[0]
    chord_scheme = scheme[1]
    all_chord_result = spell_chord(bass_line, chord_select)
    all_combination = note_combination(all_chord_result)
    # combination functions:
    register = pre
    for i in range(len(all_combination)):
        chord = all_combination[i]
        full_list = note_range_zip(chord, register)
        full_list_result = ascending_order(full_list)
        screened_result = voice_range(full_list_result)
        legal_chord = sat_octave(screened_result)
        if i == 0:
            screened_result_2 = remove_double(screened_result)
            good_chord = ideal_chord(screened_result_2)
            close_chord = find_structure(good_chord)[0]
            open_chord = find_structure(good_chord)[1]
            first_chord = start_chord(good_chord)
            chord_progression.append(first_chord)
            continue
        else: # ???
            screened_result_2 = remove_double(screened_result)
            good_chord = ideal_chord(screened_result_2)
        # voicing function:
        candidate_chord = []
        for j in range(len(legal_chord)):
            connection = [chord_progression[-1], legal_chord[j]]
            if error_check_lite(connection) == True:
                candidate_chord.append(legal_chord[j])
        # Get the next chord:
        if len(candidate_chord) > 1:
            temp_best = candidate_chord[0]
            list = candidate_chord
        else:
            temp_best = legal_chord[0]
            list = legal_chord
        previous_chord = chord_progression[-1]
        for k in range(1, len(list)):
            if count_step(previous_chord, list[k]) < count_step (previous_chord, temp_best):
                temp_best = list[k]
        chord_progression.append(temp_best)
    print('\nbass_line_result: ' + str(bass_line_result))
    print('\nchord_scheme: ' + str(chord_scheme))
    print('\ngood_chord: ' + str(good_chord))
    print('\nchord_progression: ' + str(chord_progression) + '\n')
    return chord_progression, bass_line_result

if __name__ == '__main__':
    main()