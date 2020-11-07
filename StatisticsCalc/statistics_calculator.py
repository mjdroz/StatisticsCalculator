from Calculator.calculator import calculator
from StatisticsCalc.mean import mean
from StatisticsCalc.median import median
from StatisticsCalc.mode import mode
from StatisticsCalc.variance import variance
from StatisticsCalc.standard_deviation import standard_deviation
from StatisticsCalc.z_score import z_score
from PopulationSampling.simple_random_sampling import simple_random_sampling

class statsCalc(calculator):

    result = 0

    def mean (self, data):
        self.result = mean(data)
        return self.result

    def median (self, data):
        self.result = median(data)
        return self.result

    def mode (self, data):
        self.result = mode(data)
        return self.result

    def variance (self, data):
        self.result = variance(data)
        return self.result

    def std_dev (self, data):
        self.result = standard_deviation(data)
        return self.result

    def zscore(self, data):
        self.result = z_score(data)
        return self.result

    def randSample(self, data, num_values):
        self.result = simple_random_sampling(data, num_values)
        return self.result


    # Soucrce for mean, median, and mode: https://www.geeksforgeeks.org/finding-mean-median-mode-in-python-without-libraries/
    # Source for variance: https://www.geeksforgeeks.org/python-variance-of-list/
    # Source for standard deviation: https://www.geeksforgeeks.org/python-standard-deviation-of-list/
    # Sources for z score: https://www.geeksforgeeks.org/z-score-for-outlier-detection-python/ and https://www.statology.org/z-score-python/
