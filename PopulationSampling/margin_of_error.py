from StatisticsCalc.standard_deviation import standard_deviation
from Calculator.square_root import squareRoot
from Calculator.division import division
from Calculator.multiplication import multiplication

def margin_of_error (data, confidence_Zscore):
    size = len(data)
    std = standard_deviation(data)
    z = confidence_Zscore
    moe = multiplication(z, division(std, squareRoot(size)))
    return round(moe, 5)
