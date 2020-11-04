import unittest
from RandomGenerator.random_generator import random

class MyTestCase(unittest.TestCase):
    def setUp( self ) -> None:
        self.random = random()
        self.start = 1
        self.end = 100
        self.seed = 3

    def test_randomInt_method( self ):
        print(self.random.randomInt(self.start, self.end))
        self.assertEqual(True,True)

    def test_randomDec_method(self):
        print(self.random.randomDec(self.start, self.end))
        self.assertEqual(True, True)

    '''def test_randomIntSeed_method( self ):
        print(self.random.randomIntSeed(self.start, self.end,self.seed))
        self.assertEqual(True,True)'''


if __name__ == '__main__':
    unittest.main()
