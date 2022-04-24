import time
import random
import rtmidi
import musx
import threading
from musx import keynum
from main_multi_solution import main
from structure_section import get_section_dur, get_section_chord, pool_tailer

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

total_dur = 36
paragraph = 9
list = get_section_dur(total_dur, paragraph, 4, 3, 10)
chord = get_section_chord(list, chord_progression)
pool = pool_tailer(list, chord_progression)

print('\n', list, len(list), '\n')
print(chord, len(chord), '\n')
print(pool, len(pool))

def intro_pad(list, chord):
    # Send the pad:
    for i in range(len(chord)):
        key_1, key_2, key_3, key_4 = chord[i][0], chord[i][1], chord[i][2], chord[i][3]
        dur, vel = list[i], musx.pick(30, 40, 50)
        print(f"\nmeasure {i+1}, key: {key_1}, {key_2}, {key_3}, {key_4}, dur: {dur}, vel: {vel}")
        midiout.send_message(musx.note_on(1, key_1, vel)); time.sleep(round(random.random(), 2))
        midiout.send_message(musx.note_on(2, key_2, vel)); time.sleep(round(random.random(), 2))
        midiout.send_message(musx.note_on(3, key_3, vel)); time.sleep(round(random.random(), 2))
        midiout.send_message(musx.note_on(4, key_4, vel)); time.sleep(dur)
        midiout.send_message(musx.note_off(1, key_1, vel)); time.sleep(round(random.random(), 2))
        midiout.send_message(musx.note_off(2, key_2, vel)); time.sleep(round(random.random(), 2))
        midiout.send_message(musx.note_off(3, key_3, vel)); time.sleep(round(random.random(), 2))
        midiout.send_message(musx.note_off(4, key_4, vel))

def intro_note(list, pool):
    # Send the note:
    for i in range(len(pool)):
        note_select = random.choice([2, 3, 4])
        for j in range(note_select):
            note = keynum(random.choice(pool[i]))
            vel = musx.pick(40, 50, 70)
            dur = round(list[i]/note_select, 2)
            print(f"note {i+1}, note: {note}, dur: {dur}, vel: {vel}")
            midiout.send_message(musx.note_on(5, note, vel))
            time.sleep(dur)

# if __name__ == "__main__":
#     intro_pad(list, chord)
#     intro_note(list, pool)

pad = threading.Thread(target=intro_pad, args=[list, chord])
note = threading.Thread(target=intro_note, args=[list, pool])

pad.start()
note.start()