from numpy import random

def randomDecList (start, end, length, seed):
    state = random.get_state()
    random.seed(seed)
    try:
        dec_list = random.uniform(start, end, length)
        return dec_list
    finally:
        random.set_state(state)