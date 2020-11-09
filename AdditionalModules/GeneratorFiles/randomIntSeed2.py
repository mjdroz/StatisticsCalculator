from RandomGenerator.randomIntSeed import randomIntSeed
from RandomGenerator.randomDecSeed import randomDecSeed
from numpy import random

def random_num_generatorIntSeed(start, end, seed):
    s = seed
    st = start
    e = end
    return randomIntSeed(st, e, s)
