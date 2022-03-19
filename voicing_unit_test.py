import unittest
from voicing import check_same_direction
from voicing import check_voice_overlap
from voicing import check_direct_motion
from voicing import check_parallel_motion
from voicing import count_step
from harmonizer_dict import pre_assign_register as pre

class NameTestCase(unittest.TestCase):
    def test_1_1(self):
        test = check_same_direction([['c3', 'g4', 'b4', 'e5'], ['f3', 'a4', 'c5', 'f5']])
        self.assertEqual(test, True) # True (move up)
    def test_1_2(self):
        test = check_same_direction([['f3', 'a4', 'c5', 'f5'], ['c3', 'g4', 'b4', 'e5']])
        self.assertEqual(test, True) # True (move down)
    def test_1_3(self):
        test = check_same_direction([['f3', 'a4', 'c5', 'f5'], ['f3', 'a4', 'c5', 'f5']])
        self.assertEqual(test, False) # False (static)
    def test_1_4(self):
        test = check_same_direction([['f3', 'a4', 'c5', 'f5'], ['c3', 'e4', 'b5', 'g5']])
        self.assertEqual(test, False) # False (legal voice leading)
    def test_2_1(self):
        test = check_voice_overlap([['f3', 'a4', 'c5', 'f5'], ['c3', 'g3', 'e4', 'b4']])
        self.assertEqual(test, True) # True ('e4' lower than 'a4')
    def test_2_2(self):
        test = check_voice_overlap([['f3', 'a4', 'c5', 'f5'], ['c3', 'g4', 'b4', 'e5']])
        self.assertEqual(test, False) # False (legal voice leading)
    def test_3_1(self): 
        test = check_direct_motion([['c3', 'g3', 'c4', 'e4'], ['g3', 'b3', 'd4', 'g4']])
        self.assertEqual(test, True) # True (direct 8ve)
    def test_3_2(self):
        test = check_direct_motion([['e3', 'g3', 'e4', 'c5'], ['d3', 'a3', 'f4', 'a4']])
        self.assertEqual(test, True) # True (direct 5th)
    def test_3_3(self):
        test = check_direct_motion([['g3', 'd4', 'g4', 'b4'], ['c4', 'e4', 'g4', 'c5']])
        self.assertEqual(test, False) # False (soprano stepwise)
    def test_4_1(self):
        test = check_parallel_motion([['f#3', 'c#4', 'c#4', 'a#4'], ['b2', 'f#3', 'd4', 'b4']])
        self.assertEqual(test, True) # True (Parallel 5th)
    def test_4_2(self):
        test = check_parallel_motion([['b2', 'd4', 'f#4', 'b4'], ['f#3', 'c#4', 'a#4', 'f#5']])
        self.assertEqual(test, True) # True (Parallel 8ve)
    def test_4_3(self):
        test = check_parallel_motion([['b2', 'f#4', 'b4', 'd5'], ['f#3', 'f#4', 'a#4', 'c#5']])
        self.assertEqual(test, False) # False (legal voice leading)
    def test_5_1(self):
        test = count_step(['f3', 'a4', 'c5', 'f5'], ['c3', 'e4', 'b4', 'g5'])
        self.assertEqual(test, 5) # 5 steps in SAT voice
    def test_5_2(self):
        test = count_step(['f3', 'a4', 'c5', 'f5'], ['g3', 'g4', 'b4', 'd5'])
        self.assertEqual(test, 4) # 4 steps in SAT voice
    def test_5_3(self):
        test = count_step(['f3', 'a4', 'c5', 'f5'], ['g3', 'g3', 'd4', 'b5'])
        self.assertEqual(test, 17) # 17 steps in SAT voice

if __name__ == '__main__':
    unittest.main()

###########################################################