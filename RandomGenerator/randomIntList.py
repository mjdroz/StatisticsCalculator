from numpy import random

def randomIntList (start, end, length, seed):
    state = random.get_state()
    random.seed(seed)
    try:
        int_list = random.randint(start, end, length)
        return int_list
    finally:
        random.set_state(state)