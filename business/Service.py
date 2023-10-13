# Made by Felipe Barbosa Figueira
from model.Record import Record
from persistence.DataStore import DataStore

# Service class to handle business logic
class Service:
    def __init__(self):
        self.datastore = DataStore()
        self.records = self.datastore.read_csv('travelq.csv')
        print("Records: ", self.records)

    def reload_data(self):
        self.records = self.datastore.read_csv('travelq.csv')

    def save_data(self):
        self.datastore.save_csv('travelq.csv', self.records)

    def create_record(self, data):
        new_record = Record(data)
        self.records.append(new_record)

    def edit_record(self, index, new_data):
        for k, v in new_data.items():
            setattr(self.records[index], k, v)

    def delete_record(self, index):
        del self.records[index]