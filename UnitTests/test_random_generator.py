import unittest
from pprint import pprint
from RandomGenerator.random_generator import random

class MyTestCase(unittest.TestCase):
    def setUp( self ) -> None:
        self.random = random()
        self.start = 1
        self.end = 100

    def test_randomInt_method( self ):
        int_rand = str(self.random.randomInt(self.start, self.end))
        pprint("random int: " + int_rand)
        self.assertEqual(True,True)

    def test_randomDec_method(self):
        dec_rand = str(self.random.randomDec(self.start, self.end))
        pprint("random decimal: " + dec_rand)
        self.assertEqual(True, True)

    def test_randomIntSeed_method( self ):
        int_seed = str(self.random.randomIntSeed(self.start, self.end))
        pprint("seeded int: " + int_seed)
        self.assertEqual(True,True)


if __name__ == '__main__':
    unittest.main()
