from numpy import random

def randomListSelection (list):
    try:
        rand_selection = random.choice(list)
        return rand_selection
    except ValueError as error:
        error = "ERROR: That is an empty list! Try again."
        return error
