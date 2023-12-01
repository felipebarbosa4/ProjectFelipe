from business.Service import Service


class GUIHandler:
    def __init__(self):
        self.service = Service()

    def reload_data(self):
        self.service.reload_data()
        return self.service.records

    def save_data(self):
        self.service.save_data()

    def create_record(self, data):
        self.service.create_record(data)

    def edit_record(self, index, new_data):
        self.service.edit_record(index, new_data)

    def delete_record(self, index):
        self.service.delete_record(index)

    def get_records(self):
        return self.service.records

    def get_column_data(self, column_name):
        return self.service.get_column_data(column_name)
