# Import PyQt5 modules
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtCore import pyqtSlot

# Define a class for the main window
class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'pyqt_app'
        self.left = 100
        self.top = 100
        self.width = 320
        self.height = 200
        self.initUI()
    
    def initUI(self):
        # Set the window title and size
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create a button and connect it to a slot
        self.button = QPushButton('Click me', self)
        self.button.move(100, 70)
        self.button.clicked.connect(self.on_click)

        # Create a label and set its initial text
        self.label = QLabel('Hello, world!', self)
        self.label.move(120, 120)

        # Show the window
        self.show()
    
    # Define a slot for the button click
    @pyqtSlot()
    def on_click(self):
        # Change the label text
        self.label.setText('You clicked the button!')

# Create an application instance and run it
if __name__ == '__main__':
    app = QApplication([])
    ex = App()
    app.exec_()
