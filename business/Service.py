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
        self.records = self.datastore.read_csv('travelq.csv')

    def save_data(self):
        """
        Saves current records to the CSV file.
        """
        self.datastore.save_csv('travelq.csv', self.records)

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

    def generate_chart(self):
        print("1: Horizontal Bar Chart\n2: Vertical Bar Chart\n3: Pie Chart")
        chart_choice = input("Select chart type: ")
        column_name = input("Enter column name for chart data: ")

        if chart_choice == '1':
            self.create_horizontal_bar_chart(column_name)
        elif chart_choice == '2':
            self.create_vertical_bar_chart(column_name)
        elif chart_choice == '3':
            self.create_pie_chart(column_name)

    def create_horizontal_bar_chart(self, column_name):
        data = self.service.get_column_data(column_name)
        plt.barh(list(data.keys()), list(data.values()))
        plt.xlabel('Count')
        plt.ylabel(column_name)
        plt.title('Horizontal Bar Chart')
        plt.show()

    def create_vertical_bar_chart(self, column_name):
        data = self.service.get_column_data(column_name)
        plt.bar(list(data.keys()), list(data.values()))
        plt.xlabel(column_name)
        plt.ylabel('Count')
        plt.title('Vertical Bar Chart')
        plt.show()

    def create_pie_chart(self, column_name):
        data = self.service.get_column_data(column_name)
        plt.pie(list(data.values()), labels=list(data.keys()), autopct='%1.1f%%')
        plt.title('Pie Chart')
        plt.show()

    def load_data_async(self):
        """
        Initiates asynchronous loading of data from the CSV file.
        """
        self.datastore.async_read_csv('travelq.csv', self._update_records)

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