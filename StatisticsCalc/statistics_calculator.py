from Calculator.calculator import calculator
from StatisticsCalc.mean import mean

class statsCalc(calculator):

    result = 0

    def mean (self, data):
        self.result = mean(data)
        return self.result
