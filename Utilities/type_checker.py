def is_valid_number(number_as_string):
    if number_as_string.isnumeric():
        return True
    elif number_as_string[0] == "-":
        if number_as_string[1:].isnumeric():
            return True
        else:
            return False
    elif "." in number_as_string:
        if number_as_string.count(".") > 1:
            return False
        return True
    else:
        return False