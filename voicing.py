from unittest import result
from harmonizer_dict import note_accidental_range_to_midi as midi_num
from harmonizer_dict import pre_assign_register as pre
from harmonizer_dict import close_structure_dict as close_dict
from interval_def import interval
from step_def import step

###########################################################

# Error check 1: four voices move in same direction
def check_same_direction(connection):
    this_chord = connection[0]
    next_chord = connection[1]
    direction = []
    # Get the list of difference by each note:
    for i in range(len(connection[0])):
        this_note = this_chord[i]
        next_note = next_chord[i]
        difference = midi_num[next_note] - midi_num[this_note]
        direction.append(difference)
    # Check if all the elements are positive/negative:
    ascending = [num for num in direction if num > 0]
    descending = [num for num in direction if num < 0]
    # Get the result:
    if len(ascending) == len(direction) or len(descending) == len(direction):
        result = True
    else:
        result = False
    # print(result
    return result

###########################################################

# Error check 2: voice overlap
def check_voice_overlap(connection):
    this_chord = connection[0]
    next_chord = connection[1]
    if midi_num[next_chord[0]] < midi_num[this_chord[1]]:
        if midi_num[this_chord[0]] < midi_num[next_chord[1]] < midi_num[this_chord[2]]:
            if midi_num[this_chord[1]] < midi_num[next_chord[2]] < midi_num[this_chord[3]]:
                if midi_num[this_chord[2]] < midi_num[next_chord[3]]:
                    result = False
                else: 
                    result = True
            else:
                result = True
        else:
            result = True
    else:
        result = True
    # print(result)
    return result

###########################################################

# Error check 3: direct (hidden) 5th/8ve:
def check_direct_motion(connection):
    this_chord = connection[0]
    next_chord = connection[1]
    stepwise_check = ['minor second', 'major second']
    direct_motion_check = ['perfect unison', 'perfect octave', 'perfect fifth']
    # Pre-process the low note and top note:
    if midi_num[this_chord[3]] <= midi_num[next_chord[3]]:
        low_note = this_chord[3]
        top_note = next_chord[3]
    else:
        low_note = next_chord[3]
        top_note = this_chord[3]
    # Check the soprano voice leading (stepwise):
    if interval(low_note, top_note) in stepwise_check:
        result = False
        return result
    # Check outer voice quality:
    direction = [midi_num[next_chord[0]] - midi_num[this_chord[0]], midi_num[next_chord[3]] - midi_num[this_chord[3]]]
    ascending = [num for num in direction if num > 0]
    descending = [num for num in direction if num < 0]
    # Outer voices move in same direction:
    if len(ascending) == len(direction) or len(descending) == len(direction):
        if interval(next_chord[0], next_chord[3]) in direct_motion_check:
            result = True
        else:
            result = False
    else:
        result = False
    # print(result)
    return result

###########################################################

# Error check 4: Parallel 1st/5th/8ve
def check_parallel_motion(connection):
    this_chord = connection[0]
    next_chord = connection[1]
    parallel_motion_check = ['perfect unison', 'perfect fifth', 'perfect octave']
    # Pointer for low note:
    for i in range(len(this_chord) - 1):
        # Pointer for high note:
        for j in range(i + 1, len(this_chord)):
            if interval(this_chord[i], this_chord[j]) in parallel_motion_check and interval(next_chord[i], next_chord[j]) in parallel_motion_check:
                if interval(this_chord[i], this_chord[j]) == interval(next_chord[i], next_chord[j]):
                    result = True
                    return result
            else:
                continue
    result = False
    # print(result)
    return result

###########################################################

# Rate the progression by counting step in SAT voice:
def count_step(this_chord, next_chord):
    step_list = []
    for i in range(1, len(this_chord)):
        # Pre-process the low note and top note:
        if midi_num[this_chord[i]] <= midi_num[next_chord[i]]:
            low_note = this_chord[i]
            top_note = next_chord[i]
        else:
            low_note = next_chord[i]
            top_note = this_chord[i]
        # Get the step:
        step_list.append(step(low_note, top_note))
    result = sum(step_list)
    # print(result)
    return result

###########################################################

# Combination 1 for error check functions:
def error_check(connection):
    if check_same_direction(connection) == False:
        if check_voice_overlap(connection) == False:
            if check_direct_motion(connection) == False:
                if check_parallel_motion(connection) == False:
                    result = True
                    return result
                else:
                    result = False
            else:
                result = False
        else:
            result = False
    else:
        result = False
    return result

###########################################################

# Combination 2 for error check functions:
def error_check_lite(connection):
    if check_voice_overlap(connection) == False:
        if check_direct_motion(connection) == False:
            if check_parallel_motion(connection) == False:
                result = True
                return result
            else:
                result = False
        else:
            result = False
    else:
        result = False
    return result

###########################################################