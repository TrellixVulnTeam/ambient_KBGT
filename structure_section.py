import random
from functools import reduce
from midi_chord import flatten_list
from main_multi_solution import main

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
    intro_chord = []
    chord = flatten_list(chord_progression)
    # print(chord)
    if len(list) <= len(chord):
        intro_chord = chord[:len(list)]
    else:
        intro_chord = chord*(len(list)//len(chord))+chord[:len(list)%len(chord)]
    return intro_chord

if __name__ == '__main__':
    list = get_section_dur(42, 7, 6, 3, 15); print(list, len(list))
    chord = get_section_chord(list, chord_progression); print(chord, len(chord))
