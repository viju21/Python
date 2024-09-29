# Author: VS
# Script_name: match_case_handler.py
# Description: This script prompts the user to enter commands ('start', 'stop', 'exit') and uses a match-case statement to execute different actions (print statements) for each command.

#!/usr/bin/env python3.10

import sys  # sys module allows access to command-line arguments and perform system related tasks

# Function definition to handle commands
def handle_command(command):
    # Match-case statement to handle different commands
    match command:
        case 'start':
            print("Command received: start")
            print("Starting the process...")
        case 'stop':
            print("Command received: stop")
            print("Stopping the process...")
        case 'exit':
            print("Command received: exit")
            print("Exiting the program...")
            sys.exit(0)
        case _:
            print(f"Unrecognized command: '{command}'. Please enter 'start', 'stop', or 'exit'.")

# Main program execution
if __name__ == "__main__":
    # Loop to continuously prompt the user for commands until 'exit' is entered
    while True:
        # Prompt the user to enter a command
        command = input("Enter command ('start', 'stop', 'exit'): ")
        # Call the function to handle the entered command
        handle_command(command)
