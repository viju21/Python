# Author: VS
# Script_name: square_numbers.py
# Description: This script demonstrates the use of list comprehensions and generator expressions to create a list of squares of numbers from 1 to 20.

#!/usr/bin/env python3
# List Comprehension
def list_comprehension():
    # Create a list of squares using a list comprehension
    squares_list = [x ** 2 for x in range(1, 20)]
    # Print the list of squares
    print("List of squares using list comprehension:")
    print(squares_list)

# Generator Expression
def generator_expression():
    # Create a generator expression for squares
    squares_generator = (x ** 2 for x in range(1, 20))
    # Print each square value by iterating over the generator
    print("Squares using generator expression:")
    for square in squares_generator:
        print(square)

# Main program execution
if __name__ == "_main_":
    # Call the list comprehension function
    list_comprehension()
    # Call the generator expression function
    generator_expression()