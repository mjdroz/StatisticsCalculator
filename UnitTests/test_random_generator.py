import unittest
from pprint import pprint
from RandomGenerator.random_generator import random

class MyTestCase(unittest.TestCase):
    def setUp( self ) -> None:
        self.random = random()
        self.start = 1
        self.end = 100
        self.length = 6
        self.seed = 8
        self.num_val = 3
        self.list = self.random.randomIntList(self.start, self.end, self.length, self.seed)

    def test_randomInt_method( self ):
        int_rand = str(self.random.randomInt(self.start, self.end))
        pprint("random int: " + int_rand)
        self.assertEqual(isinstance(self.random.randomInt(self.start, self.end), int),True)

    def test_randomDec_method(self):
        dec_rand = str(self.random.randomDec(self.start, self.end))
        pprint("random decimal: " + dec_rand)
        self.assertEqual(isinstance(self.random.randomDec(self.start, self.end), float), True)

    def test_randomIntSeed_method( self ):
        int_seed = str(self.random.randomIntSeed(self.start, self.end, self.seed))
        pprint("seeded int: " + int_seed)
        self.assertEqual(int_seed, str(self.random.randomIntSeed(self.start, self.end, self.seed)))

    def test_randomDecSeed_method( self ):
        dec_seed = str(self.random.randomDecSeed(self.start, self.end, self.seed))
        pprint("seeded decimal: " + dec_seed)
        self.assertEqual(dec_seed, str(self.random.randomDecSeed(self.start, self.end, self.seed)))

    def test_randomIntList_method(self):
        int_array = str(self.random.randomIntList(self.start, self.end, self.length, self.seed))
        val_list = (self.random.randomIntList(self.start, self.end, self.length, self.seed))
        pprint("integer array with a seed: " + int_array)
        for val in val_list:
            test_val = int(val)
            self.assertEqual(isinstance(test_val, int), True)

    def test_randomDecList_method(self):
        dec_array = str(self.random.randomDecList(self.start, self.end, self.length, self.seed))
        dec_list = (self.random.randomDecList(self.start, self.end, self.length, self.seed))
        pprint("decimal array with a seed: " + dec_array)
        for val in dec_list:
            test_val = float(val)
            self.assertEqual(isinstance(test_val, float), True)

    def test_randomListSelection_method(self):
        selection = str(self.random.randomListSelection(self.list))
        non_str_selection = self.random.randomListSelection(self.list)
        pprint("selection from the list: " + selection)
        if non_str_selection in self.list:
            in_list = True
        else:
            in_list = False
        self.assertEqual(in_list, True)

    def test_randomListSelectionSeed_method(self):
        selection = str(self.random.randomListSelectionSeed(self.list, self.seed))
        pprint("seeded selection from the list: " + selection)
        self.assertEqual(selection, str(self.random.randomListSelectionSeed(self.list, self.seed)))

    def test_randomAmountSelection_method(self):
        selection = str(self.random.randomAmountSelection(self.list, self.num_val))
        non_str_selection = self.random.randomAmountSelection(self.list, self.num_val)
        pprint("N number of values selection from the list: " + selection)
        in_list = False
        for val in non_str_selection:
            if val in self.list:
                in_list = True
            else:
                in_list = False
        self.assertEqual(in_list, True)

    def test_randomAmountSelectionSeed_method(self):
        selection = str(self.random.randomAmountSelectionSeed(self.list, self.num_val, self.seed))
        pprint("N number of values selection from the list with a seed: " + selection)
        self.assertEqual(selection, str(self.random.randomAmountSelectionSeed(self.list, self.num_val, self.seed)))

if __name__ == '__main__':
    unittest.main()
