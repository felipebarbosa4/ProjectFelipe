# Made by Felipe Barbosa Figueira
class Record:
    def __init__(self, data):
        """Initializer method, demonstrates constructors in OOP."""
        self.ref_number = data['ref_number']
        for k, v in data.items():
            setattr(self, k, v)

    def __str__(self):
        """String representation of the object."""
        return str(self.__dict__)