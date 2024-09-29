#Author: VS
#script_name: Even_filter.py
#description: This Script accepts a list of numbers and returns a list of even numbers found in the input list.


#!/usr/bin/env python3
import sys # sys module allow access to command line arguments and perform system related tasks
#Function declaration
def filter_even(numbers):
    #initialize an empty list to store even numbers
    even_numbers = []
    #looping through each number in the even list
    for number in numbers:
        # check if the num is divisible by 2
        if number % 2 == 0:
            #add the even number to the list
            even_numbers.append(number)
    #return list of even numbers
    return even_numbers

#main program execution
if __name__ == "__main__": # this block ensures the conditionals of the script are executed directly rather than importing them as a module for another script
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) < 2: # with sys.argv you can retrieve arguments passed to the script from the command line
        print("Usage: python Even_filter.py <num1> <num2> ...<numN>") #If there are not enough arguments, this line prints a usage message to inform the user how to run the script correctly.
    else:
        # Convert command-line arguments to a list of integers
        try:
            numbers = [int(arg) for arg in sys.argv[1:]] #convert each argument from the second element onward (excluding the script name which is the first element sys.argv[0]) to an integer.
        except ValueError:
            print("Error: All inputs must be integers")
            sys.exit(1)

        # Call the function to filter even numbers
        even_numbers = filter_even(numbers)

        # Print the original list and the filtered list of even numbers
        print("Original list:",numbers)
        print("Even numbers:",even_numbers)