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

from arithmetic2 import *

def calculator():
    """A REPL function that creates a prefix calculator"""

    def create_token(usr_input_string):
        """Turns users input into operator and list or nums"""

        token = usr_input_string.split("[")
        operator = token[0].strip()
        pre_lst1 = token[1].split("]")
        pre_lst2 = list(pre_lst1[0])
        str_lst = pre_lst2[0::3]
        lst = []

        # [lst.append(float(i)) for i in str_lst] #correct list comprehension

        for i in str_lst:
            lst.append(float(i))


        # calc_input = (operator, lst)

        return (operator, lst)

    while True:
        user_input = raw_input("> ")

        calc_input = create_token(user_input)

        if calc_input[0] == "q":
            return
        elif calc_input[0] == "+":
            result = add(calc_input[1])

        elif calc_input[0] == "-":
            result = subtract(calc_input[1])

        elif calc_input[0] == "*":
            result = multiply(calc_input[1])

        elif calc_input[0] == "/":
            result = divide(calc_input[1])

        elif calc_input[0] == "square":
            result = square(calc_input[1])

        elif calc_input[0] == "cube":
            result = cube(calc_input[1])

        elif calc_input[0] == "pow":
            result = power(calc_input[1])

        elif calc_input[0] == "mod":
            result = mod(calc_input[1])

        else:
            result = "Invalid Input"

        print result

calculator()