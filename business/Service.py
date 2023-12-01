# Made by Felipe Barbosa Figueira
import os

from matplotlib import pyplot as plt

from model.Record import Record
from persistence.DataStore import DataStore

"""
This class manages the core business logic related to handling records.
It interacts with the DataStore for data persistence and provides functionalities
to create, edit, delete, and reload records from a CSV file.

Attributes:
    datastore (DataStore): The datastore object for handling CSV file operations.
    records (list): A list of Record objects representing the current state of data.
"""

# Service class to handle business logic
class Service:
    def __init__(self):
        """
        Initializes the Service object, setting up the datastore and loading data asynchronously.
        """
        self.datastore = DataStore()
        self.records = []
        self.load_data_async()

    def reload_data(self):
        """
        Reloads data from the CSV file into the records list.
        """
        self.records = self.datastore.read_csv('../../data/travelq.csv')

    def save_data(self):
        """
        Saves current records to the CSV file.
        """
        self.datastore.save_csv('../../data/travelq.csv', self.records)


    def create_record(self, data):
        """
        Creates a new record from the given data and appends it to the records list.

        Args:
            data (dict): A dictionary containing data for the new record.
        """
        new_record = Record(data)
        self.records.append(new_record)

    def edit_record(self, index, new_data):
        """
        Edits an existing record in the records list at the specified index with the provided new data.

        Args:
            index (int): The index of the record to be edited.
            new_data (dict): A dictionary containing updated data for the record.
        """
        for k, v in new_data.items():
            setattr(self.records[index], k, v)

    def delete_record(self, index):
        """
        Deletes a record from the records list at the specified index.

        Args:
            index (int): The index of the record to be deleted.
        """
        del self.records[index]


    def load_data_async(self):
        """
        Initiates asynchronous loading of data from the CSV file.
        """
        print("Current WD:", os.getcwd())
        print("Absolute path:", os.path.abspath('data/travelq.csv'))

        self.datastore.async_read_csv('../../data/travelq.csv', self._update_records)

    def _update_records(self, records):
        """
        Private helper method to update the records list with asynchronously loaded data.

        Args:
            records (list): A list of Record objects to update the current records list.
        """
        self.records = records
        if os.environ.get('TESTING') != 'True':
            print("Records updated asynchronously.")

    def get_column_data(self, column_name):
        """
        Gathers data for a specific column to generate charts.

        Args:
            column_name (str): The name of the column.

        Returns:
            dict: A dictionary with unique values as keys and their occurrences as values.
        """
        column_data = {}
        for record in self.records:
            value = getattr(record, column_name, None)
            if value:
                column_data[value] = column_data.get(value, 0) + 1
        return column_data

    def column_exists(self, column_name):
        """
        Checks if a column exists in the record data.

        Args:
            column_name (str): The name of the column.

        Returns:
            bool: True if column exists, False otherwise.
        """
        if self.records:
            return hasattr(self.records[0], column_name)
        return False

    def get_column_data(self, column_name):
        """
        Gathers data for a specific column to generate charts.

        Args:
            column_name (str): The name of the column.

        Returns:
            dict: A dictionary with unique values as keys and their occurrences as values.
        """
        column_data = {}
        for record in self.records:
            value = getattr(record, column_name, None)
            if value:
                column_data[value] = column_data.get(value, 0) + 1
        if not column_data:
            print(f"Column '{column_name}' exists but contains no data.")
        return column_data