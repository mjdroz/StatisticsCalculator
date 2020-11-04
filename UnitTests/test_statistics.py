import unittest
from numpy.random import randint
from StatisticsCalc.statistics_calculator import statsCalc

class MyTestCase(unittest.TestCase):
    def setUp( self ) -> None:
        self.statsCalc = statsCalc()
        #self.testData = numpy.randint()

    def test_instantiate_stats_calculator( self ):
        self.assertIsInstance(self.statsCalc, statsCalc)

if __name__ == '__main__':
    unittest.main()
