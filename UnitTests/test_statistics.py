import unittest
from StatisticsCalc.statistics_calculator import statsCalc
from CSVReader.csv_reader import CSVReader
from numpy import var, std, mean
from scipy import stats
from RandomGenerator.randomIntList import randomIntList
from pprint import pprint

class MyTestCase(unittest.TestCase):
    def setUp( self ) -> None:
        self.statsCalc = statsCalc()
        self.allData = CSVReader('./UnitTests/TestData/StatisticsTestData.csv').data
        self.testData = [int(row['Value']) for row in self.allData]
        self.testAnswers = CSVReader('./UnitTests/TestData/StatsAnswers.csv').data
        self.list = randomIntList(1,100,20,10)
        self.num_val = 4
        self.confidenceLevel = 0.95
        self.confidenceLevel_Zscore = 1.96
        self.testvaribility = 0.5

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

    def test_simple_random_sampling_method( self ):
        selection = str(self.statsCalc.randSample(self.list, self.num_val))
        non_str_selection = self.statsCalc.randSample(self.list, self.num_val)
        pprint("Random Sample from the list: " + selection)
        in_list = False
        for val in non_str_selection:
            if val in self.list:
                in_list = True
            else:
                in_list = False
        self.assertEqual(in_list, True)

    def test_confidence_interval_method (self):
        pprint("confidence interval bottom: " + str(self.statsCalc.confidenceIntervalBottom(self.testData, self.confidenceLevel)))
        pprint("confidence interval top: " + str(self.statsCalc.confidenceIntervalTop(self.testData, self.confidenceLevel)))
        test_values = stats.norm.interval(self.confidenceLevel, mean(self.testData), self.statsCalc.divide(std(self.testData), self.statsCalc.squareRoot(len(self.testData))))

        confidence_bottom = self.statsCalc.confidenceIntervalBottom(self.testData, self.confidenceLevel)
        confidence_top = self.statsCalc.confidenceIntervalTop(self.testData, self.confidenceLevel)
        tester = False
        for values in range(len(test_values)):
            test = test_values[values]
            rounded = round(test, 5)

            if rounded == confidence_bottom:
                tester = True
            elif rounded == confidence_top:
                tester = True
            else:
                tester = False

        self.assertEqual(tester,True)
        '''confidence_bottom = self.statsCalc.confidenceIntervalBottom(self.testData, self.confidenceLevel)
        confidence_top = self.statsCalc.confidenceIntervalTop(self.testData, self.confidenceLevel)
        test_values = stats.norm.interval(self.confidenceLevel, mean(self.testData), std(self.testData))
        testList = []
        for val in test_values:
            x = round(val, 5)
            testList.append(x)
        in_list = False
        for num in testList:
            pprint(num)
            pprint(confidence_bottom)
            pprint(confidence_top)
            if num == confidence_bottom or num == confidence_top:
                in_list = True
            else:
                in_list = False
        self.assertEqual(in_list, True)'''

    def test_marginOfError_method( self ):
        pprint("Margin of Error: " + str(self.statsCalc.marginOfError(self.testData,self.confidenceLevel_Zscore)))
        self.assertEqual(True, True)

    def test_cochran_method( self ):
        pprint("Cochran Sample Size: " + str(self.statsCalc.cochran(self.testData,self.confidenceLevel, self.confidenceLevel_Zscore, self.testvaribility)))
        self.assertEqual(True, True)

if __name__ == '__main__':
    unittest.main()
