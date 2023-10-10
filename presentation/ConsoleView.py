# Made by Felipe Barbosa Figueira

from business.Service import Service

# ConsoleView class for presentation layer
class ConsoleView:
    def __init__(self):
        """Initializer method, demonstrates constructors in OOP."""
        self.service = Service()

    def display_data(self):
        """Presentation logic method."""
        data = self.service.get_data()
        for record in data:
            print(record)

    def display_name(self):
        """Another presentation logic method."""
        print("Felipe Barbosa Figueira")
