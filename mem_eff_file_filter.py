# Author: VS
# Script_name: mem_eff_file_filter.py
# Description: This script reads a CSV file, filters records by a specified year, and writes the filtered data to a new CSV file.

#!/usr/bin/env python3
import csv
from datetime import datetime

def read_csv(file_path):
    with open(file_path, mode='r', newline='') as csvfile: #Read a CSV file and strip whitespace from headers and values.
        reader = csv.DictReader(csvfile)
        # Clean the headers
        reader.fieldnames = [field.strip() for field in reader.fieldnames]
        print(f"Headers: {reader.fieldnames}")  
        for row in reader:
            # Clean the row values
            cleaned_row = {key.strip(): value.strip() for key, value in row.items()}
            yield cleaned_row

def filter_by_year(records, year):    #Filter records by a specific year.
    for row in records:
        try:
            row_date = datetime.strptime(row['date'], '%Y-%m-%d')
            if row_date.year == year:
                yield row
        except KeyError as e:
            print(f"KeyError: {e} in row: {row}")  
        except ValueError as e:
            print(f"ValueError: {e} in row: {row}")  

def write_csv(records, output_file, fieldnames):        #Write filtered records to a new CSV file
    with open(output_file, mode='w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in records:
            writer.writerow(row)

def main():
    # Input and output CSV file paths
    input_file = 'sales_data.csv'
    output_file = 'filtered_sales_data.csv'

    # Get the year from the user
    year = int(input("Enter the year to filter records by (e.g., 2021): "))

    # Read and process the CSV file
    records = read_csv(input_file)

    # Extract header from the first record
    first_record = next(records, None)
    if not first_record:
        print("No records found in the CSV file.")
        return

    header = first_record.keys()

    # Filter records by the specified year
    filtered_records = filter_by_year([first_record], year) if datetime.strptime(first_record['date'], '%Y-%m-%d').year == year else []
    filtered_records = list(filtered_records) + list(filter_by_year(records, year))

    # Write the filtered records to a new CSV file
    write_csv(filtered_records, output_file, header)

# Main program execution
if __name__ == "__main__":
    main()
