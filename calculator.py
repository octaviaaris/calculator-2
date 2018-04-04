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
    while True:
        user_input = raw_input("> ")
        token = user_input.split(' ')
        if token[0] == "q":
            return
        elif token[0] == "+":
            result = add(float(token[1]), float(token[2]))
            print result
        elif token[0] == "-":
            result = subtract(float(token[1]), float(token[2]))
            print result
        elif token[0] == "*":
            result = multiply(float(token[1]), float(token[2]))
            print result
        elif token[0] == "/":
            result = divide(float(token[1]), float(token[2]))
            print result
        elif token[0] == "square":
            result = square(float(token[1]))
            print result
        elif token[0] == "cube":
            result = cube(float(token[1]))
            print result
        elif token[0] == "pow":
            result = power(float(token[1]), float(token[2]))
            print result
        elif token[0] == "mod":
            result = mod(float(token[1]), float(token[2]))
            print result


calculator()
