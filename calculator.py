"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""


# repeat forever:
#     read input
#     tokenize input
#     if the first token is "q":
#         quit
#     else:
#         decide which math function to call based on first token

from arithmetic import *


def calculator():
    """A REPL function that creates a prefix calculator"""

    def create_token(usr_input_string):
        token = string.split("[")
        operator = token[0].strip()
        pre_lst1 = token[1].split("]")
        pre_lst2 = list(pre_lst[0])
        lst = pre_lst2[0::3]

        calc_input = (operator, lst)

        return calc_input


    while True:
        user_input = raw_input("> ")
        # token = user_input.split('[')
        # token
        # for i in token

        create_token(user_input)

        if token[0].strip() == "q":
            return
        elif token[0].strip() == "+":
            result = add(float(token[1]), float(token[2]))

        elif token[0].strip() == "-":
            result = subtract(float(token[1]), float(token[2]))

        elif token[0].strip() == "*":
            result = multiply(float(token[1]), float(token[2]))

        elif token[0].strip() == "/":
            result = divide(float(token[1]), float(token[2]))

        elif token[0].strip() == "square":
            result = square(float(token[1]))

        elif token[0].strip() == "cube":
            result = cube(float(token[1]))

        elif token[0].strip() == "pow":
            result = power(float(token[1]), float(token[2]))

        elif token[0].strip() == "mod":
            result = mod(float(token[1]), float(token[2]))

        else:
            result = "Invalid Input"

        print result

calculator()

+ [12, 3, 4]