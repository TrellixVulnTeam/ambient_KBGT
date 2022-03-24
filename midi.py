import time
import sys
import rtmidi
import musx
from musx import keynum
from main_multi_solution import main
# from main import main

# MIDI port set up:
midiout = rtmidi.MidiOut()
outports = midiout.get_ports()
midiout.open_port(outports.index('IAC Driver Bus 1'))
midiout.is_port_open()

# Define the melody:
chord_progression = main()[0]
# melody = keynum([['a2', 'd4', 'a4', 'e5'], ['d3', 'c#4', 'a4', 'f#5'], ['f3', 'c4', 'a4', 'e5'], ['e3', 'g3', 'b4', 'e5'], ['f3', 'f3', 'ab4', 'c5'], ['b2', 'f#3', 'b4', 'e5'], ['g3', 'b3', 'g4', 'd5'], ['a3', 'b3', 'e4', 'a4'], ['d3', 'c4', 'f4', 'a4'], ['c#3', 'c#4', 'g#4', 'e5'], ['a2', 'b3', 'a4', 'e5'], ['d3', 'g3', 'a4', 'd5'], ['c3', 'g3', 'c4', 'eb4'], ['g3', 'a3', 'd4', 'g4'], ['e3', 'b3', 'e4', 'g4'], ['g3', 'a3', 'd4', 'g4'], ['e3', 'b3', 'e4', 'g4'], ['g3', 'a3', 'd4', 'g4'], ['b2', 'a#3', 'd#4', 'f#4'], ['c3', 'g3', 'c4', 'e4'], ['a2', 'g3', 'c4', 'e4'], ['b2', 'e4', 'b4', 'f#5'], ['c3', 'e4', 'g4', 'c5'], ['c3', 'eb4', 'bb4', 'g5'], ['g3', 'd4', 'b4', 'f#5'], ['e3', 'e4', 'b4', 'g5'], ['g3', 'd4', 'c5', 'g5'], ['e3', 'e4', 'b4', 'a5'], ['g3', 'd4', 'b4', 'g5'], ['b2', 'd4', 'b4', 'f#5'], ['c3', 'c4', 'g4', 'e5'], ['a2', 'e4', 'g#4', 'c#5'], ['b2', 'd4', 'f#4', 'b4'], ['c3', 'eb4', 'g4', 'c5'], ['f3', 'g3', 'c4', 'f4'], ['e3', 'g3', 'e4', 'b4'], ['f3', 'f3', 'c4', 'a4'], ['b2', 'f#3', 'd4', 'b4'], ['g3', 'b3', 'd4', 'g4'], ['a3', 'a3', 'd4', 'e4'], ['d3', 'a3', 'c4', 'f4'], ['c#3', 'e3', 'c#4', 'g#4'], ['a2', 'b3', 'e4', 'a4'], ['d3', 'g3', 'd4', 'a4'], ['f3', 'a3', 'c4', 'f4'], ['e3', 'b3', 'd#4', 'g#4'], ['f3', 'c4', 'eb4', 'ab4'], ['b3', 'b3', 'e4', 'f#4'], ['g3', 'd4', 'f4', 'bb4'], ['a3', 'c4', 'e4', 'a4'], ['d3', 'd4', 'f4', 'a4'], ['c#3', 'e4', 'g#4', 'c#5'], ['a2', 'e4', 'g#4', 'c#5'], ['d3', 'd4', 'g4', 'a4'], ['f3', 'c4', 'e4', 'a4'], ['e3', 'g3', 'e4', 'b4'], ['f3', 'f3', 'c4', 'ab4'], ['b2', 'f#3', 'd4', 'a4'], ['g3', 'bb3', 'd4', 'f4'], ['a2', 'c4', 'e4', 'g4'], ['d3', 'a3', 'c#4', 'f#4'], ['c#3', 'c#4', 'g#4', 'd#5']])

# Flatten the chord_progression:
melody = keynum([item for sublist in chord_progression for item in sublist])
print('\nflatten_chord_progression: ' + str(melody))
print(len(melody))

# Control the player:
command = input('\nContinue? (y/n) ')
if command == 'y':
    control = True
else:
    sys.exit()

# Real time MIDI output:
if control == True:
    for i in range(len(melody)):
        # pick a random midi key number
        key_1 = melody[i][0]
        key_2 = melody[i][1]
        key_3 = melody[i][2]
        key_4 = melody[i][3]
        # pick a random duration
        dur = musx.pick(3, 3.5, 4)
        # dur = musx.pick(0.8, 1.3, 1.6)
        # dur = musx.pick(0.5, 0.6, 0.7, 0.8)
        # send it out
        print(f"chord {i+1}, key: {key_1}, {key_2}, {key_3}, {key_4}, dur: {dur}")
        midiout.send_message(musx.note_on(0, key_1, 80))
        midiout.send_message(musx.note_on(0, key_2, 80))
        midiout.send_message(musx.note_on(0, key_3, 80))
        midiout.send_message(musx.note_on(0, key_4, 80))
        # wait for duration
        time.sleep(dur)
        # stop the note
        midiout.send_message(musx.note_off(0, key_1, 127))
        midiout.send_message(musx.note_off(0, key_2, 80))
        midiout.send_message(musx.note_off(0, key_3, 80))
        midiout.send_message(musx.note_off(0, key_4, 80))

print("\nAll done!\n")

# set midi synth back to piano
midiout.send_message(musx.program_change(0, 0))