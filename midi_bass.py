import time
import random
import rtmidi
import musx
from musx import keynum

from main_multi_solution import main
from midi_chord import flatten_list

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
# chord_progression = main()[0] * 4

def get_bass_line(chord_progression):
    chord_progression = flatten_list(chord_progression)
    bass_line = []
    for chord in chord_progression:
        bass_line.append(chord[0])
    return bass_line

def bass_line_maker(chord_progression):
    bass_line = get_bass_line(chord_progression)
    for note in bass_line:
        key = note
        vel = musx.pick(40, 50, 60)
        dur = 4
        print(f"bass line: {key} vel: {vel}")
        midiout.send_message(musx.note_on(6, key, vel))
        time.sleep(dur)
        midiout.send_message(musx.note_off(6, key, vel))
    # Test:
    print("\nAll done!\n")
    # set midi synth back to piano
    midiout.send_message(musx.program_change(0, 0))

if __name__ == '__main__':
    bass_line_maker(chord_progression)