import threading, time, sys
import rtmidi
import musx
from musx import keynum

midiout = rtmidi.MidiOut()
print(midiout)

outports = midiout.get_ports()
print("available ports:", outports)

midiout.open_port(outports.index('IAC Driver Bus 1'))

midiout.is_port_open()

# Define the melody:
melody = [
    ['g3', 'g4', 'a4', 'd4'], ['c3', 'c4', 'd4', 'g4'], 
    ['d3', 'd4', 'f4', 'a4'], ['a3', 'a4', 'c4', 'e4'], 
    ['e3', 'e4', 'f#4', 'b4'], ['b3', 'b4', 'd#4', 'f#4'], 
    ['d3', 'f#4', 'a4', 'c#4'], ['f#3', 'a4', 'c#4', 'e4']
]

# Extract the four voices from the list:
soprano = keynum([i[3] for i in melody])
alto = keynum([i[2] for i in melody])
tenor = keynum([i[1] for i in melody])
bass = keynum([i[0] for i in melody])

# Functions:
def voice_leading(notes):
    for key in musx.keynum(notes):
        print("note: ", key)
        midiout.send_message(musx.note_on(0, key, 95))
        time.sleep(3.5)
        midiout.send_message(musx.note_off(0, key, 127))

# Threading:
s_voice = threading.Thread(target=voice_leading, args=soprano)
a_voice = threading.Thread(target=voice_leading, args=alto)
t_voice = threading.Thread(target=voice_leading, args=tenor)
b_voice = threading.Thread(target=voice_leading, args=bass)

# Start the threads:
s_voice.start()
a_voice.start()
t_voice.start()
b_voice.start()
