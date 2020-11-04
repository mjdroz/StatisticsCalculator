from numpy import random

def randomIntList (start, end, length):
    state = random.get_state()
    random.seed(7)
    try:
        int_list = random.randint(start, end, length)
        return int_list
    finally:
        random.set_state(state)