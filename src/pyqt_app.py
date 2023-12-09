from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QListWidget, QTableWidget, QTableWidgetItem, QLineEdit, QDialog
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Flight Information App'
        self.left = 100
        self.top = 100
        self.width = 640
        self.height = 480
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Main layout
        main_layout = QVBoxLayout()

        # Menu buttons
        menu_layout = QHBoxLayout()
        btn_airlines = QPushButton('Airlines', self)
        btn_airlines.clicked.connect(self.show_airlines)
        btn_airports = QPushButton('Airports', self)
        btn_airports.clicked.connect(self.show_airports)
        menu_layout.addWidget(btn_airlines)
        menu_layout.addWidget(btn_airports)
        main_layout.addLayout(menu_layout)

        # Scrollable List
        self.list_widget = QListWidget(self)
        main_layout.addWidget(self.list_widget)

        # Scrollable Table
        self.table_widget = QTableWidget(self)
        main_layout.addWidget(self.table_widget)

        # Textbox for user input
        self.textbox = QLineEdit(self)
        main_layout.addWidget(self.textbox)

        # Label for displaying text
        self.label = QLabel('Select an option', self)
        main_layout.addWidget(self.label)

        # Set the main layout
        self.setLayout(main_layout)

    @pyqtSlot()
    def show_airlines(self):
        # You can populate this list with airline data
        self.list_widget.clear()
        self.list_widget.addItem("Airline 1")
        self.list_widget.addItem("Airline 2")

    @pyqtSlot()
    def show_airports(self):
        # Populate the table with airport data
        self.table_widget.clear()
        self.table_widget.setRowCount(2)
        self.table_widget.setColumnCount(2)
        self.table_widget.setItem(0, 0, QTableWidgetItem("Airport 1"))
        self.table_widget.setItem(0, 1, QTableWidgetItem("Location 1"))
        self.table_widget.setItem(1, 0, QTableWidgetItem("Airport 2"))
        self.table_widget.setItem(1, 1, QTableWidgetItem("Location 2"))

# Create an application instance and run it
if __name__ == '__main__':
    app = QApplication([])
    ex = App()
    app.exec_()
