from numpy import random
from RandomGenerator.randomListSelection import randomListSelection

def randomListSelectionSeed(list):
    state = random.get_state()
    random.seed(7)
    try:
        seeded_selection = randomListSelection(list)
        return seeded_selection
    finally:
        random.set_state(state)