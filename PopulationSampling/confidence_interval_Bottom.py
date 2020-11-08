from Calculator.division import division
from Calculator.subtraction import subtraction
from Calculator.multiplication import multiplication
from Calculator.square_root import squareRoot
from StatisticsCalc.mean import mean
from StatisticsCalc.standard_deviation import standard_deviation
from scipy import stats

def confidenceIntervalBottom (data, confidence_level):
    values = len(data)
    std = standard_deviation(data)
    avg = mean(data)
    rounded_interval = stats.norm.interval(confidence_level, avg, division(std,squareRoot(values)))
    intervalBottom = round(rounded_interval[0], 5)
    # rounded_interval = round(subtraction(avg,multiplication(confidence_level,division(std,squareRoot(values)))), 5)
    return intervalBottom

