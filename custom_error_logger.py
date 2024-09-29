#Author: VS
#Script_name: custom_error_logger.py
#Description: This script functions as a simple calculator and logs all operations and errors to a file named error_log.txt with timestamps.

#!/usr/bin/env python3
# Import necessary modules
import datetime  # datetime provides functions to handle dates and times

#Function to log errors and operations to a file
def log_message(message):
    with open('error_log.txt', 'a') as log_file:
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_file.write(f"{timestamp} - {message}\n")

#Function to perform addition
def add(a, b):
    return a + b

#Function to perform subtraction
def subtract(a, b):
    return a - b

#Function to perform multiplication
def multiply(a, b):
    return a * b

#Function to perform division with error handling for division by zero
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        log_message("Error: Division by zero")
        print("Error: Division by zero is not allowed.")
        return None

#Main program execution
if __name__ == "_main_": # this block ensures that this conditional will run directly but not as a imported module in another script
    # Loop to continuously prompt the user for input until 'exit' is entered
    while True:
        print("Simple Calculator")
        print("Choose an operation: add, subtract, multiply, divide, or exit")
        operation = input("Enter operation: ").strip().lower()

        if operation == 'exit':
            break

        if operation not in ['add', 'subtract', 'multiply', 'divide']:
            print("Invalid operation. Please try again.")
            continue

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError as e:
            log_message(f"Error: Invalid input ({e})")
            print("Error: Invalid input. Please enter valid numbers.")
            continue

        result = None
        if operation == 'add':
            result = add(num1, num2)
        elif operation == 'subtract':
            result = subtract(num1, num2)
        elif operation == 'multiply':
            result = multiply(num1, num2)
        elif operation == 'divide':
            result = divide(num1, num2)

        if result is not None:
            log_message(f"Operation: {operation}, Numbers: {num1}, {num2}, Result: {result}")
            print(f"The result of {operation}ing {num1} and {num2} is: {result}")