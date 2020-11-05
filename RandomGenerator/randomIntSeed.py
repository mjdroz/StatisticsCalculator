from RandomGenerator.randomInt import randomInt
from numpy import random

def randomIntSeed (start, end, seed):
    state = random.get_state()
    random.seed(seed)
    try:
        randIntSeeded = randomInt(start, end)
        return randIntSeeded
    finally:
        random.set_state(state)
