from business.Service import Service


class GUIHandler:
    """
    A handler class that serves as an intermediary between the GUI and the business logic.

    It utilizes the Service class to perform operations such as loading, saving, creating,
    editing, and deleting records, as well as retrieving specific data from the records.
    """
    def __init__(self):
        """Initializes the GUIHandler with a Service instance."""

        self.service = Service()

    def reload_data(self):
        """
        Reloads data from the underlying data store using the Service instance.

        Returns:
            list: A list of Record objects currently held by the Service instance.
        """
        self.service.reload_data()
        return self.service.records

    def save_data(self):
        """
        Saves the current state of data records through the Service instance.
        """
        self.service.save_data()

    def create_record(self, data):
        """
        Creates a new record with the provided data.

        Args:
            data (dict): The data for the new record.
        """
        self.service.create_record(data)

    def edit_record(self, index, new_data):
        """
        Edits an existing record identified by the index with new data.

        Args:
            index (int): The index of the record to be edited.
            new_data (dict): The new data for the record.
        """
        self.service.edit_record(index, new_data)

    def delete_record(self, index):
        """
        Deletes a record from the current record list at the specified index.

        Args:
            index (int): The index of the record to be deleted.
        """
        self.service.delete_record(index)

    def get_records(self):
        """
        Retrieves the current list of records.

        Returns:
            list: A list of Record objects.
        """
        return self.service.records

    def get_column_data(self, column_name):
        """
        Retrieves data for a specific column from the records.

        Args:
            column_name (str): The name of the column for which to retrieve data.

        Returns:
            dict: A dictionary with keys as unique values from the column and
                  values as their respective counts.
        """
        return self.service.get_column_data(column_name)
