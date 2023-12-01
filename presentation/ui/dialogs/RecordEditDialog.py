from PyQt5.QtWidgets import QFormLayout, QDialog, QLineEdit, QPushButton


class RecordEditDialog(QDialog):
    """
    A dialog for editing an existing record.

    Allows the user to edit the details of a record. Fields are pre-populated with
    existing data, which can be updated.

    Attributes:
        inputs (dict): A dictionary of QLineEdit widgets representing record fields.
    """
    def __init__(self, record_data, parent=None):
        """
        Initializes the dialog with a form for editing a record.

        Args:
            record_data (dict): A dictionary containing the record's current data.
            parent (QWidget, optional): The parent widget. Defaults to None.
        """
        super().__init__(parent)
        self.setWindowTitle("Edit Record")

        self.layout = QFormLayout(self)
        self.inputs = {}
        field_names = ['ref_number', 'disclosure_group', 'title_en', 'title_fr', 'name', 'purpose_en', 'purpose_fr', 'start_date', 'end_date', 'destination_en', 'destination_fr', 'airfare', 'other_transport', 'lodging', 'meals', 'other_expenses', 'total', 'additional_comments_en', 'additional_comments_fr', 'owner_org', 'owner_org_title']  # Add all necessary fields here

        for field in field_names:
            self.inputs[field] = QLineEdit(self)
            self.inputs[field].setText(record_data.get(field, ""))
            self.layout.addRow(field, self.inputs[field])

        self.confirm_button = QPushButton("Update", self)
        self.confirm_button.clicked.connect(self.accept)
        self.layout.addRow(self.confirm_button)

    def get_data(self):
        """
        Retrieves the data from the input fields.

        Returns:
            dict: A dictionary with the field names as keys and the updated data as values.
        """
        return {field: self.inputs[field].text() for field in self.inputs}
