import rtmidi
import random
import threading
from timeit import default_timer as timer
from musx import keynum
from main_multi_solution import main
from structure_macro import get_duration, get_section
from structure_section import get_flatten_list, get_time_frame, get_chord, get_all_pool

# MIDI port set up:
midiout = rtmidi.MidiOut()
outports = midiout.get_ports()
midiout.open_port(outports.index('IAC Driver Bus 1'))
midiout.is_port_open()

# Define the chord_progression:
chord_progression = [
    [['c3', 'g3', 'eb4', 'bb4'], ['c3', 'c4', 'd4', 'g4'], ['g3', 'b3', 'd4', 'g4']], 
    [['c3', 'g4', 'eb5', 'bb5'], ['c3', 'c5', 'd5', 'g5'], ['g3', 'b4', 'd5', 'g5']], 
    [['c4', 'g4', 'eb5', 'bb5'], ['c4', 'c5', 'd5', 'g5'], ['g3', 'b4', 'd5', 'g5']], 
    [['c3', 'g4', 'bb4', 'eb5'], ['c3', 'd4', 'c5', 'g5'], ['g3', 'd4', 'b4', 'g5']], 
    [['c4', 'g4', 'bb4', 'eb5'], ['c3', 'd4', 'c5', 'g5'], ['g3', 'd4', 'b4', 'g5']], 
    [['c3', 'bb3', 'g4', 'eb5'], ['c3', 'd4', 'c5', 'g5'], ['g3', 'd4', 'b4', 'g5']]
] * 4
# chord_progression = main()[0] * 10

paragraph = random.randint(5, 8); print('\nparagraph:', str(paragraph))
total_time = get_duration(paragraph, 10, 8, 12); print('total_paragraph:', str(total_time), str(sum(total_time)), '\n')
section = get_section(total_time); print('section:', section[1], len(section[1]),'\n\ntotal_sec:', section[2], len(section[2]), '\n')
start = timer()
total_section = get_flatten_list(section[1]); print('total_section:', total_section, len(total_section), '\n')
total_time_frame = get_time_frame(section[2]); print('total_time_frame:', total_time_frame, len(total_time_frame), '\n')
total_chord = get_chord(total_time_frame, chord_progression); print('total_chord:', total_chord, len(total_chord), '\n')
total_pool = get_all_pool(total_time_frame, chord_progression); print('total_pool:', total_pool, len(total_pool))
end = timer(); print('\nRunning time:', str(round((end - start), 2)) + 's\n')