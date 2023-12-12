import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QStackedWidget, QTableWidget, QDialog

class MainWidget(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.airports_button = QPushButton('Airports', self)
        self.airports_button.clicked.connect(self.show_airports)
        layout.addWidget(self.airports_button)

        self.airlines_button = QPushButton('Airlines', self)
        self.airlines_button.clicked.connect(self.show_airlines)
        layout.addWidget(self.airlines_button)
        
        self.routes_button = QPushButton('Routes', self)
        self.routes_button.clicked.connect(self.show_airlines)
        layout.addWidget(self.routes_button)
        
        self.search_button = QPushButton('Search', self)
        self.search_button.clicked.connect(self.show_airlines)
        layout.addWidget(self.search_button)

        # Add buttons for Routes and Search with their respective click events
        
        self.setLayout(layout)

    def show_airports(self):
        self.stacked_widget.setCurrentIndex(1)  # Index of the airports view
    
    def show_airlines(self):
        self.stacked_widget.setCurrentIndex(2)  # Index of the airlines view
        
    def show_routes(self):
        self.stacked_widget.setCurrentIndex(3)  # Index of the airlines view
        
    def show_search(self):
        self.stacked_widget.setCurrentIndex(4)  # Index of the airlines view

    # Implement functions to show routes and search views


class AirportWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.table = QTableWidget(self)
        # Set up your table with data
        layout.addWidget(self.table)
        self.setLayout(layout)

    # Include a button or mechanism to return to the main view


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.stacked_widget = QStackedWidget(self)
        self.setCentralWidget(self.stacked_widget)

        main_widget = MainWidget(self.stacked_widget)
        airport_widget = AirportWidget()  # You will add AirlinesWidget, RoutesWidget, and SearchWidget similarly
        # Add widgets to the stacked widget
        self.stacked_widget.addWidget(main_widget)
        self.stacked_widget.addWidget(airport_widget)
        
        
        # Continue adding other views

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
