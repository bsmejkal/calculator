"""A prefix-notation calculator.
    
Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
while True:

    input_string = input(">")
    tokens = input_string.split(" ")

    num1 = float(tokens[1])
    
    if len(tokens) > 2:
        num2 = float(tokens[2])

    operand = tokens[0]

    if operand == "q":
        break

    else:

        if operand == "+":
            print(add(num1, num2))

        elif operand == "-":
            print(subtract(num1, num2))

        elif operand == "*":
            print(multiply(num1, num2))

        elif operand == "/":
            print(divide(num1, num2))

        elif operand == "square":
            print(square(num1))

        elif operand == "cube":
            print(cube(num1))

        elif operand == "pow":
            print(power(num1, num2))

        elif operand == "mod":
            print(mod(num1, num2))
