"""
This is my first musx program. 
The goal is to test out the necessary module to make the music.
"""

# Import the modules:
from musx import Score, Seq, MidiFile, keynum
from musx.midi.gm import AcousticGrandPiano
from musx.paint import brush


# Define the melody:
melody = keynum([
    ['g3', 'g4', 'a4', 'd4'], ['c3', 'c4', 'd4', 'g4'], 
    ['d3', 'd4', 'f4', 'a4'], ['a3', 'a4', 'c4', 'e4'], 
    ['e3', 'e4', 'f#4', 'b4'], ['b3', 'b4', 'd#4', 'f#4'], 
    ['d3', 'f#4', 'a4', 'c#4'], ['f#3', 'a4', 'c#4', 'e4']
])

# Main function:
if __name__ == '__main__':
    # Meta track:
    track0 = MidiFile.metatrack()
    # Track holds the composition:
    track1 = Seq()
    # Create the score:
    score = Score(out = track1)
    # Compose the score:
    score.compose(brush(
        score, 
        length=8, 
        pitch=melody, 
        rhythm=2,
        duration=2, 
        amplitude=0.5, 
        instrument=AcousticGrandPiano,
        ))
    # Create the Midi file:
    file = MidiFile('mymusx1.mid', [track0, track1]).write()
    print(f"'{file.pathname}' done!")