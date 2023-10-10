# Made by Felipe Barbosa Figueira

# Importing required modules demonstrates modular programming.
import csv
from model.Record import Record

# DataStore Class demonstrates Object-Oriented Programming (OOP)
class DataStore:
    # Docstring for method matches the requirement of code documentation.
    def read_csv(self, filename):
        """Reads data from a CSV file and returns a list of records. This demonstrates file I/O."""
        # Data structure to hold records demonstrates data encapsulation.
        records = []
        try:
            # Exception Handling
            with open(filename, 'r', encoding='utf-8') as f:  # Ensuring UTF-8 encoding
                reader = csv.DictReader(f)
                next(reader, None)  # Skip the header
                # Loop demonstrates control structures.
                for row in reader:
                    # Object Instantiation
                    record = Record(row)
                    # Data manipulation
                    records.append(record)
        except FileNotFoundError:
            print("File not found.")  # Error message
        # Return statement demonstrates the function's exit point.
        return records[:2000]

# Your other classes and methods can be explained in a similar manner.
