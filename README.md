# Project-10---Calculator

This is a beginner Python project built as part of my 100 Days of Code challenge.

The goal of this project is to build a console-based calculator that can perform chained calculations using basic arithmetic operations.

**Project Overview**

The Calculator allows the user to:

Enter a starting number

Choose an operation

Enter another number

See the calculated result

Continue calculating using the previous result or start fresh

Supported operations:

Addition

Subtraction

Multiplication

Division

**Project File Structure**

main.py
Contains the calculator logic, arithmetic functions, and user interaction.

art.py
Stores the ASCII art logo displayed at program start.

**Why this project exists**

This project helped me understand how functions can be treated as values and stored inside data structures.

It also introduced the concept of chaining calculations — similar to how real calculators work.

**What I learned**

How to define and reuse functions

How to store functions inside dictionaries

How to dynamically call functions based on user input

How to manage program state using while loops

How to reuse previous results for continuous calculations

How to restart a program cleanly

**How the code works (step-by-step)**

Display the calculator logo

Ask the user for the first number

Show available mathematical operations

Ask the user to select an operation

Ask for the next number

Perform the calculation using a function stored in a dictionary

Display the result

Ask if the user wants to continue or start over

Repeat until the user exits

**Example Output**

What's the first number?:
10

Pick an operation:
+

What's the next number?:
5

10 + 5 = 15

Type 'y' to continue calculating with 15, or type 'n' to start a new calculation:
y

Pick an operation:
*

What's the next number?:
2

15 * 2 = 30
