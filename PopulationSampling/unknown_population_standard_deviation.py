from Calculator.subtraction import subtraction
from Calculator.multiplication import multiplication
from Calculator.division import division
from Calculator.square import square

def unknown_pop_stand_deviation(data, confidenceZscore, marginOfError, percentSample):
    try:

        z = confidenceZscore
        if isinstance(marginOfError, float):
            moe = marginOfError
        else:
            moe = division(marginOfError, 100)
        if isinstance(percentSample, float):
            percent = percentSample
        else:
            percent = division(percentSample, 100)

        e = division(moe, 2)
        p = subtraction(1, percent)
        sample_muliply = multiplication(p, percent)
        z_by_e = division(z, e)
        squared = square(z_by_e)

        result = multiplication(sample_muliply, squared)
        return result

    except ValueError:
        print("ERROR: That is an emtpy list! Try again.")
