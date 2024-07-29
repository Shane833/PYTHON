# A Menubar is a set of pull-down menus with list of commands that we can use
# to interact with the program
import sys
from PyQt5.QtWidgets import (QApplication,QMainWindow,QAction)
# The two new modules we imported are QMainWindow and QAction

# QMainWindow : This class provides necessary tool for creating and managing 
# the layout for the main window of an application. It allows you to setup a
# window with status bar,tool bar,dock widgets etc

# While the QWidget class is the base class of all the widgets including the
# QMainWindow. So QWidget is like the general case while the QMainWindows is
# specifically designed to embed other widgets and features in the app window
# You can the following things in the main window:
# MenuBar, Tool bar, Dock other widgets, Central Widget


class BasicMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUI()
    
    def initializeUI(self):
        self.setGeometry(100,100,350,350)
        self.setWindowTitle('Basic Menu')
        self.createMenu()
        
        self.show()
    
    def createMenu(self):
        # Create action for file menu
        exit_act = QAction('Exit',self)
        # We create actions using QAction class which can be added to other widgets
        exit_act.setShortcut('Ctrl+Q')
        # You can set the shortcuts for each action to be performed
        exit_act.triggered.connect(self.close)
        # Like the QPushButton you also have the certain signal when an action is to be 
        # performed or in this case triggered then you can connect it a function
        
        # Create menubar
        menu_bar = self.menuBar()
        # Alternatively you can also use the QMenuBar class to create it
        # but its just as easy to do it from here using method menuBar()
        menu_bar.setNativeMenuBar(False)
        
        # Create file menu and add action
        file_menu = menu_bar.addMenu('File')
        # You add menu directely using the addMenu('string') method
        # Alternatively you can also use the QMenu class to create an instance
        file_menu.addAction(exit_act)
        
def main():
    app = QApplication(sys.argv)
    window = BasicMenu()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()