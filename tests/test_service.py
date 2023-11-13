import os
from unittest.mock import patch

import pytest

from model.Record import Record
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


def mock_read_csv(filename):
    return [Record({'ref_number': '001', 'name': 'Test Record'})]

@patch('persistence.DataStore.DataStore.read_csv', side_effect=mock_read_csv)
def test_async_data_load(mocked_read_csv):
    os.environ['TESTING'] = 'True'
    service = Service()

    assert len(service.records) > 0, "Records should be loaded asynchronously."
    os.environ['TESTING'] = 'False'
    print("\nFelipe Barbosa Figueira")

print("Felipe Barbosa Figueira")
