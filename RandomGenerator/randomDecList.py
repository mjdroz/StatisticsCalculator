from numpy import random

def randomDecList (start, end, length):
    state = random.get_state()
    random.seed(4)
    try:
        dec_list = random.uniform(start, end, length)
        return dec_list
    finally:
        random.set_state(state)