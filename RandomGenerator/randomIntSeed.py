from RandomGenerator.randomInt import randomInt
from numpy import random

def randomIntSeed (start, end):
    state = random.get_state()
    random.seed(7)
    try:
        randIntSeeded = randomInt(start, end)
        return randIntSeeded
    finally:
        random.set_state(state)
