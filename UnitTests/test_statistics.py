import unittest
from StatisticsCalc.statistics_calculator import statsCalc
from CSVReader.csv_reader import CSVReader

class MyTestCase(unittest.TestCase):
    def setUp( self ) -> None:
        self.statsCalc = statsCalc()
        self.testData = CSVReader('/UnitTests/TestData/StatisticsTestData.csv').data

    def test_instantiate_stats_calculator( self ):
        self.assertIsInstance(self.statsCalc, statsCalc)

    '''def test_mean_method( self ):
        res = self.statsCalc.mean(self.testData)
        print (res)
        self.assertEqual(True,True)'''

if __name__ == '__main__':
    unittest.main()
