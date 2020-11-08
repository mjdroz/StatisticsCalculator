from Calculator.division import division
from Calculator.square_root import squareRoot
from StatisticsCalc.mean import mean
from StatisticsCalc.standard_deviation import standard_deviation
from scipy import stats

def confidenceIntervalTop (data, confidence_level):
    values = len(data)
    std = standard_deviation(data)
    avg = mean(data)
    rounded_interval = stats.norm.interval(confidence_level, avg, division(std, squareRoot(values)))
    intervalBottom = round(rounded_interval[1], 5)
    return intervalBottom