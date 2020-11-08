from collections import Counter

def mode (data):
    try:
        total_values = len(data)
        count = Counter(data)
        get_mode = dict(count)
        mode = [a for a, v in get_mode.items() if v == max(list(count.values()))]

        if len(mode) == total_values:
            get_mode = "Mode was not found"

        else:
            get_mode = mode[0]

        return (get_mode)

    except ValueError:
        print("ERROR: That is an emtpy array! Try again.")