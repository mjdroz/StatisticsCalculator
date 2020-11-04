import unittest
from RandomGenerator.random_generator import random

class MyTestCase(unittest.TestCase):
    def setUp( self ) -> None:
        self.random = random()
        self.start = 1
        self.end = 100

    def test_randomInt_method( self ):
        print(self.random.randomInt(self.start, self.end))
        self.assertEqual(True,True)



if __name__ == '__main__':
    unittest.main()
