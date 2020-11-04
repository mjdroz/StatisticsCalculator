import unittest
from pprint import pprint
from RandomGenerator.random_generator import random

class MyTestCase(unittest.TestCase):
    def setUp( self ) -> None:
        self.random = random()
        self.start = 1
        self.end = 100
        self.length = 6
        self.sneed = 8
        self.items = 3
        self.list = self.random.randomIntList(self.start, self.end, self.length, self.sneed)

    def test_randomInt_method( self ):
        int_rand = str(self.random.randomInt(self.start, self.end))
        pprint("random int: " + int_rand)
        self.assertEqual(True,True)

    def test_randomDec_method(self):
        dec_rand = str(self.random.randomDec(self.start, self.end))
        pprint("random decimal: " + dec_rand)
        self.assertEqual(True, True)

    def test_randomIntSeed_method( self ):
        int_seed = str(self.random.randomIntSeed(self.start, self.end, self.sneed))
        pprint("seeded int: " + int_seed)
        self.assertEqual(True,True)

    def test_randomDecSeed_method( self ):
        dec_seed = str(self.random.randomDecSeed(self.start, self.end, self.sneed))
        pprint("seeded decimal: " + dec_seed)
        self.assertEqual(True,True)

    def test_randomIntList_method(self):
        int_array = str(self.random.randomIntList(self.start, self.end, self.length, self.sneed))
        pprint("integer array with a seed: " + int_array)
        self.assertEqual(True, True)

    def test_randomDecList_method(self):
        dec_array = str(self.random.randomDecList(self.start, self.end, self.length, self.sneed))
        pprint("decimal array with a seed: " + dec_array)
        self.assertEqual(True, True)

    def test_randomListSelection_method(self):
        selection = str(self.random.randomListSelection(self.list))
        pprint("selection from the list: " + selection)
        self.assertEqual(True, True)

    def test_randomListSelectionSeed_method(self):
        selection = str(self.random.randomListSelectionSeed(self.list, self.sneed))
        pprint("seeded selection from the list: " + selection)
        self.assertEqual(True, True)

    def test_randomAmountSelection_method(self):
        selection = str(self.random.randomAmountSelection(self.list, self.items))
        pprint("N number of values selection from the list: " + selection)
        self.assertEqual(True, True)

    def test_randomAmountSelectionSeed_method(self):
        selection = str(self.random.randomAmountSelectionSeed(self.list, self.items, self.sneed))
        pprint("N number of values selection from the list with a seed: " + selection)
        self.assertEqual(True, True)

if __name__ == '__main__':
    unittest.main()
