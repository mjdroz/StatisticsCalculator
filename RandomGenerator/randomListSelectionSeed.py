from numpy import random
from RandomGenerator.randomListSelection import randomListSelection

def randomListSelectionSeed(list, seed):
    state = random.get_state()
    random.seed(seed)
    try:
        seeded_selection = randomListSelection(list)
        return seeded_selection
    finally:
        random.set_state(state)