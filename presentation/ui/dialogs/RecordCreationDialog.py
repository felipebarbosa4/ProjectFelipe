from PyQt5.QtWidgets import QDialog, QLineEdit, QFormLayout, QPushButton

class RecordCreationDialog(QDialog):
    """
    A dialog window for PyQt5 application to create a new record.

    This dialog collects inputs for each field required to create a new record.
    Once all data is entered, it can be confirmed and the record will be created.
    """
    def __init__(self, parent=None):
        """
        Initializes the record creation dialog with a form layout.

        Args:
            parent (QWidget): The parent widget of the dialog. Defaults to None.
        """
        super().__init__(parent)
        self.setWindowTitle("Create New Record")

        self.layout = QFormLayout(self)
        self.inputs = {}
        field_names = ['ref_number', 'disclosure_group', 'title_en', 'title_fr', 'name', 'purpose_en', 'purpose_fr', 'start_date', 'end_date', 'destination_en', 'destination_fr', 'airfare', 'other_transport', 'lodging', 'meals', 'other_expenses', 'total', 'additional_comments_en', 'additional_comments_fr', 'owner_org', 'owner_org_title']  # Add all necessary fields here

        for field in field_names:
            self.inputs[field] = QLineEdit(self)
            self.layout.addRow(field, self.inputs[field])

        self.confirm_button = QPushButton("Confirm", self)
        self.confirm_button.clicked.connect(self.accept)
        self.layout.addRow(self.confirm_button)

    def get_data(self):
        """
        Retrieves the data from all input fields.

        Returns:
            dict: A dictionary with field names as keys and entered text as values.
        """
        return {field: self.inputs[field].text() for field in self.inputs}
