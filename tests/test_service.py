import pytest
from persistence.DataStore import DataStore


def test_read_csv_file_not_found():
    datastore = DataStore()

    # Use a file name that does not exist
    filename = 'file_that_does_not_exist.csv'

    try:
        records = datastore.read_csv(filename)

        # The function should return an empty list if the file is not found
        assert records == []
    except FileNotFoundError:
        pytest.fail("FileNotFoundError was not caught by the program")

    print("Felipe Barbosa Figueira")
