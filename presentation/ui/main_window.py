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
    """Main Application Window.

    The App class creates the main window for the application and handles
    the layout and interaction of widgets within the application.
    """
    def __init__(self):
        """Initializes the main window with a title, geometry, and style."""
        super().__init__()
        self.setWindowTitle('My Data Application')
        self.setGeometry(100, 100, 800, 2200)
        self.setStyleSheet("background-color: white;")

        # Initialize the GUI Handler for managing the application's logic.
        self.gui_handler = GUIHandler()

        # Set up the main widget and its layout.
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Create the UI components and populate the data table.
        self.create_widgets()
        self.update_data_table()

    def create_widgets(self):
        """Creates the UI components and adds them to the main layout."""
        # Create action buttons for user interaction.
        self.create_action_buttons()
        # Initialize the data display table.
        self.data_table = QTableWidget()
        self.layout.addWidget(self.data_table)

    def create_action_buttons(self):
        """Creates action buttons and adds them to a grid layout."""
        # Define a gradient style for the buttons.
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

        # Initialize the grid layout.
        grid_layout = QGridLayout()

        # Create and configure the 'Load Data' button.
        self.load_button = QPushButton('Load Data')
        self.load_button.setStyleSheet(gradient_style)
        self.load_button.clicked.connect(self.load_data)
        grid_layout.addWidget(self.load_button, 0, 0)  # Row 0, Column 0

        # Create and configure the 'Save Data' button.
        self.save_button = QPushButton('Save Data')
        self.save_button.setStyleSheet(gradient_style)
        self.save_button.clicked.connect(self.save_data)
        grid_layout.addWidget(self.save_button, 0, 1)  # Row 0, Column 1

        # Create and configure the 'Record Record' button.
        self.create_button = QPushButton('Create Record')
        self.create_button.setStyleSheet(gradient_style)
        self.create_button.clicked.connect(self.create_record)
        grid_layout.addWidget(self.create_button, 1, 0)  # Row 1, Column 0

        # Create and configure the 'Edit Record' button.
        self.edit_button = QPushButton('Edit Record')
        self.edit_button.setStyleSheet(gradient_style)
        self.edit_button.clicked.connect(self.edit_record)
        grid_layout.addWidget(self.edit_button, 1, 1)  # Row 1, Column 1

        # Create and configure the 'Delete Record' button.
        self.delete_button = QPushButton('Delete Record')
        self.delete_button.setStyleSheet(gradient_style)
        self.delete_button.clicked.connect(self.delete_record)
        grid_layout.addWidget(self.delete_button, 2, 0)  # Row 2, Column 0

        # Create and configure the 'Search Record' button.
        self.search_button = QPushButton('Search Records')
        self.search_button.setStyleSheet(gradient_style)
        self.search_button.clicked.connect(self.search_records)
        grid_layout.addWidget(self.search_button, 2, 1)  # Row 2, Column 1

        # Add the grid layout to the main layout
        self.layout.addLayout(grid_layout)

    def load_data(self):
        """Loads data from a source and updates the data table."""
        # Attempt to load data using the GUI Handler and handle any exceptions.
        try:
            records = self.gui_handler.reload_data()
            self.update_data_table(records)
            QMessageBox.information(self, "Success", "Data loaded successfully")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def save_data(self):
        """Saves the current state of data."""
        # Attempt to save data using the GUI Handler and handle any exceptions.
        try:
            self.gui_handler.save_data()
            QMessageBox.information(self, "Success", "Data saved successfully")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def create_record(self):
        """Opens a dialog to create a new record."""
        # Use RecordCreationDialog to collect new record information.
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
        """Opens a dialog to edit an existing record."""
        # Use RecordEditDialog to edit an existing record's information.
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
        """Deletes the selected record."""
        # Use QInputDialog to get the index of the record to delete.
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
        """Searches for records matching the entered criteria."""
        # Use RecordSearchDialog to get search criteria and update the table.
        dialog = RecordSearchDialog(self)
        if dialog.exec_():
            criteria = dialog.get_search_criteria()
            filtered_records = self.filter_records(criteria)
            self.update_data_table(filtered_records)

    def filter_records(self, criteria):
        """Filters records based on given criteria."""
        # Check if each criterion is a substring of the corresponding record attribute.
        filtered = []
        for record in self.gui_handler.get_records():
            # Check if each criterion is a substring of the corresponding record attribute
            if all(value.lower() in getattr(record, key, "").lower() for key, value in criteria.items()
                   if value):
                filtered.append(record)
        return filtered

    def update_data_table(self, records=None):
        """
               Updates the data table widget with a new set of records.

               If no records are provided, it fetches the current records from the GUI handler.

               Args:
                   records (list of Record, optional): A list of Record objects to populate the table with.
               """
        # If no records are provided, get the current records from the GUI handler

        records = records or self.gui_handler.get_records()
        # Set the number of rows in the table to the number of records
        self.data_table.setRowCount(len(records))

        # Set the number of columns in the table to the number of attributes in a record
        # This assumes all records have the same attributes
        self.data_table.setColumnCount(len(vars(records[0])) if records else 0)

        # Set the horizontal headers for the table using the attribute names from the first record
        self.data_table.setHorizontalHeaderLabels(vars(records[0]).keys() if records else [])

        # Populate the table with the records' data
        for i, record in enumerate(records):
            for j, (key, value) in enumerate(vars(record).items()):
                # Convert each attribute value to a string and create a QTableWidgetItem
                self.data_table.setItem(i, j, QTableWidgetItem(str(value)))


# Run the application
if __name__ == '__main__':
    # Create an instance of the application
    app = QApplication(sys.argv)
    # Create an instance of the main window
    main_window = App()
    # Display the main window
    main_window.show()
    # Start the application's event loop
    sys.exit(app.exec_())
