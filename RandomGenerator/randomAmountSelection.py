from numpy import random

def randomAmountSelection (list, num_values):
    try:
        return_values = []
        for num in range(num_values):
            rand_selection = random.choice(list)
            return_values.append(rand_selection)
        return return_values

    except ValueError as error:
        error = "ERROR: That is an empty array! Try again."
        return error