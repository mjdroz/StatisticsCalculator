from StatisticsCalc.standard_deviation import standard_deviation
from Calculator.square_root import squareRoot
from Calculator.division import division
from Calculator.multiplication import multiplication

def margin_of_error (data):
    ph_ci = 0.72
    size = len(data)
    std = standard_deviation(data)
