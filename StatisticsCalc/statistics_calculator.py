from Calculator.calculator import calculator
from StatisticsCalc.mean import mean
from StatisticsCalc.median import median

class statsCalc(calculator):

    result = 0

    def mean (self, data):
        self.result = mean(data)
        return self.result

    def median (self, data):
        self.result = median(data)
        return self.result
