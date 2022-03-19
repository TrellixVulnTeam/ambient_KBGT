from harmonizer_dict import note_accidental_to_semitone

# Get the keys:
def getKey(dictionary):
    return dictionary.keys()

# Get the values:
def getValue(dictionary):
    return dictionary.values()

# Assign the input:
dictionary = note_accidental_to_semitone

# Get the dictionary:
semitone_to_note_accidental = dict(zip(getValue(dictionary), getKey(dictionary)))
print(semitone_to_note_accidental)

# Result:
semitone_to_note_accidental = {

}
