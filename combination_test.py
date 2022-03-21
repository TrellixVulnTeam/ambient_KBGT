import unittest
import random

from harmonizer_dict import note_accidental_range_to_midi as midi_num
from harmonizer_dict import close_structure_dict as close_dict
from harmonizer_dict import pre_assign_register as pre
from distance_def import distance

from combination import note_range_zip
from combination import ascending_order
from combination import voice_range
from combination import sat_octave
from combination import remove_double
from combination import ideal_chord
from combination import find_structure
from combination import start_chord


# Input_1:
# register = [['2', '4', '4', '4'], ['3', '4', '5', '5']]
# chord = [['c', 'c', 'e', 'g'], ['f', 'f', 'c', 'a']]

# Input_2:
# register = pre
# chord = [['g', 'g', 'b', 'd'], ['g', 'g', 'd', 'b'], ['g', 'b', 'g', 'd'], ['g', 'b', 'd', 'g'], ['g', 'd', 'g', 'b'], ['g', 'd', 'b', 'g']]
# chord = [['f', 'f', 'a', 'c'], ['f', 'f', 'c', 'a'], ['f', 'a', 'f', 'c'], ['f', 'a', 'c', 'f'], ['f', 'c', 'f', 'a'], ['f', 'c', 'a', 'f']]
# chord = [['ebb', 'ebb', 'abb', 'bbb'], ['ebb', 'ebb', 'bbb', 'abb'], ['ebb', 'abb', 'ebb', 'bbb'], ['ebb', 'abb', 'bbb', 'ebb'], ['ebb', 'bbb', 'ebb', 'abb'], ['ebb', 'bbb', 'abb', 'ebb']]
# chord = [['a##', 'c##', 'e##', 'g##'], ['a##', 'c##', 'g##', 'e##'], ['a##', 'e##', 'c##', 'g##'], ['a##', 'e##', 'g##', 'c##'], ['a##', 'g##', 'c##', 'e##'], ['a##', 'g##', 'e##', 'c##']]

# Input_3:
register = pre
chord = [['c', 'e', 'g', 'b'], ['c', 'e', 'b', 'g'], ['c', 'g', 'e', 'b'], ['c', 'g', 'b', 'e'], ['c', 'b', 'e', 'g'], ['c', 'b', 'g', 'e']]

# For all chords:
full_list = note_range_zip(chord, register)
full_list_result = ascending_order(full_list)
screened_result = voice_range(full_list_result)
legal_chord = sat_octave(screened_result)

# First chord only:
screened_result_2 = remove_double(screened_result)
good_chord = ideal_chord(screened_result_2)
close_chord = find_structure(good_chord)[0]
open_chord = find_structure(good_chord)[1]
first_chord = start_chord(good_chord)

# Test (all chord):
# print(voice_range(ascending_order(note_range_zip(chord, register))))
# print(len(voice_range(ascending_order(note_range_zip(chord, register)))))

# Test (first chord):
# print(start_chord(ideal_chord(remove_double(voice_range(ascending_order(note_range_zip(chord, register)))))))
# print(len(start_chord(ideal_chord(remove_double(voice_range(ascending_order(note_range_zip(chord, register))))))))

# Test:
print('full_list: ' + str(full_list))
print(len(full_list))
print('full_list_result: ' + str(full_list_result))
print(len(full_list_result))
print('screened_result: ' + str(screened_result))
print(len(screened_result))
print('legal_chord: ' + str(legal_chord))
print(len(legal_chord))
print('screened_result_2: ' + str(screened_result_2))
print(len(screened_result_2))
print('good_chord: ' + str(good_chord))
print(len(good_chord))
print('close_chord: ' + str(close_chord))
print(len(close_chord))
print('open_chord: ' + str(open_chord))
print(len(open_chord))
print('first_chord: ' + str(first_chord))
print(len(first_chord))