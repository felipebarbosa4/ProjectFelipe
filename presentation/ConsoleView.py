# Made by Felipe Barbosa Figueira
from matplotlib import pyplot as plt

from business.Service import Service
from model.Record import Record


# ConsoleView class for presentation layer
class ConsoleView:
    """
    Provides a console-based user interface for interacting with the Service class.

    This class acts as a presentation layer, allowing users to interact with the application
    through a series of console-based menus and prompts.

    Methods:
    - display_name: Displays the creator's name.
    - display_data: Prints all records currently loaded.
    - main_menu: Presents the main menu and handles user input.
    """

    def __init__(self):
        """
        Initializes the ConsoleView object and sets up the associated Service object.
        """
        self.service = Service()

    def display_name(self):
        """
        Displays the name of the creator.
        """
        print("Felipe Barbosa Figueira")

    def display_data(self):
        """
        Displays all records currently loaded in the Service object.
        """
        for i, record in enumerate(self.service.records):
            print(f"{i}: {record}")

    def main_menu(self):
        """
        Presents the main menu to the user and handles the user's choices to interact with the application.
        """
        while True:
            self.display_name()
            print(
                "1: Reload Data\n2: Save Data\n3: Create Record\n4: Edit Record\n5: Delete Record\n6: Show Records\n7: Generate Chart\n8: Exit")
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
                self.generate_chart()
            elif choice == '8':
                break

    def generate_chart(self):
        print("1: Horizontal Bar Chart\n2: Vertical Bar Chart\n3: Pie Chart")
        chart_choice = input("Select chart type: ")
        column_name = input("Enter column name for chart data: ")

        if not self.service.column_exists(column_name):
            print(f"No data found for column '{column_name}'.")
            return

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