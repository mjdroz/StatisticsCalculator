from StatisticsCalc.mean import mean
from StatisticsCalc.standard_deviation import standard_deviation
from Calculator.division import division
from Calculator.subtraction import subtraction

def z_score(data):
    try:
        zscore_list = []

        for x in data:
            zmean = mean(data)
            standard_dev = standard_deviation(data)
            diff = subtraction(x, zmean)
            z = division(diff, standard_dev)
            roundedz = round(z, 5)
            zscore_list.append(roundedz)

        return zscore_list

    except ValueError:
        print("ERROR: That is an emtpy list! Try again.")