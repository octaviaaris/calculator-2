"""Math functions that take lsts containing any number of number inputs"""


def add(lst):
    if not lst:
        return []
    elif len(lst) == 1:
        return lst
    result = 0
    for i in lst:
        result += i
    return result


def subtract(lst):
    if not lst:
        return []
    elif len(lst) == 1:
        return lst
    else:
        result = lst[0]
        for i in lst:
            result -= i
        return result


def multiply(lst):
    if not lst:
        return []
    elif len(lst) == 1:
        return lst
    else:
        result = 1
        for i in lst:
            result *= i
        return result


def divide(lst):
    if not lst:
        return []
    elif len(lst) == 1:
        return lst
    else:
        result = lst[0]
        for i in range(1, len(lst)):
            result /= lst[i]
        return result


def square(lst):
    if not lst:
        return []
    else:
        squared_nums = []
        for i in lst:
            squared_nums.append(i * i)
        return squared_nums


def cube(lst):
    if not lst:
        return []
    else:
        cubed_nums = []
        for i in lst:
            cubed_nums.append(i**3)
        return cubed_nums
