# Import PyQt5 modules
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from main_window import MainWindow # Import the main window class from the other file

# Define a class for the pop-up window
class PopUpWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Pop-up window'
        self.left = 200
        self.top = 200
        self.width = 200
        self.height = 100
        self.initUI()
    
    def initUI(self):
        # Set the window title and size
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Hide the window
        self.hide()
    
    # Define a slot for the item clicked signal
    @pyqtSlot(str)
    def on_item_click(self, text):
        # Create a message box widget
        self.message_box = QMessageBox(self)

        # Set the text, icon, and buttons of the message box
        self.message_box.setText(f'You clicked {text}')
        self.message_box.setIcon(QMessageBox.Information)
        self.message_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        # Show the message box
        self.message_box.show()

# Create an application instance and run it
if __name__ == '__main__':
    app = QApplication([])
    main_window = MainWindow() # Create a main window object
    pop_up_window = PopUpWindow() # Create a pop-up window object
    # Connect the item clicked signal of the main window to the slot of the pop-up window
    main_window.item_clicked.connect(pop_up_window.on_item_click)
    app.exec_()
