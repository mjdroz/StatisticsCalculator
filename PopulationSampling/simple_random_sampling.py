from RandomGenerator.randomAmountSelection import randomAmountSelection

def simple_random_sampling(list, num):
    try:

        return_list = randomAmountSelection(list, num)
        return return_list

    except ValueError:
        print("ERROR: That is an emtpy list! Try again.")
