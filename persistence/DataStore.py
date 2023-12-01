# Made by Felipe Barbosa Figueira

# Importing required modules demonstrates modular programming.
import csv
import threading

from model.Record import Record
import os

# DataStore Class demonstrates Object-Oriented Programming (OOP)
class DataStore:
    """
    Handles data storage operations, particularly for reading and writing CSV files.

    This class provides methods to read from and write to CSV files, and to
    perform these operations asynchronously.

    Methods:
    - read_csv: Reads records from a CSV file and returns them.
    - save_csv: Saves records to a CSV file.
    - async_read_csv: Performs asynchronous reading of a CSV file.
    """
    def read_csv(self, filename):
        """
        Reads records from a specified CSV file.

        Args:
            filename (str): The name of the file to read from.

        Returns:
            list: A list of Record objects read from the file.
        """
        records = []
        full_path = os.path.join(os.getcwd(), filename)
        if not os.path.exists(full_path):
            print(f"File does not exist: {full_path}")
            return []
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
        """
        Saves given records to a specified CSV file.

        Args:
            filename (str): The name of the file to write to.
            records (list): A list of Record objects to be saved.
        """
        keys = vars(records[0]).keys()
        with open(filename, 'w') as output_file:
            dict_writer = csv.DictWriter(output_file, fieldnames=keys)
            dict_writer.writeheader()
            for record in records:
                dict_writer.writerow(vars(record))

    def async_read_csv(self, filename, callback):
        """
        Initiates an asynchronous operation to read records from a CSV file.

        Args:
            filename (str): The name of the file to read from.
            callback (function): The callback function to be executed after completion of the read operation.
        """
        print(os.getcwd())
        thread = threading.Thread(target=self._threaded_read_csv, args=(filename, callback))
        thread.start()

    def _threaded_read_csv(self, filename, callback):
        """
        Private helper method to perform the threaded reading operation of a CSV file.

        Args:
            filename (str): The name of the file to read from.
            callback (function): The callback function to be executed after completion of the read operation.
        """
        records = self.read_csv(filename)
        callback(records)