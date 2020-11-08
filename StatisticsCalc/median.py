from Calculator.division import division
from Calculator.subtraction import subtraction
from Calculator.addition import addition

def median(data):
    try:
        total_values = len(data)
        list_of_nums = [data[i] for i in range(total_values)]
        list_of_nums.sort()
        if total_values % 2 == 0:
            median1 = list_of_nums[int(total_values // 2)]
            median2 = list_of_nums[int(subtraction((total_values // 2), 1))]
            result = division(addition(median1, median2), 2)
        else:
            result = list_of_nums[int(division(total_values, 2))]
        return result
    except ValueError:
        print("ERROR: That is an emtpy array! Try again.")