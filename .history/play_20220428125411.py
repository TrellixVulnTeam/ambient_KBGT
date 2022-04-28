import time
import musx
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
# chord_progression = main()[0] * 4

# Get the structure of the piece:
paragraph = random.randint(5, 8)
timeline = get_duration(paragraph, 10, 8, 12)
section = get_section(timeline)
start = timer()
total_section = get_flatten_list(section[1])
total_time_frame = get_time_frame(section[2])
total_chord = get_chord(total_time_frame, chord_progression)
total_pool = get_all_pool(total_time_frame, chord_progression)
end = timer()

print('\nparagraph:', str(paragraph))
print('total_paragraph:', str(timeline), str(sum(timeline)), '\n')
print('section:', section[1], len(section[1]),'\n\ntotal_sec:', section[2], len(section[2]), '\n')
print('total_section:', total_section, len(total_section), '\n')
print('total_time_frame:', total_time_frame, len(total_time_frame), '\n')
print('total_chord:', total_chord, len(total_chord), '\n')
print('total_pool:', total_pool, len(total_pool))
print('\nRunning time:', str(round((end - start), 2)) + 's\n')

def ornament(total_section, total_time_frame, total_pool):
    for i in range(len(total_section)):
        current_section = total_section[i]
        current_time_frame = total_time_frame[i]
        current_pool = total_pool[i]
        print('current_section:', current_section, '\n')
        print('current_time_frame:', current_time_frame, len(current_time_frame), '\n')
        print('current_pool:', current_pool, len(current_pool), '\n')
        if current_section == 'intro':
            print('—————————————————— now playing:', current_section, '\n')
            for j in range(len(current_time_frame)):
                phrase_time = current_time_frame[j]
                phrase_pool = current_pool[j]
                print('phrase_time:', phrase_time, '\n')
                print('phrase_pool:', phrase_pool, '\n')
                if phrase_time < 5:
                    note_select = random.randint(2, 4)
                elif 5 <= phrase_time < 10:
                    note_select = random.randint(2, 5)
                elif 10 <= phrase_time < 15:
                    note_select = random.randint(3, 7)
                elif 15 <= phrase_time < 20:
                    note_select = random.randint(6, 10)
                else:
                    note_select = random.randint(8, 15)
                print('note_select:', note_select, '\n')
                pre_post_ratio = random.randint(10, 50) / 100
                print('pre_post_ratio:', pre_post_ratio, '\n')
                notes_ratio = round(1 - pre_post_ratio, 2)
                print('notes_ratio:', notes_ratio, '\n')
                pre_time = round(phrase_time * round(random.uniform(0.01, pre_post_ratio*0.7), 2), 2)
                print('pre_time:', pre_time, '\n')
                post_time = round(phrase_time * pre_post_ratio - pre_time, 2)
                print('post_time:', post_time, '\n')
                note_span = phrase_time * notes_ratio
                note_time = []
                for k in range(note_select):
                    temp_note_time = round(random.uniform(0.01, (note_span-sum(note_time))/(note_select-k)), 2)
                    if k == note_select-1:
                        temp_note_time = round(note_span - sum(note_time), 2)
                    note_time.append(temp_note_time)
                print('note_time:', note_time, '\n')
                print('check:', round(sum(note_time), 2) + pre_time + post_time, phrase_time, '\n')
                print('—————————————————— sending notes\n')
                time.sleep(pre_time)
                print(f'pre_time: {pre_time}\n')
                for m in range(note_select):
                    note = random.choices(phrase_pool, weights=(1, 1, 1, 1, 1, 0.1, 0.1, 0.1, 0.1, 0.1), k=1)[0]
                    vel = random.randint(30, 70)
                    midiout.send_message(musx.note_on(6, note, vel))
                    print(f'melody {m+1}, note: {note}, vel: {vel}\n')
                    time.sleep(note_time[m])
                    midiout.send_message(musx.note_off(6, note, vel))
                time.sleep(post_time)
                print(f'post_time: {post_time}\n')
                print('—————————————————— phrase finished\n')

def pad(total_section, total_time_frame, total_chord):
    for i in range(len(total_section)):
        current_section = total_section[i]
        current_time_frame = total_time_frame[i]
        current_chord = total_chord[i]
        print('current_section:', current_section, '\n')
        print('current_time_frame:', current_time_frame, len(current_time_frame), '\n')
        print('current_chord:', current_chord, len(current_chord), '\n')
        # if current_section == 'intro':
        #     print('—————————————————— now playing: intro', '\n')
        #     for j in range(len(current_time_frame)):
        #         phrase_time = current_time_frame[j]
        #         phrase_chord = current_chord[j]
        #         print('phrase_time:', phrase_time, '\n')
        #         print('phrase_chord:', phrase_chord, '\n')
        #         note_time = []
        #         for k in range(len(phrase_chord)):
        #             if k == 0:
        #                 temp_note_time = round(random.uniform(0.01, 0.8), 2)
        #             else:
        #                 temp_note_time = round(random.uniform(0.01, (phrase_time-sum(note_time))/(len(phrase_chord))), 2)
        #             note_time.append(temp_note_time)
        #         print('note_time:', note_time, '\n')
        #         print('check:', round(sum(note_time), 2), phrase_time, round(sum(note_time), 2) <= phrase_time, '\n')
        #         print('—————————————————— sending chords\n')
        #         for m in range(len(note_time)):
        #             time.sleep(note_time[m])
        #             note = phrase_chord[m]
        #             vel = random.randint(30, 70)
        #             midiout.send_message(musx.note_on(m+1, note, vel))
        #             print(f'chord {m+1}, note: {note}, vel: {vel}, chan: {m+1}\n')
        #         time.sleep(phrase_time - sum(note_time))
        #         print(f'chord_last: {round(phrase_time - sum(note_time), 2)}\n')
        #         for n in range(len(note_time)):
        #             midiout.send_message(musx.note_off(n+1, phrase_chord[n], vel))
        #         print('—————————————————— phrase finished\n')
        if current_section == 'A' or current_section == 'B':
            print('—————————————————— now playing: A section', '\n')
            for j in range(len(current_time_frame)):
                phrase_time = current_time_frame[j]
                phrase_chord = current_chord[j]
                print('phrase_time:', phrase_time, '\n')
                print('phrase_chord:', phrase_chord, '\n')
                print('—————————————————— sending chords\n')
                for k in range(len(phrase_chord)):
                    note = phrase_chord[k]
                    if current_section == 'A':
                        vel = random.randint(20, 40)
                    elif current_section == 'B':
                        vel = random.randint(30, 50)
                    midiout.send_message(musx.note_on(k+1, note, vel))
                    print(f'chord {j+1}, note: {note}, vel: {vel}, chan: {k+1}\n')
                time.sleep(phrase_time)
                for k in range(len(phrase_chord)):
                    midiout.send_message(musx.note_off(k+1, phrase_chord[k], vel))
                print('—————————————————— phrase finished\n')
        if current_section == 'C' or 

if __name__ == '__main__':
    # ornament(total_section, total_time_frame, total_pool)
    pad(total_section, total_time_frame, total_chord)

# Threading:
# ornaments = threading.Thread(target=ornament, args=[total_section, total_time_frame, total_pool])
# chord = threading.Thread(target=pad, args=[total_section, total_time_frame, total_chord])

# Call the variables:
# ornaments.start()
# chord.start()