from unittest import result
from harmonizer_dict import note_accidental_range_to_midi as midi_num
from harmonizer_dict import pre_assign_register as pre
from harmonizer_dict import close_structure_dict as close_dict
from interval_def import interval
from step_def import step

###########################################################

# Error check 1: four voices move in same direction
def check_same_direction(connection):
    this_chord, next_chord = connection[0], connection[1]
    direction = []
    # Get the list of difference by each note:
    for i in range(len(connection[0])):
        this_note, next_note = this_chord[i], next_chord[i]
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
    this_chord, next_chord = connection[0], connection[1]
    # if midi_num[next_chord[0]] < midi_num[this_chord[1]]:
    if  midi_num[next_chord[0]] < midi_num[this_chord[1]] and \
        midi_num[this_chord[0]] < midi_num[next_chord[1]] < midi_num[this_chord[2]] and \
        midi_num[this_chord[1]] < midi_num[next_chord[2]] < midi_num[this_chord[3]] and \
        midi_num[this_chord[2]] < midi_num[next_chord[3]]:
        result = False
    else:
        result = True
    # print(result)
    return result

###########################################################

# Error check 3: direct (hidden) 5th/8ve:
def check_direct_motion(connection):
    # For Debug:
    # print('def: check_direct_motion')
    this_chord, next_chord = connection[0], connection[1]
    stepwise_check = ['minor second', 'major second']
    direct_motion_check = ['perfect unison', 'perfect octave', 'perfect fifth']
    # Pre-process the low note and top note:
    if midi_num[this_chord[3]] <= midi_num[next_chord[3]]:
        low_note, top_note = this_chord[3], next_chord[3]
    else:
        low_note, top_note = next_chord[3], this_chord[3]
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
    # For Debug:
    # print('def: check_parallel_motion')
    this_chord, next_chord = connection[0], connection[1]
    parallel_motion_check = ['perfect unison', 'perfect fifth', 'perfect octave']
    # Pointer for low note:
    for i in range(len(this_chord) - 1):
        # Pointer for high note:
        for j in range(i + 1, len(this_chord)):
            if  interval(this_chord[i], this_chord[j]) in parallel_motion_check and \
                interval(next_chord[i], next_chord[j]) in parallel_motion_check:
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
            low_note, top_note = this_chord[i], next_chord[i]
        else:
            low_note, top_note = next_chord[i], this_chord[i]
        # Get the step:
        step_list.append(step(low_note, top_note))
    result = sum(step_list)
    # print(result)
    return result

###########################################################

# Combination 1 for error check functions:
def error_check(connection):
    return not (check_same_direction(connection) or check_voice_overlap(connection) or \
                check_direct_motion(connection) or check_parallel_motion(connection))

###########################################################

# Combination 2 for error check functions:
def error_check_lite(connection):
    return not (check_voice_overlap(connection) or check_direct_motion(connection) or \
                check_parallel_motion(connection))

###########################################################

# Count the step and sort the answers in legal_answer:
def rate_and_sort(legal_answer):
    # Container:
    progression_rate = []
    rate_list = []
    # Iteration:
    for i in range(len(legal_answer)):
        for j in range(1, len(legal_answer[i])):
            this_chord, next_chord = legal_answer[i][j-1], legal_answer[i][j]
            chord_rate = count_step(this_chord, next_chord)
            progression_rate.append(chord_rate)
        # print('\nprogression_rate: ' + str(progression_rate))
        temp_rate = sum(progression_rate)
        # print('temp_rate: ' + str(temp_rate))
        progression_rate = []
        rate_list.append(temp_rate)
    # print('\nrate_list: ' + str(rate_list))
    # Combine rate and chord progression into dict:
    rate = dict()
    for k in range(len(rate_list)):
        if rate_list[k] in rate:
            rate[rate_list[k]].append(legal_answer[k])
        else:
            rate[rate_list[k]] = [legal_answer[k]]
    # print('\nrate: ' + str(rate) + '\n' + len(rate))
    # Sort the chord progressions by rate:
    rate_sorted = {key:value for key, value in sorted(rate.items(), key=lambda item: int(item[0]))}
    # print('\nrate_sorted: ' + str(rate_sorted) + '\n' + len(rate_sorted))
    # Extract the value from dict and create a list:
    temp_answer = list(map(list, (chord for chord in rate_sorted.values())))
    # print('\ntemp_answer: ' + str(temp_answer))
    # Flatten the list:
    sorted_answer = [item for sublist in temp_answer for item in sublist]
    return sorted_answer

if __name__ == '__main__':
    rate_and_sort()

###########################################################