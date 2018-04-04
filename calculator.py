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


calculator()