import time
import random
import threading
import rtmidi
import musx
from musx import keynum

from main_multi_solution import main
from midi_chord import pad_maker
from midi_ornament import ornament_maker

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
] * 10
chord_progression = main()[0] * 10

# Threading:
pad = threading.Thread(target=pad_maker, args=[chord_progression])
ornaments = threading.Thread(target=ornament_maker, args=[chord_progression])

# Call the variables:
pad.start()
ornaments.start()