import unittest
from StatisticsCalc.statistics_calculator import statsCalc
from CSVReader.csv_reader import CSVReader
from numpy import var, std
from scipy import stats

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

    def test_variance_method( self ):
        var_test_val = (var(self.testData))
        self.assertEqual(self.statsCalc.variance(self.testData), var_test_val)
        self.assertEqual(self.statsCalc.result, var_test_val)

    def test_standard_deviation_method( self ):
        std_test_val = (std(self.testData))
        round_test = round(float(std_test_val), 8)
        self.assertEqual(self.statsCalc.std_dev(self.testData), round_test)
        self.assertEqual(self.statsCalc.result, round_test)

    def test_z_score_method( self ):
        round_vals = []
        z_test_vals = (stats.zscore(self.testData))
        for val in z_test_vals:
            rounded_test_val = round(val, 5)
            round_vals.append(rounded_test_val)
        zscores = self.statsCalc.zscore(self.testData)
        length =len(z_test_vals)
        for i in range(length):
            self.assertEqual(zscores[i], round_vals[i])

if __name__ == '__main__':
    unittest.main()
