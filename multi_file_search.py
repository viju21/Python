# Author: VS
# Script_name: multi_file_search.py
# Description: This script searches for a specific string in all .txt files within a specified directory and prints the names of the files containing the string.

#!/usr/bin/env python3

#Importing modules
import os  # Module to interact with the operating system
import sys  # Module to access command-line arguments

#Function to search for a specific string in a given file.
def search_string_in_file(file_path, search_string):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if search_string in line:
                    return True
        return False
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return False
    
#Function to search for a specific string in all .txt files within a specified directory.
def search_files_in_directory(directory, search_string):  
    matching_files = []

    try:
        for filename in os.listdir(directory):
            if filename.endswith('.txt'):
                file_path = os.path.join(directory, filename)
                if search_string_in_file(file_path, search_string):
                    matching_files.append(filename)
    except Exception as e:
        print(f"Error accessing directory {directory}: {e}")

    return matching_files

# Main Program Execution
if __name__ == "_main_":
    if len(sys.argv) != 3:
        print("Usage: python multi_file_search.py <directory> <search_string>")
    else:
        directory = sys.argv[1]
        search_string = sys.argv[2]

        matching_files = search_files_in_directory(directory, search_string)

        if matching_files:
            print("Files containing the search string:")
            for file in matching_files:
                print(file)
        else:
            print("No files found containing the search string.")