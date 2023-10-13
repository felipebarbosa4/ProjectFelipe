# Made by Felipe Barbosa Figueira

# Importing required modules demonstrates modular programming.
import csv
from model.Record import Record
import os

# DataStore Class demonstrates Object-Oriented Programming (OOP)
class DataStore:
    # Docstring for method matches the requirement of code documentation.
    def read_csv(self, filename):
        records = []

        try:
            with open(filename, 'r', encoding='ansi') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    record = Record(row)
                    records.append(record)
        except FileNotFoundError:
            print("File not found.")
        return records[:100]

    def save_csv(self, filename, records):
        keys = vars(records[0]).keys()
        with open(filename, 'w') as output_file:
            dict_writer = csv.DictWriter(output_file, fieldnames=keys)
            dict_writer.writeheader()
            for record in records:
                dict_writer.writerow(vars(record))