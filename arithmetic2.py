"""Math functions that take lists containing any number of number inputs"""


def add(list):
    result = 0
    for i in list:
        result += i
    return result


def subtract(list):
    if len(list) == 0:
        return 0
    else:
        result = list[0]
        for i in list:
            result -= i
        return result


def multiply(list):
    if len(list) == 0:
        return 0
    else:
        result = 1
        for i in list:
            result *= i
        return result


def divide(list):
    if len(list) == 0:
        return 0
    elif len(list) == 1:
        return list[0]
    else:
        result = list[0]
        print range(len(list))
        for i in range(len(list)-1):
            result /= list[i+1]
        return result


def square(list):
    if len(list) == 0:
        return []
    else:
        squared_nums = []
        for i in list:
            squared_nums.append(i * i)
        return squared_nums


def cube(list):
    if len(list) == 0:
        return []
    else:
        cubed_nums = []
        for i in list:
            cubed_nums.append(i**3)
        return cubed_nums
