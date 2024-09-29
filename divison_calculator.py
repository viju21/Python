#Author: VS
#Script_name: Divison_calculator.py
#description: This script that asks for two numbers from the user and attempts to divide the first by the second. Handle any potential exceptions (e.g., division by zero, input that isn't a number) gracefully, informing the user of the error.

#!/usr/bin/env python3
# Import necessary modules
import sys  # sys provides access to command-line arguments and other system-related functions

# Function definition to perform division
def perform_division():
    # Prompt the user to enter the first number
    while True:
        try:
            num1 = float(input("Enter the first number: "))  # Convert user input to a floating-point number
            break  # Break out of the loop if input is valid
        except ValueError:
            print("Error: Please enter a valid number.")

    # Prompt the user to enter the second number
    while True:
        try:
            num2 = float(input("Enter the second number: "))  # Convert user input to a floating-point number
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                break  # Break out of the loop if input is valid
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")

    # Attempt division and handle potential exceptions
    try:
        result = num1 / num2
        print(f"The result of dividing {num1} by {num2} is: {result}")
    except Exception as e:
        print(f"Error: {e}")

# Main program execution
if __name__ == "_main_":
    # Call the function to perform division
    perform_division()