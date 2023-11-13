import os

import pytest
from persistence.DataStore import DataStore
from business.Service import Service
import time


def test_read_csv_file_not_found():
    """
    Tests the read_csv method of DataStore to ensure it handles file not found errors correctly.
    """
    datastore = DataStore()

    # Use a file name that does not exist
    filename = 'file_that_does_not_exist.csv'

    try:
        records = datastore.read_csv(filename)

        # The function should return an empty list if the file is not found
        assert records == []
    except FileNotFoundError:
        pytest.fail("FileNotFoundError was not caught by the program")


def test_async_data_load():
    """
    Tests the asynchronous data loading functionality of the Service class.
    """
    os.environ['TESTING'] = 'True'
    service = Service()
    time.sleep(4)  # Wait for the async load to complete
    assert len(service.records) > 0, "Records should be loaded asynchronously."
    os.environ['TESTING'] = 'False'

    print("Felipe Barbosa Figueira")
