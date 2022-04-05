from harmonizer import get_input, get_bass_line, chord_quality_scheme
from harmonizer import spell_chord, note_combination
from combination import note_range_zip, ascending_order, voice_range, sat_octave
from combination import remove_double, ideal_chord, find_structure, start_chord
from voicing import count_step, error_check_lite, rate_and_sort, error_check

from harmonizer_dict import pre_assign_register as pre

from timeit import default_timer as timer

def main():
    # Output container:
    legal_answer = []
    temp_progression = []
    chord_progression = []
    # harmonizer functions:
    bass_line = get_input('\n' + 'Hello, please enter the bass line and separate by space: ')
    # bass_line = ['c#', 'c#', 'gb', 'gb', 'ab', 'ab', 'g#', 'f#', 'fb', 'eb', 'e#', 'd#', 'db', 'c#', 'g#', 'gb', 'f#', 'fb', 'e#', 'eb', 'db', 'g#', 'gb', 'f#', 'fb', 'eb', 'eb', 'd']
    # Start the timer: 
    start = timer()
    # harmonizer functions:
    bass_line_result = get_bass_line(bass_line)
    # bass_line_result = ['c#3', 'c#3', 'gb3', 'gb3', 'ab3', 'ab3', 'g#3', 'f#3', 'fb3', 'eb3', 'e#3', 'd#3', 'db3', 'c#3', 'g#2', 'gb2', 'f#2', 'fb2', 'e#2', 'eb2', 'db2', 'g#2', 'gb2', 'f#2', 'fb2', 'eb2', 'eb2', 'd2']
    # print('\nbass_line_result: ' + str(bass_line_result))
    # print(len(bass_line_result))
    scheme = chord_quality_scheme(bass_line)
    chord_select = scheme[0]
    # chord_select = ['m7', 'maj7', 'sus4', 'sus2', 'maj7', '', 'sus2', 'maj7', '', 'sus4', 'maj7', 'sus2', 'm7', 'sus4', 'm', 'sus4', 'm7', 'sus2', 'm7', 'm', 'sus4', '', 'm7', 'sus2', 'maj7', 'sus2', '', 'sus2']
    chord_scheme = scheme[1]
    # chord_scheme = ['C#m7', 'C#maj7', 'Gbsus4', 'Gbsus2', 'Abmaj7', 'Ab', 'G#sus2', 'F#maj7', 'Fb', 'Ebsus4', 'E#maj7', 'D#sus2', 'Dbm7', 'C#sus4', 'G#m', 'Gbsus4', 'F#m7', 'Fbsus2', 'E#m7', 'Ebm', 'Dbsus4', 'G#', 'Gbm7', 'F#sus2', 'Fbmaj7', 'Ebsus2', 'Eb', 'Dsus2']
    # print('\nchord_scheme: ' + str(chord_scheme))
    # print(len(chord_scheme))
    all_chord_result = spell_chord(bass_line, chord_select)
    all_combination = note_combination(all_chord_result)
    # print('\nall_combination: ' + str(all_combination))
    # combination functions:
    register = pre
    # Determine the first chord:
    chord = all_combination[0]
    full_list = note_range_zip(chord, register)
    full_list_result = ascending_order(full_list)
    screened_result = voice_range(full_list_result)
    screened_result_2 = remove_double(screened_result)
    good_chord = ideal_chord(screened_result_2)
    # print('\ngood_chord (start_chord): ' + str(good_chord))
    # print(len(good_chord))
    for i in range(len(good_chord)):
        first_chord = good_chord[i]
        # print('\nfirst_chord: ' + str(first_chord))
        temp_progression.append(first_chord)
        for j in range(1, len(all_combination)):
            chord = all_combination[j]
            full_list = note_range_zip(chord, register)
            full_list_result = ascending_order(full_list)
            screened_result = voice_range(full_list_result)
            screened_result_2 = remove_double(screened_result)
            legal_chord = sat_octave(screened_result)
            # voicing function:
            candidate_chord = []
            for k in range(len(legal_chord)):
                connection = [temp_progression[-1], legal_chord[k]]
                if error_check_lite(connection) == True:
                    candidate_chord.append(legal_chord[k])
            # print('candidate_chord: ' + str(candidate_chord))
            # Get the next chord:
            if len(candidate_chord) != 0:
                temp_best = candidate_chord[0]
                list = candidate_chord
            else:
                i += 1
                j += 1
                # print(f'{first_chord} have no candidate connection')
                # print('incomplete progression: ' + str(temp_progression))
                # print(len(temp_progression))
                temp_progression = []
                break    
            previous_chord = temp_progression[-1]
            for k in range(1, len(list)):
                if count_step(previous_chord, list[k]) < count_step (previous_chord, temp_best):
                    temp_best = list[k]
            temp_progression.append(temp_best)
        # if len(temp_progression) != 0:
            # print('temp_progression: ' + str(temp_progression))
        if len(temp_progression) == len(chord_scheme):
            # chord_progression.append(temp_progression)
            legal_answer.append(temp_progression)
            temp_progression = []
    # print('\nlegal_answer: ' + str(legal_answer))
    print(len(legal_answer))
    sorted_answer = rate_and_sort(legal_answer)
    # print('\nsorted_answer: ' + str(sorted_answer)) 
    # print(len(sorted_answer))
    # print(f'\ntry {len(good_chord)} times, {len(legal_answer)} solutions found!')
    # End the timer:
    end = timer()
    print('\nRunning time:', str((end - start) * 1000) + ' ms')
    return sorted_answer, bass_line_result, good_chord, chord_scheme

if __name__ == '__main__':
    main()