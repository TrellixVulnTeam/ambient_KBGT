# from input_check import getNotes
import sys, re
from interval_dict import key_dict, interval_dict, key_dict_extend
from interval_dict import midi_dict, benchmark_dict, input_dict_2, semitone_dict
# from interval_dict import major_quality_dict, perfect_quality_dict, octave_dict

def distance(low_note, top_note):

    # Exchange the note is low note is higher than top note:
    if midi_dict[low_note] > midi_dict[top_note]:
        low_note = top_note
        top_note = low_note

    # Get letter corresponding number:
    low = key_dict[low_note[0]]
    top = key_dict[top_note[0]]

    # Check if the inputs contains the octave:
    low_contains_register = any(map(str.isdigit, low_note))
    top_contains_register = any(map(str.isdigit, top_note))

    # Test: 
    # print('\n' + 'if low contains digit: ' + str(low_contains_register))
    # print('if top contains digit: ' + str(top_contains_register))

    # Return error message if only one octave register is assigned:
    if low_contains_register == False or top_contains_register == False:
        if low_contains_register == True or top_contains_register == True:
            print('\n' + '(distance_def_1) Oops, incomplete octave register assignemt. Please try it again.' + '\n')
            sys.exit()

    # If the input has no digit, assign default octave register:
    if low_contains_register == False and top_contains_register == False:
        if low > top:
            low_note = low_note + '4'
            top_note = top_note + '5'
        else:
            low_note = low_note + '4'
            top_note = top_note + '4'

    # Test:
    # print('low note w/ register: ' + low_note)
    # print('top note w/ register: ' + top_note)

    # Get the register:
    low_register = int(re.findall(r'\d+', low_note)[0])
    top_register = int(re.findall(r'\d+', top_note)[0])

    # Get the note without register:
    low_no_register = low_note[0:-1]
    top_no_register = top_note[0:-1]

    # Return unison if actual pitch is same but with different name:
    if low_register == top_register:
        # if semitone_dict[low_no_register] > semitone_dict[top_no_register]:
        #     print('\n' + '(distance_def_2) Oops, invalid input. Please try it again.' + '\n')
        #     sys.exit()
        if low > top and semitone_dict[low_no_register] == semitone_dict[top_no_register]:
            result = 'unison'
            return result

    # Return the error message if the low note register is higher the top note:
    # if low_register > top_register:
    #     print('\n' + '(distance_def_3) Oops, invalid register input. Please try it again.' + '\n')
    #     sys.exit()

    # Pre-process the notes with accidentals:
    low_note_natural = low_note[0] + low_note[-1]
    top_note_natural = top_note[0] + top_note[-1]

    # Test:
    # print('low note w/o accidentals:' + low_note_natural)
    # print('top note w/o accidentals:' + top_note_natural) 

    # Get the distance:
    temp_distance = key_dict_extend[top_note_natural] - key_dict_extend[low_note_natural]
    if temp_distance <= 7:
        distance = interval_dict[temp_distance]
    else:
        distance = str(temp_distance + 1) + 'th'

    # Test:
    # print('temporary distance: ' + str(temp_distance))
    # print('\n' + 'interval distance: ' + distance)

    # According to midi note dict, get the corresponding index:
    low_note_midi = midi_dict[low_note]
    top_note_midi = midi_dict[top_note]

    # Test:
    # print('\n' + 'low note midi index: ' + str(low_note_midi))
    # print('top note midi index: ' + str(top_note_midi))

    # Get the semitone distance:
    semi_distance = top_note_midi - low_note_midi

    # Test:
    # print('semitone distance: ' + str(semi_distance))

    # Get the benchmark semitone distance:
    if low_note[0] == top_note[0] and low_register != top_register:
        benchmark = benchmark_dict[interval_dict[7]]
    else:
        benchmark = benchmark_dict[interval_dict[temp_distance % 7]]

    # Test:
    # print('benchmark semitone: ' + str(benchmark))

    # Get the difference between the interval and benchmark:
    if distance in ['unison', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh']:
        difference = semi_distance - benchmark
    else:
        difference = (semi_distance % 12) - benchmark
    if benchmark == 12 and input_dict_2[low_note[:-1]] <= input_dict_2[top_note[:-1]]:
        difference = difference + 12

    # Test:
    # print('difference from benchmark: ' + str(difference))

    return distance

if __name__ == '__main__':
    print(distance('f5', 'b5'))
    print(distance('d4', 'c5'))
    print(distance('g3', 'a4'))
    print(distance('eb4', 'd#4'))