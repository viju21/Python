#Author: VS
#Script_name: Line_counter.py
#Description: The script should accept a filename as a command-line argument, count the number of lines in the file, and print the count.

#Shebang ensures the script runs with python3 in unix like env
#!/usr/bin/env python3  

import sys  # sys provides access to command-line arguments and other system-related functions.

# Function definition
def count_lines(filename):
    # Try block to handle file reading
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            return len(lines)
    # Except block 1 for file not found
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return None
    # Except block 2 for other exceptions
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Main Program Execution
if __name__=="_main_": #ensures the script is being run directly as a main script or being imported as module
    if len(sys.argv) != 2: # Checks the number of command-line arguments must be 2 
        print("Usage: python line_counter.py <filename>")
    else:
        filename = sys.argv[1]  # Assigns the filename from the command-line arguments; 0-argument(script name) and 1-argument(i.e,filename)
        line_count = count_lines(filename)
        if line_count is not None:
            print(f"The file '{filename}' has {line_count}lines.") #output}