import sys
from PyQt5.QtWidgets import (QApplication,QMainWindow,QStatusBar,QAction,
                             QTextEdit,QDockWidget,QToolBar)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize

class BasicMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUI()
        
    def initializeUI(self):
        self.setGeometry(100,100,350,350)
        self.setWindowTitle("Basic Menu 2")
        
        # Set a Central Widget
        self.setCentralWidget(QTextEdit())
        
        self.createMenu()
        self.createToolBar()
        self.createDockWidget()
        
        self.show()
    
    def createMenu(self):
        # Create action for file menu
        self.exit_act = QAction('Exit',self)
        self.exit_act.setShortcut('Ctrl+Q')
        self.exit_act.setStatusTip('Quit Program')
        self.exit_act.triggered.connect(self.close)
        
        # Create action for view menu
        full_screen_act = QAction('FullScreen',self,checkable = True)
        full_screen_act.setStatusTip('Switch to Full Screen Mode')
        full_screen_act.triggered.connect(self.switchToFullScreen)
        
        # Create a menu bar
        menu_bar = self.menuBar()
        
        # Create file menu and add actions
        file_menu = menu_bar.addMenu('File')
        file_menu.addAction(self.exit_act)
        
        # Create View menu, Appearance sub-menu, and add actions
        view_menu = menu_bar.addMenu('View')
        appearance_submenu = view_menu.addMenu('Appearance')
        appearance_submenu.addAction(full_screen_act)
        
        # Display  info about tools menu and view in the status bar
        self.setStatusBar(QStatusBar(self))
        
    def createToolBar(self):
        # Create toolbar for GUI
        tool_bar = QToolBar("Main ToolBar")
        self.addToolBar(tool_bar)
        
        # Add actions to toolbar
        tool_bar.addAction(self.exit_act)
        
    def createDockWidget(self):
        # Set up dock widget
        dock_widget = QDockWidget()
        dock_widget.setWindowTitle("Example Dock")
        dock_widget.setAllowedAreas(Qt.AllDockWidgetAreas)
        
        # Set main widget for the QDockWidget
        dock_widget.setWidget(QTextEdit())
        
        # Set initial location of dock widget in main window
        self.addDockWidget(Qt.LeftDockWidgetArea,dock_widget)
        
    def switchToFullScreen(self,state):
        # If the state is True then display in FullScreen
        # otherwise keep it normal
        if state:
            self.showFullScreen()
        else:
            self.showNormal()

def main():
    app = QApplication(sys.argv)
    window = BasicMenu()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
        