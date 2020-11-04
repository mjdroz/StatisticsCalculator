from numpy import random
from RandomGenerator.randomAmountSelection import randomAmountSelection

def randomAmountSelectionSeed (list, num_values):
    state = random.get_state()
    random.seed(7)
    try:
        selection = randomAmountSelection(list, num_values)
        return selection
    finally:
        random.set_state(state)