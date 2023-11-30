# Made by Felipe Barbosa Figueira
class Record:
    """
    Represents a single record of data with various attributes.

    This class is used to create objects that store individual records of data,
    each attribute representing a different data field.

    Args:
        data (dict): A dictionary representing the data fields and their values for the record.
    """

    def search_records(records, search_criteria):
        # search_criteria is a dict: {'column_name': 'value_to_search', ...}
        filtered_records = [record for record in records if
                            all(record[column] == value for column, value in search_criteria.items())]
        return filtered_records

    def __init__(self, data):
        """
        Initializes the Record object with data provided in the dictionary.
        """
        self.ref_number = data['ref_number']
        for k, v in data.items():
            setattr(self, k, v)

    def __str__(self):
        """
        Provides a string representation of the Record object.

        Returns:
            str: A string representation of the record's data fields and values.
        """
        return str(self.__dict__)