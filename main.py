# Day 10 – Calculator Project
# Part of my 100 Days of Code journey
#
# Learning goals for this project:
# - Defining and using functions
# - Storing functions inside dictionaries
# - Calling functions dynamically based on user input
# - Using while loops to control program flow
# - Reusing results for continuous calculations
# - Clearing the console for a clean user experience
#
# This project simulates a basic calculator that can
# chain multiple calculations together.

import os
from art import logo


def add(n1, n2):
    # Adds two numbers
    return n1 + n2


def subtract(n1, n2):
    # Subtracts second number from first
    return n1 - n2


def multiply(n1, n2):
    # Multiplies two numbers
    return n1 * n2


def divide(n1, n2):
    # Divides first number by second
    return n1 / n2


# Dictionary that maps symbols to functions
operations = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply
}


def calc():
    # Controls one full calculation session
    calculation_on = True
    print(logo)

    # Ask for the first number
    num_1 = float(input("What's the first number?: "))

    while calculation_on:
        # Show available operations
        cal_func = input("+\n-\n*\n/\nPick an operation: ")

        # Ask for the next number
        num_2 = float(input("What's the next number?: "))

        # Call the selected function from the dictionary
        result_1 = operations[cal_func](num_1, num_2)

        # Display result
        print(f"{num_1} {cal_func} {num_2} = {result_1}")

        # Ask if user wants to continue with the result
        continue_cal = input(
            f"Type 'y' to continue calculating with {result_1}, or type 'n' to start a new calculation: "
        )

        if continue_cal == "y":
            # Use the result as the first number for next calculation
            num_1 = result_1
        else:
            # Clear screen and restart calculator
            os.system('cls')
            calculation_on = False
            calc()


# Start the calculator
calc()
