
def typeCheck(dict):
    for row in dict:
        for value in row:
            num = row[value]
            for char in num:
                if char == '-' or char == '.':
                    return
                elif char.isalpha():
                    raise ValueError("ERROR: Value is not a valid number! Try again.")
                else:
                    return
