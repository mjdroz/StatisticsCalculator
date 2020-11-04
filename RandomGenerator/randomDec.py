from numpy.random import uniform

def randomDec (start, end):
    rand = uniform(start, end)
    rounded_num = round(rand, 2)
    return rounded_num