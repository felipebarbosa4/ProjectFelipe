# Importing necessary modules
import os

from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget,
                             QTableWidget, QTableWidgetItem, QMessageBox, QInputDialog, QGridLayout)
import sys

from presentation.ui.dialogs.RecordCreationDialog import RecordCreationDialog
from presentation.ui.dialogs.RecordEditDialog import RecordEditDialog
from presentation.ui.dialogs.RecordSearchDialog import RecordSearchDialog
from presentation.GUIHandler import GUIHandler  # Import the modified GUIHandler


# Main Application Window
class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My Data Application')
        self.setGeometry(100, 100, 800, 2200)
        self.setStyleSheet("background-color: white;")

        self.gui_handler = GUIHandler()  # Initialize GUIHandler

        # Main widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.create_widgets()
        self.update_data_table()

    def create_widgets(self):
        self.create_action_buttons()

        # Data display table
        self.data_table = QTableWidget()
        self.layout.addWidget(self.data_table)

    def create_action_buttons(self):
        gradient_style = """
        QPushButton {
            background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, 
                              stop:0 rgba(192, 192, 192, 255), stop:1 rgba(255, 255, 255, 255));
            color: black;
            border-radius: 5px;
            padding: 5px;
            border: 2px solid #B0B0B0;  /* Adjust the color as needed */
            margin: 4px;
        }
        QPushButton:hover {
            background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, 
                              stop:0 rgba(180, 180, 180, 255), stop:1 rgba(235, 235, 235, 255));
        }
        QPushButton:pressed {
            background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, 
                              stop:0 rgba(150, 150, 150, 255), stop:1 rgba(210, 210, 210, 255));
        }
        """

        grid_layout = QGridLayout()

        # Button to load data
        self.load_button = QPushButton('Load Data')
        self.load_button.setStyleSheet(gradient_style)
        self.load_button.clicked.connect(self.load_data)
        grid_layout.addWidget(self.load_button, 0, 0)  # Row 0, Column 0

        # Button to save data
        self.save_button = QPushButton('Save Data')
        self.save_button.setStyleSheet(gradient_style)
        self.save_button.clicked.connect(self.save_data)
        grid_layout.addWidget(self.save_button, 0, 1)  # Row 0, Column 1

        # Buttons for creating, editing, and deleting records
        self.create_button = QPushButton('Create Record')
        self.create_button.setStyleSheet(gradient_style)
        self.create_button.clicked.connect(self.create_record)
        grid_layout.addWidget(self.create_button, 1, 0)  # Row 1, Column 0

        self.edit_button = QPushButton('Edit Record')
        self.edit_button.setStyleSheet(gradient_style)
        self.edit_button.clicked.connect(self.edit_record)
        grid_layout.addWidget(self.edit_button, 1, 1)  # Row 1, Column 1

        self.delete_button = QPushButton('Delete Record')
        self.delete_button.setStyleSheet(gradient_style)
        self.delete_button.clicked.connect(self.delete_record)
        grid_layout.addWidget(self.delete_button, 2, 0)  # Row 2, Column 0

        # Button to search records
        self.search_button = QPushButton('Search Records')
        self.search_button.setStyleSheet(gradient_style)
        self.search_button.clicked.connect(self.search_records)
        grid_layout.addWidget(self.search_button, 2, 1)  # Row 2, Column 1

        # Add the grid layout to the main layout
        self.layout.addLayout(grid_layout)

    def load_data(self):
        try:
            records = self.gui_handler.reload_data()
            self.update_data_table(records)
            QMessageBox.information(self, "Success", "Data loaded successfully")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def save_data(self):
        try:
            self.gui_handler.save_data()
            QMessageBox.information(self, "Success", "Data saved successfully")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def create_record(self):
        dialog = RecordCreationDialog(self)
        if dialog.exec_():
            data = dialog.get_data()
            try:
                self.gui_handler.create_record(data)
                self.update_data_table()
                QMessageBox.information(self, "Success", "Record created successfully")
            except Exception as e:
                QMessageBox.critical(self, "Error", str(e))

    def edit_record(self):
        # First, select a record to edit. This can be done in various ways, e.g., by entering an index or selecting from a table.
        index, ok = QInputDialog.getInt(self, "Edit Record", "Enter the index of the record to edit:")
        if ok and 0 <= index < len(self.gui_handler.get_records()):
            current_data = vars(self.gui_handler.get_records()[index])
            dialog = RecordEditDialog(current_data, self)

            if dialog.exec_():
                new_data = dialog.get_data()
                try:
                    self.gui_handler.edit_record(index, new_data)
                    self.update_data_table()
                    QMessageBox.information(self, "Success", "Record updated successfully")
                except Exception as e:
                    QMessageBox.critical(self, "Error", str(e))
        else:
            QMessageBox.warning(self, "Warning", "Invalid index")

    def delete_record(self):
        index, ok = QInputDialog.getInt(self, "Delete Record", "Enter the index of the record to delete:")
        if ok and 0 <= index < len(self.gui_handler.get_records()):
            try:
                self.gui_handler.delete_record(index)
                self.update_data_table()
                QMessageBox.information(self, "Success", "Record deleted successfully")
            except Exception as e:
                QMessageBox.critical(self, "Error", str(e))
        else:
            QMessageBox.warning(self, "Warning", "Invalid index")

    def search_records(self):
        dialog = RecordSearchDialog(self)
        if dialog.exec_():
            criteria = dialog.get_search_criteria()
            filtered_records = self.filter_records(criteria)
            self.update_data_table(filtered_records)

    def filter_records(self, criteria):
        filtered = []
        for record in self.gui_handler.get_records():
            # Check if each criterion is a substring of the corresponding record attribute
            if all(value.lower() in getattr(record, key, "").lower() for key, value in criteria.items() if value):
                filtered.append(record)
        return filtered

    def update_data_table(self, records=None):
        records = records or self.gui_handler.get_records()
        self.data_table.setRowCount(len(records))
        self.data_table.setColumnCount(len(vars(records[0])) if records else 0)
        self.data_table.setHorizontalHeaderLabels(vars(records[0]).keys() if records else [])

        for i, record in enumerate(records):
            for j, (key, value) in enumerate(vars(record).items()):
                self.data_table.setItem(i, j, QTableWidgetItem(str(value)))


# Run the application
if __name__ == '__main__':
    print(os.getcwd())
    app = QApplication(sys.argv)
    main_window = App()
    main_window.show()
    sys.exit(app.exec_())
