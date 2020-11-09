import unittest
from AdditionalModules.random_generator2 import randomNumberGenerator


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.randomGen = randomNumberGenerator()
        self.start = 1
        self.end = 500
        self.seed = 12

    def test_random_int_generator_method(self):
        num = self.randomGen.randomNumGeneratorInt(self.start, self.end)
        print("Random Number Generator 2 Test Int: " + str(num))
        self.assertEqual(isinstance(num, int), True)

    def test_random_dec_generator_method(self):
        num = self.randomGen.randomNumGeneratorDec(self.start, self.end)
        print("Random Number Generator 2 Test Dec: " + str(num))
        self.assertEqual(isinstance(num, float), True)

    def test_random_int_generator_seed_method(self):
        num = self.randomGen.randomNumGeneratorIntSeed(self.start, self.end, self.seed)
        print("Random Number Generator 2 Test Int with Seed: " + str(num))
        self.assertEqual(isinstance(num, int), True)

    def test_random_dec_generator_seed_method(self):
        num = self.randomGen.randomNumGeneratorDecSeed(self.start, self.end, self.seed)
        print("Random Number Generator 2 Test Dec with Seed: " + str(num))
        self.assertEqual(isinstance(num, float), True)

if __name__ == '__main__':
    unittest.main()
