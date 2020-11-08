from Calculator.addition import addition
from Calculator.subtraction import subtraction
from Calculator.multiplication import multiplication
from Calculator.division import division
from Calculator.square import square

def cochran_sample_size(data,confidenceLevel, confidencelevelZscore, testVaribility):
    numvalues = len(data)
    precision = subtraction(1.00,confidenceLevel)
    z = confidencelevelZscore
    p = testVaribility
    recommendation = division(multiplication(square(z), multiplication(p, p)), square(precision))
    cochran = division(recommendation, addition (1, (division(subtraction(recommendation, 1),numvalues))))

    return cochran




