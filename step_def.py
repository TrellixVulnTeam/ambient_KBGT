import sys, re
from interval_dict import key_dict, key_dict_extend
# from interval_dict import midi_dict, benchmark_dict, octave_dict, interval_dict
# from interval_dict import major_quality_dict, perfect_quality_dict, input_dict_2

def step(low_note, top_note):

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
            print('\n' + '(step_def) Oops, incomplete octave register assignemt. Please try it again.' + '\n')
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
            print('\n' + '(step_def) Oops, invalid input. Please try it again.' + '\n')
            sys.exit()

    # Return the error message if the low note register is higher the top note:
    if low_register > top_register:
        print('\n' + '(step_def) Oops, invalid register input. Please try it again.' + '\n')
        sys.exit()

    # Pre-process the notes with accidentals:
    low_note_natural = low_note[0] + low_note[-1]
    top_note_natural = top_note[0] + top_note[-1]

    # Test:
    # print('low note w/o accidentals:' + low_note_natural)
    # print('top note w/o accidentals:' + top_note_natural) 

    # Get the distance:
    temp_distance = key_dict_extend[top_note_natural] - key_dict_extend[low_note_natural]

    return temp_distance

if __name__ == '__main__':
    print(step('f5', 'b5'))
    print(step('d4', 'c5'))
    print(step('g3', 'a4'))
