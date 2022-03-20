import sys, re
from unittest import result
# from input_check import getNotes
from interval_dict import key_dict, interval_dict, key_dict_extend
from interval_dict import midi_dict, benchmark_dict, octave_dict
from interval_dict import major_quality_dict, perfect_quality_dict, input_dict_2

def interval(low_note, top_note):

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
            print('\n' + 'Oops, incomplete octave register assignemt. Please try it again.' + '\n')
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

    # Return error message if low note is higher than top note in same register:
    if low_register == top_register:
        if low > top:
            print('\n' + 'Oops, invalid input. Please try it again.' + '\n')
            sys.exit()

    # Return the error message if the low note register is higher the top note:
    if low_register > top_register:
        print('\n' + 'Oops, invalid register input. Please try it again.' + '\n')
        sys.exit()

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
    difference = (semi_distance % 12) - benchmark
    if benchmark == 12 and input_dict_2[low_note[:-1]] <= input_dict_2[top_note[:-1]]:
        difference = difference + 12

    # Test:
    # print('difference from benchmark: ' + str(difference))

    # Get the result:
    if benchmark == 0 and difference == 0:  # Unison
        # print('\n' + 'result: perfect unison' + '\n')
        result = 'perfect unison'
    elif benchmark == 0:    # Unison Variant
        # print(f'\nresult: {perfect_quality_dict[difference]} unison\n')
        # result = f'{perfect_quality_dict[difference]} unison'
        result = 'unison'
    elif benchmark == 12 and difference == 0:   # Octave
        # print(f'\nresult: {octave_dict[semi_distance / 12]}perfect octave\n')
        result = 'perfect octave'
    elif benchmark == 12:   # Octave Variant
        # print(f'\nresult: {perfect_quality_dict[difference]} {distance} ({perfect_quality_dict[difference]} octave)\n')
        result = f'{perfect_quality_dict[difference]}'
    elif benchmark in [2, 4, 9, 11] and temp_distance <= 7:  # Major interval
        # print(f'\nresult: {major_quality_dict[difference]} {distance}\n')
        result = f'{major_quality_dict[difference]} {distance}'
    elif benchmark in [2, 4, 9, 11]:    # Compound major interval
        # print(f'\nresult: {major_quality_dict[difference]} {distance} ({major_quality_dict[difference]} {interval_dict[temp_distance % 7]})\n')
        result = f'{major_quality_dict[difference]} {interval_dict[temp_distance % 7]}'
    elif benchmark in [5, 7] and temp_distance <= 7:   # Perfect interval
        # print(f'\nresult: {perfect_quality_dict[difference]} {distance}\n')
        result = f'{perfect_quality_dict[difference]} {distance}'
    elif benchmark in [5, 7]:   # Compound perfect interval
        # print(f'\nresult: {perfect_quality_dict[difference]} {distance} ({perfect_quality_dict[difference]} {interval_dict[temp_distance % 7]})\n')
        result = f'{perfect_quality_dict[difference]} {interval_dict[temp_distance % 7]}'
    else:   # Error message
        # print('\n' + 'Oops, there is an error. Please try it again.' + '\n')
        result = 'Oops, there is an error. Please try it again.'
    return result

if __name__ == '__main__':
    interval('d4', 'd5')
    interval('d4', 'd7')
    interval('d', 'a')
    interval('d4', 'a7')