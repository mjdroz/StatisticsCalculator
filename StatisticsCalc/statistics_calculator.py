from Calculator.calculator import calculator
from StatisticsCalc.mean import mean
from StatisticsCalc.median import median
from StatisticsCalc.mode import mode
from StatisticsCalc.variance import variance

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







    # Soucrce for mean, median, mode, and variance: https://www.geeksforgeeks.org/finding-mean-median-mode-in-python-without-libraries/
