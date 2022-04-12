import time
import random
import rtmidi
import musx
from musx import keynum 
from main_multi_solution import main

from harmonizer_dict import note_to_number, number_to_note
from harmonizer_dict import note_accidental_to_semitone as semitone
from harmonizer_dict import semitone_to_accidental as accidental

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
]
# chord_progression = main()[0] * 100

# Generate the pool w/o register:
def spell_pool(chord_progression):
    # Grab the bass note (without register):
    bass_note_list = []
    for i in range(len(chord_progression)):
        progression = chord_progression[i]
        for j in range(len(progression)):
            chord = progression[j]
            bass_note = chord[0][:-1]
            bass_note_list.append(bass_note)
    # Test:
    # print('\nbass_note_list: ' + str(bass_note_list) + '\n' + str(len(bass_note_list)))
    # Get the diatonic spelling:
    diatonic_pool = []
    diatonic_sublist = []
    for i in range(len(bass_note_list)):
        start_note = bass_note_list[i][0]
        start_note_num = note_to_number[start_note]
        diatonic_sublist.append(start_note)
        for number in [1, 2, 4, 5]:
            if start_note_num + number > 7:
                next_note = number_to_note[start_note_num + number - 7]
            else:
                next_note = number_to_note[start_note_num + number]
            diatonic_sublist.append(next_note)
        # print('\ndiatonic_sublist: ' + str(diatonic_sublist) + '\n' + str(len(diatonic_sublist)))
        diatonic_pool.append(diatonic_sublist)
        diatonic_sublist = []
    # Test:
    # print('\ndiatonic_pool: ' + str(diatonic_pool) + '\n' + str(len(diatonic_pool)))
    # Get the chromatic spelling:
    chromatic_pool = []
    chromatic_sublist = []
    benchmark = (2, 4, 7, 9)
    for i in range(len(diatonic_pool)):
        progression = diatonic_pool[i]
        chromatic_sublist.append(progression[0])
        for j in range(1, len(progression)):
            first, latter = progression[0], progression[j]
            if semitone[latter] < semitone[first]:
                difference = benchmark[j-1] - (semitone[latter] + 12 - semitone[first]) 
            else:
                difference = benchmark[j-1] - (semitone[latter] - semitone[first])
            offset = accidental[difference]
            latter = latter + offset
            chromatic_sublist.append(latter)
        # print('\nchromatic_sublist: ' + str(chromatic_sublist) + '\n' + str(len(chromatic_sublist)))
        chromatic_pool.append(chromatic_sublist)
        chromatic_sublist = []
    # Test:
    # print('\nchromatic_pool: ' + str(chromatic_pool) + '\n' + str(len(chromatic_pool)))
    return chromatic_pool

# Assign the pool with register:
def add_register(chromatic_pool):
    pool_register = []
    pool_register_sublist = []
    for i in range(len(chromatic_pool)):
        progression = chromatic_pool[i] * 2
        for j in range(int(len(progression) * 0.5)):
            note = progression[j]
            pool_register_sublist.append(note + '5')
        for k in range(int(len(progression) * 0.5), len(progression)):
            note = progression[k]
            pool_register_sublist.append(note + '6')
        # print('\npool_register_sublist: ' + str(pool_register_sublist) + '\n' + str(len(pool_register_sublist)))
        pool_register.append(pool_register_sublist)
        pool_register_sublist = []
    # Test:
    # print('\npool_register: ' + str(pool_register) + '\n' + str(len(pool_register)))
    return pool_register

# Get the pool:
def get_pool(chord_progression):
    return add_register(spell_pool(chord_progression))

# Send out the MIDI note:
def ornament_maker(chord_progression):
    # Get the pool:
    pool_register = get_pool(chord_progression)
    # Loop through the pool:
    for i in range(len(pool_register)):
        # Assign the note pool:
        note_pool = pool_register[i]
        # Assign the possibility:
        possibility = (1, 1, 1, 1, 1, 0.1, 0.1, 0.1, 0.1, 0.1)
        # Pick a random duration:
        # dur = musx.pick(3, 3.5, 4)
        # dur = musx.pick(0.8, 1.3, 1.6)
        # dur = musx.pick(1.4, 1.13, 1.5)
        dur = musx.pick(0.11, 0.13, 0.15)
        repeat = random.randint(3, 6)
        pre_time = float(format(random.uniform(0, 4 - (dur * 4 * repeat)), '.2f'))
        after_time = float(format(4 - (dur * 4 * repeat) - pre_time, '.2f'))
        vel = musx.pick(30, 50, 60)
        # Set up the pre_time:
        time.sleep(pre_time)
        print(f"pre: {pre_time}, after: {after_time}")
        # Inner loop to play the notes:
        for i in range(repeat):
            # Select the notes:
            note_selected = random.choices(note_pool, weights=(possibility), k = 4)
            # Pick a random midi key number:
            key_1, key_2, key_3, key_4 = keynum(note_selected[0]), keynum(note_selected[1]), keynum(note_selected[2]), keynum(note_selected[3])
            # Print and send the notes:
            print(f"ornament {i+1}, key: {key_1}, {key_2}, {key_3}, {key_4}, dur: {dur}, vel: {vel}")
            midiout.send_message(musx.note_on(2, key_1, vel))
            # Wait for duration:
            time.sleep(dur)
            midiout.send_message(musx.note_off(2, key_1, vel))
            midiout.send_message(musx.note_on(2, key_2, vel))
            # Wait for duration:
            time.sleep(dur)
            midiout.send_message(musx.note_off(2, key_2, vel))
            midiout.send_message(musx.note_on(2, key_3, vel))
            # Wait for duration:
            time.sleep(dur)
            midiout.send_message(musx.note_off(2, key_3, vel))
            midiout.send_message(musx.note_on(2, key_4, vel))
            # Wait for duration:
            time.sleep(dur)
            # Stop the note:
            midiout.send_message(musx.note_off(2, key_4, vel))
        # Set up the after_time:
        time.sleep(after_time)
    # Test:
    print("\nAll done!\n")
    # Set midi synth back to piano:
    midiout.send_message(musx.program_change(0, 0))

if __name__ == '__main__':
    ornament_maker(chord_progression)