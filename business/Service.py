# Made by Felipe Barbosa Figueira

from persistence.DataStore import DataStore

# Service class to handle business logic
class Service:
    def __init__(self):
        """Initializer method, demonstrates constructors in OOP."""
        self.datastore = DataStore()

    def get_data(self):
        """Business logic method."""
        return self.datastore.read_csv('./travelq.csv')