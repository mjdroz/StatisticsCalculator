from RandomGenerator.randomDecSeed import randomDecSeed
from numpy import random

def random_num_generatorDecSeed(start, end, seed):
    s = seed
    st = start
    e = end
    return randomDecSeed(st, e, s)