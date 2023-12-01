from PyQt5.QtWidgets import QLineEdit, QFormLayout, QDialog, QPushButton


class RecordSearchDialog(QDialog):
    """
    A dialog for searching records based on various criteria.

    Attributes:
        inputs (dict): A dictionary of QLineEdit widgets for user input.
    """
    def __init__(self, parent=None):
        """
        Initializes a new instance of RecordSearchDialog.

        Args:
            parent (QWidget, optional): The parent widget. Defaults to None.
        """
        super().__init__(parent)
        self.setWindowTitle("Search Records")

        self.layout = QFormLayout(self)
        self.inputs = {}
        search_fields = ['ref_number', 'disclosure_group', 'title_en', 'title_fr', 'name',
                         'purpose_en', 'purpose_fr', 'start_date', 'end_date', 'destination_en',
                         'destination_fr', 'airfare', 'other_transport', 'lodging', 'meals', 'other_expenses',
                         'total', 'additional_comments_en', 'additional_comments_fr', 'owner_org',
                         'owner_org_title']

        for field in search_fields:
            self.inputs[field] = QLineEdit(self)
            self.layout.addRow(field, self.inputs[field])

        self.search_button = QPushButton("Search", self)
        self.search_button.clicked.connect(self.accept)
        self.layout.addRow(self.search_button)

    def get_search_criteria(self):
        """
        Retrieves the search criteria from the input fields.

        Returns:
            dict: A dictionary where the key is the field name and the value is the text entered by the user.
        """
        return {field: self.inputs[field].text() for field in self.inputs}
