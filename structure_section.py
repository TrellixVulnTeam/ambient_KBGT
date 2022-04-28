import random
from timeit import default_timer as timer
from functools import reduce
from midi_chord import flatten_list
from midi_ornament import get_pool
from main_multi_solution import main
from structure_macro import get_duration, get_section

chord_progression = [
    [['c3', 'g3', 'eb4', 'bb4'], ['c3', 'c4', 'd4', 'g4'], ['g3', 'b3', 'd4', 'g4']], 
    [['c3', 'g4', 'eb5', 'bb5'], ['c3', 'c5', 'd5', 'g5'], ['g3', 'b4', 'd5', 'g5']], 
    [['c3', 'bb3', 'g4', 'eb5'], ['g3', 'd4', 'b4', 'g5']]
]
# chord_progression = main()[0]

def get_section_dur(total_dur, paragraph, average, minimum, maximum):
    while True:
        if isinstance(average, int):
            list = [random.randint(minimum, maximum) for i in range(paragraph)]
        if isinstance(average, float):
            list = [round(random.uniform(minimum, maximum), 1) for i in range(paragraph)]
        current_average = reduce(lambda x, y: x + y, list) / len(list)
        if current_average == average and sum(list) == total_dur:
            return list

def get_section_chord(list, chord_progression):
    section_chord = []
    chord = flatten_list(chord_progression)
    # print(chord)
    if len(list) <= len(chord):
        section_chord = chord[:len(list)]
    else:
        section_chord = chord*(len(list)//len(chord))+chord[:len(list)%len(chord)]
    return section_chord

def pool_tailer(list, chord_progession):
    temp_pool = get_pool(chord_progression)
    if len(list) <= len(temp_pool):
        return temp_pool[:len(list)]
    else:
        return temp_pool*(len(list)//len(temp_pool))+temp_pool[:len(list)%len(temp_pool)]

def get_flatten_list(list):
    output = []
    for i in range(len(list)):
        sub_list = list[i]
        for j in range(len(sub_list)):
            output.append(sub_list[j])
    return output

def get_time_frame(total_sec):
    total_time_frame = []
    for i in range(len(total_sec)):
        sec_time_frame = total_sec[i]
        for j in range(len(sec_time_frame)):
            temp_time_frame = []
            total_dur = sec_time_frame[j]
            if j == 0 or j == len(sec_time_frame) - 1:
                paragraph = random.randint(3, 6)
            else:
                if sec_time_frame[j] >= 120: paragraph = random.randint(12, 20)
                elif 120 > sec_time_frame[j] >= 60: paragraph = random.randint(8, 12)
                else: paragraph = random.randint(4, 8)
            average = total_dur / paragraph
            minimum, maximum = average * 0.5, average * 2
            temp_time_frame = get_section_dur(total_dur, paragraph, average, minimum, maximum)
            total_time_frame.append(temp_time_frame)
    return total_time_frame

def get_chord(total_time_frame, chord_progression):
    total_chord = []
    for list in total_time_frame:
        section_chord = get_section_chord(list, chord_progression)
        total_chord.append(section_chord)
    return total_chord

def get_all_pool(total_time_frame, chord_progression):
    total_pool = []
    for list in total_time_frame:
        section_pool = pool_tailer(list, chord_progression)
        total_pool.append(section_pool)
    return total_pool

if __name__ == '__main__':
    paragraph = random.randint(5, 8); print('\nparagraph:', str(paragraph))
    total_time = get_duration(paragraph, 10, 8, 12); print('total_paragraph:', str(total_time), str(sum(total_time)), '\n')
    section = get_section(total_time); print('section:', section[1], len(section[1]),'\n\ntotal_sec:', section[2], len(section[2]), '\n')
    # list = get_section_dur(42, 7, 6, 3, 15); print(list, len(list))
    # chord = get_section_chord(list, chord_progression); print(chord, len(chord))
    start = timer()
    total_section = get_flatten_list(section[1]); print('total_section:', total_section, len(total_section), '\n')
    total_time_frame = get_time_frame(section[2]); print('total_time_frame:', total_time_frame, len(total_time_frame), '\n')
    total_chord = get_chord(total_time_frame, chord_progression); print('total_chord:', total_chord, len(total_chord), '\n')
    total_pool = get_all_pool(total_time_frame, chord_progression); print('total_pool:', total_pool, len(total_pool))
    end = timer(); print('\nRunning time:', str(round((end - start), 2)) + 's\n')