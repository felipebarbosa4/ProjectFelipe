# Made by Felipe Barbosa Figueira

from business.Service import Service
from model.Record import Record


# ConsoleView class for presentation layer
class ConsoleView:
    def __init__(self):
        self.service = Service()

    def display_name(self):
        print("Felipe Barbosa Figueira")

    def display_data(self):
        for i, record in enumerate(self.service.records):
            print(f"{i}: {record}")

    def main_menu(self):
        while True:
            self.display_name()
            print(
                "1: Reload Data\n2: Save Data\n3: Create Record\n4: Edit Record\n5: Delete Record\n6: Show Records\n7: Exit")
            choice = input("Choice: ")
            if choice == '1':
                self.service.reload_data()
            elif choice == '2':
                self.service.save_data()
            elif choice == '3':
                data = {}
                field_names = ['ref_number', 'disclosure_group', 'title_en', 'title_fr', 'name', 'purpose_en', 'purpose_fr', 'start_date', 'end_date', 'destination_en', 'destination_fr', 'airfare', 'other_transport', 'lodging', 'meals', 'other_expenses', 'total', 'additional_comments_en', 'additional_comments_fr', 'owner_org', 'owner_org_title']
                for field in field_names:
                    data[field] = input(f"Enter {field}: ")
                self.service.create_record(data)
            elif choice == '4':
                ref_number_to_edit = input("Enter the reference number you wish to edit: ")

                # Check if ref_number exists in the current records
                index_to_edit = None
                for i, record in enumerate(self.service.records):
                    if record.ref_number == ref_number_to_edit:
                        index_to_edit = i
                        break

                if index_to_edit is None:
                    print("This reference number does not exist. Please choose a valid reference number.")
                    continue

                new_data = {}
                field_names = ['ref_number', 'disclosure_group', 'title_en', 'title_fr', 'name', 'purpose_en',
                               'purpose_fr', 'start_date', 'end_date', 'destination_en', 'destination_fr', 'airfare',
                               'other_transport', 'lodging', 'meals', 'other_expenses', 'total',
                               'additional_comments_en', 'additional_comments_fr', 'owner_org', 'owner_org_title']
                for field in field_names:
                    new_value = input(f"Enter new value for {field} (press Enter to keep current): ")
                    if new_value:  # Check if user has entered a value; if not, keep the current one
                        new_data[field] = new_value
                self.service.edit_record(index_to_edit, new_data)
            elif choice == '5':
                index = int(input("Index: "))
                self.service.delete_record(index)
            elif choice == '6':
                self.display_data()
            elif choice == '7':
                break