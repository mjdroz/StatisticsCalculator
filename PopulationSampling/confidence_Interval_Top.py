from Calculator.division import division
from Calculator.addition import addition
from Calculator.multiplication import multiplication
from Calculator.square_root import squareRoot
from StatisticsCalc.mean import mean
from StatisticsCalc.standard_deviation import standard_deviation

def confidenceIntervalTop (data, confidence_level):
    values = len(data)
    std = standard_deviation(data)
    avg = mean(data)
    rounded_interval = round(addition(avg, multiplication(confidence_level, division(std, squareRoot(values)))), 5)
    return rounded_interval