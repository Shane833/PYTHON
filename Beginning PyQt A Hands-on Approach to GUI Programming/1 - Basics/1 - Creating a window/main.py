# Importing necessary modules
import sys 
# This module is used to store and pass cmd line arguments to the program and  
# other system related tasks
from PyQt5.QtWidgets import QApplication, QWidget
# -> The QWidgets module contains various UI elements to help develop GUI apps
# -> QApplication class is responsible for application's main event loop, flow 
#    initialization, finalization and session management
# -> You only need to create a single instance of the QtApplication class as you
#    will only be working with a single application at a time

class EmptyWindow(QWidget): # Inheriting QWigdet Class
    # Constructor
    def __init__(self):
        super().__init__() # Creating a constructor of the QWidget Class
        self.initializeUI()
    
    # Initializing UI
    def initializeUI(self):
        # Initializing the window and displaying it to the screen
        self.setGeometry(100,100,400,300) 
        # QWidget.setGeometry(xpos,ypos,width,height)
        self.setWindowTitle("Empty Window in PyQt")
        self.show()
        # QWidget.show() displays the widget to the screen

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # The QApplication takes cmd-line arguments as input, alternatively you 
    # can also pass an empty list in the arguments
    window = EmptyWindow()
    sys.exit(app.exec_())
    # QApplication.exec_() is used to start the event loop and using sys.exit()
    # ensures a clean exit of the program