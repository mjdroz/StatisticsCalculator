from StatisticsCalc.mean import mean
from Calculator.square import square
from Calculator.division import division

def variance(data):
    try:
        mean_of_data = mean(data)
        total_values = len(data)
        ph = 0
        for a in data:
            ph = ph + square(a - mean_of_data)
        result = division(ph, total_values)

        return result

    except ValueError:
        print("ERROR: That is an emtpy list! Try again.")


# RENAME ph VARIABLE - Michael 11/5