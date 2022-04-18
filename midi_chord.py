import time
import rtmidi
import musx
from musx import keynum
from main_multi_solution import main

# MIDI port set up:
midiout = rtmidi.MidiOut()
outports = midiout.get_ports()
midiout.open_port(outports.index('IAC Driver Bus 1'))
midiout.is_port_open()

# Define the melody:
chord_progression = [
    [['c3', 'g3', 'eb4', 'bb4'], ['c3', 'c4', 'd4', 'g4'], ['g3', 'b3', 'd4', 'g4']], 
    [['c3', 'g4', 'eb5', 'bb5'], ['c3', 'c5', 'd5', 'g5'], ['g3', 'b4', 'd5', 'g5']], 
    [['c4', 'g4', 'eb5', 'bb5'], ['c4', 'c5', 'd5', 'g5'], ['g3', 'b4', 'd5', 'g5']], 
    [['c3', 'g4', 'bb4', 'eb5'], ['c3', 'd4', 'c5', 'g5'], ['g3', 'd4', 'b4', 'g5']], 
    [['c4', 'g4', 'bb4', 'eb5'], ['c3', 'd4', 'c5', 'g5'], ['g3', 'd4', 'b4', 'g5']], 
    [['c3', 'bb3', 'g4', 'eb5'], ['c3', 'd4', 'c5', 'g5'], ['g3', 'd4', 'b4', 'g5']]
] * 100
# chord_progression = main()[0] * 100

# Function to flatten the chord_progression:
def flatten_list(chord_progression):
    return keynum([item for sublist in chord_progression for item in sublist])

def pad_maker(chord_progression):
    # Flatten the chord_progression:
    melody = flatten_list(chord_progression)
    # Loop through the pool:
    for i in range(len(melody)):
        # Pick a random midi key number:
        key_1, key_2, key_3, key_4 = melody[i][0]-12, melody[i][1]-12, melody[i][2]-12, melody[i][3]-12
        # Pick a random duration:
        dur = 4
        # dur = musx.pick(0.5, 0.6, 0.7, 0.8)
        vel = musx.pick(20, 40, 50, 70)
        # Send it out:
        print(f"\nchord {i+1}, key: {key_1}, {key_2}, {key_3}, {key_4}, dur: {dur}, vel: {vel}")
        midiout.send_message(musx.note_on(1, key_1, vel))
        midiout.send_message(musx.note_on(1, key_2, vel))
        midiout.send_message(musx.note_on(1, key_3, vel))
        midiout.send_message(musx.note_on(1, key_4, vel))
        # Wait for duration:
        time.sleep(dur)
    # Test:
    print("\nAll done!\n")
    # set midi synth back to piano
    midiout.send_message(musx.program_change(0, 0))

if __name__ == "__main__":
    pad_maker(chord_progression)

# Test:
# print('\nflatten_chord_progression: ' + str(melody))
# print(len(melody))

# Control the player:
# command = input('\nContinue? (y/n) ')
# if command == 'y':
#     control = True
# else:
#     sys.exit()

# Real time MIDI output:
# if control == True: