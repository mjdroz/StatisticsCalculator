from StatisticsCalc.variance import variance
from Calculator.square_root import squareRoot

def standard_deviation(data):
    variance_of_data = variance(data)
    return squareRoot(variance_of_data)