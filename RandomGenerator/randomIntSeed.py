from numpy.random import randint
from numpy.random import seed

def randomIntSeed (start, end, s):
    seed(s)
    randIntSeed = randint(start, end)
    return randIntSeed