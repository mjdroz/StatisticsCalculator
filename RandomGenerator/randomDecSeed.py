from RandomGenerator.randomDec import randomDec
from numpy import random

def randomDecSeed(start, end):
    state = random.get_state()
    random.seed(4)
    try:
        randIntSeeded = randomDec(start, end)
        return randIntSeeded
    finally:
        random.set_state(state)