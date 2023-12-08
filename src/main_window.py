# Import PyQt5 modules
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QMenuBar, QMenu, QAction, QListWidget, QListWidgetItem, QTableWidget, QTableWidgetItem, QLineEdit, QChartView
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtGui import QPixmap
#from PyQt5.QtChart import QChart, QLineSeries

# Define a class for the main window
class MainWindow(QWidget):

    # Define a signal to emit when an item is clicked
    item_clicked = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.title = 'pyqt_app'
        self.left = 100
        self.top = 100
        self.width = 320
        self.height = 300
        self.initUI()
    
    def initUI(self):
        # Set the window title and size
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create a menu bar and add it to the main window
        self.menu_bar = QMenuBar(self)
        self.setMenuBar(self.menu_bar)

        # Create a file menu and add actions to it
        self.file_menu = QMenu('File', self)
        self.menu_bar.addMenu(self.file_menu)
        self.open_action = QAction('Open', self)
        self.save_action = QAction('Save', self)
        self.exit_action = QAction('Exit', self)
        self.file_menu.addAction(self.open_action)
        self.file_menu.addAction(self.save_action)
        self.file_menu.addAction(self.exit_action)

        # Connect the actions to slots
        self.open_action.triggered.connect(self.open_file)
        self.save_action.triggered.connect(self.save_file)
        self.exit_action.triggered.connect(self.close)

        # Create a list widget and add it to the main window
        self.list_widget = QListWidget(self)
        self.list_widget.setGeometry(10, 30, 100, 150)

        # Add some items to the list widget
        self.list_widget.addItem('Item 1')
        self.list_widget.addItem('Item 2')
        self.list_widget.addItem('Item 3')

        # Connect the item clicked signal to a slot
        self.list_widget.itemClicked.connect(self.on_item_click)

        # Create a table widget and add it to the main window
        self.table_widget = QTableWidget(self)
        self.table_widget.setGeometry(120, 30, 200, 150)

        # Set the row and column count and headers
        self.table_widget.setRowCount(3)
        self.table_widget.setColumnCount(2)
        self.table_widget.setHorizontalHeaderLabels(['Name', 'Age'])
        self.table_widget.setVerticalHeaderLabels(['Person 1', 'Person 2', 'Person 3'])

        # Set some data to the table cells
        self.table_widget.setItem(0, 0, QTableWidgetItem('Alice'))
        self.table_widget.setItem(0, 1, QTableWidgetItem('25'))
        self.table_widget.setItem(1, 0, QTableWidgetItem('Bob'))
        self.table_widget.setItem(1, 1, QTableWidgetItem('30'))
        self.table_widget.setItem(2, 0, QTableWidgetItem('Charlie'))
        self.table_widget.setItem(2, 1, QTableWidgetItem('35'))

        # Create a line edit widget and add it to the main window
        self.line_edit = QLineEdit(self)
        self.line_edit.setGeometry(10, 190, 100, 20)

        # Create a label widget and add it to the main window
        self.image_label = QLabel(self)
        self.image_label.setGeometry(120, 190, 100, 100)

        # Load an image file and set it as the pixmap of the label
        self.image_pixmap = QPixmap('image.jpg')
        self.image_label.setPixmap(self.image_pixmap)

        # Create a chart view widget and add it to the main window
        self.chart_view = QChartView(self)
        self.chart_view.setGeometry(230, 190, 100, 100)

        # Create a chart object and add it to the chart view
        self.chart = QChart()
        self.chart_view.setChart(self.chart)

        # Create some data for the graph
        x_data = [1, 2, 3, 4, 5]
        y_data = [10, 20, 15, 30, 25]

        # Create a line series and add the data to it
        #self.line_series = QLineSeries()
        #for x, y in zip(x_data, y_data):
            #self.line_series.append(x, y)

        # Add the line series to the chart
        self.chart.addSeries(self.line_series)

        # Set the title and axis labels of the chart
        self.chart.setTitle('A simple line graph')
        self.chart.createDefaultAxes()
        self.chart.axisX().setTitleText('X')
        self.chart.axisY().setTitleText('Y')

        # Show the window
        self.show()
    
    # Define a slot for the open action
    def open_file(self):
        # Do something to open a file
        print('You clicked open')
    
    # Define a slot for the save action
    def save_file(self):
        # Do something to save a file
        print('You clicked save')
    
    # Define a slot for the item click
    def on_item_click(self, item):
        # Get the text of the item
        text = item.text()

        # Emit the item clicked signal with the text as the argument
        self.item_clicked.emit(text)

# Create an application instance and run it
if __name__ == '__main__':
    app = QApplication([])
    main_window = MainWindow()
    app.exec_()
