import unittest
from StatisticsCalc.statistics_calculator import statsCalc
from CSVReader.csv_reader import CSVReader
from pprint import pprint

class MyTestCase(unittest.TestCase):
    def setUp( self ) -> None:
        self.statsCalc = statsCalc()
        self.allData = CSVReader('./UnitTests/TestData/StatisticsTestData.csv').data
        self.testData = [int(row['Value']) for row in self.allData]
        self.testAnswers = CSVReader('./UnitTests/TestData/StatsAnswers.csv').data

    def test_instantiate_stats_calculator( self ):
        self.assertIsInstance(self.statsCalc, statsCalc)

    def test_mean_method( self ):
        for row in self.testAnswers:
            self.assertEqual(self.statsCalc.mean(self.testData),float(row['Mean']))
            self.assertEqual(self.statsCalc.result, float(row['Mean']))

    def test_median_method( self ):
        for row in self.testAnswers:
            self.assertEqual(self.statsCalc.median(self.testData), float(row['Median']))
            self.assertEqual(self.statsCalc.result, float(row['Median']))

    def test_mode_method( self ):
        for row in self.testAnswers:
            self.assertEqual(self.statsCalc.mode(self.testData), float(row['Mode']))
            self.assertEqual(self.statsCalc.result, float(row['Mode']))


if __name__ == '__main__':
    unittest.main()
