import unittest
from StatisticsCalc.statistics_calculator import statsCalc
from CSVReader.csv_reader import CSVReader
from pprint import pprint

class MyTestCase(unittest.TestCase):
    def setUp( self ) -> None:
        self.statsCalc = statsCalc()
        self.allData = CSVReader('./UnitTests/TestData/StatisticsTestData.csv').data
        self.testData = [int(row['Value']) for row in self.allData]
        #self.testAnswers = CSVReader('./UnitTests/TestData/StatsAnswers.csv').data

    def test_instantiate_stats_calculator( self ):
        self.assertIsInstance(self.statsCalc, statsCalc)
        pprint("this is a test")

    def test_mean_method( self ):
        pprint("hello world")
        testAnswers = CSVReader('./UnitTests/TestData/StatsAnswers.csv').data
        pprint(testAnswers)
        for row in testAnswers:
            self.assertEqual(self.statsCalc.mean(self.testData),float(row['Mean']))
            self.assertEqual(self.statsCalc.result, float(row['Mean']))


if __name__ == '__main__':
    unittest.main()
