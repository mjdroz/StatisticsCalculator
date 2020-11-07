from StatisticsCalc.variance import variance
from Calculator.square_root import squareRoot

def standard_deviation(data):
    try:
        variance_of_data = variance(data)
        return squareRoot(variance_of_data)

    except ValueError:
        print("ERROR: That is an emtpy list! Try again.")
