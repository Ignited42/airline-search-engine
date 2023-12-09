from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QListWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import pyqtSlot
import pymongo

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
        btn_airports = QPushButton('Airports', self)
        btn_airlines.clicked.connect(self.show_airlines)
        btn_airports.clicked.connect(self.show_airports)
        menu_layout.addWidget(btn_airlines)
        menu_layout.addWidget(btn_airports)
        main_layout.addLayout(menu_layout)

        # Scrollable List
        self.list_widget = QListWidget(self)
        main_layout.addWidget(self.list_widget)

        # Scrollable Table
        self.table_widget = QTableWidget(self)
        self.table_widget.setColumnCount(2)  # Example column count
        main_layout.addWidget(self.table_widget)

        self.setLayout(main_layout)
        self.show()

    @pyqtSlot()
    def show_airlines(self):
        self.list_widget.clear()
        self.list_widget.addItems(["Airline 1", "Airline 2", "Airline 3"])  # Example items

    @pyqtSlot()
    def show_airports(self):
        self.table_widget.clear()
        self.table_widget.setRowCount(3)  # Example row count
        self.table_widget.setItem(0, 0, QTableWidgetItem("Airport 1"))
        self.table_widget.setItem(0, 1, QTableWidgetItem("Location 1"))
        self.table_widget.setItem(1, 0, QTableWidgetItem("Airport 2"))
        self.table_widget.setItem(1, 1, QTableWidgetItem("Location 2"))
        self.table_widget.setItem(2, 0, QTableWidgetItem("Airport 3"))
        self.table_widget.setItem(2, 1, QTableWidgetItem("Location 3"))

if __name__ == '__main__':
    app = QApplication([])
    ex = App()
    app.exec_()
