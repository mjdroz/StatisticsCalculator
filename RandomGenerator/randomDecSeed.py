from RandomGenerator.randomDec import randomDec
from numpy import random

def randomDecSeed(start, end, seed):
    state = random.get_state()
    random.seed(seed)
    try:
        randIntSeeded = randomDec(start, end)
        return randIntSeeded
    finally:
        random.set_state(state)