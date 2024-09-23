# Icons are very useful for doing many tasks
# They can exist in any 4 states : Normal,Disabled,Active or Selected
# The QIcon is the class which is used to perform all the functions related to 
# setting up icons on the windows, widgets etc.

import sys
from PyQt5.QtWidgets import (QApplication,QLabel,QWidget,QPushButton,QVBoxLayout)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
import random

class ChangeIcon(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()
    
    def initializeUI(self):
        self.setWindowTitle("Set Icons Example")
        self.setGeometry(100,100,200,200)
        self.setWindowIcon(QIcon("mute.png"))
        # Whenever you wish to put an icon onto anything
        # It has to be an instance of the QIcon class
        # like QIcon("Path of the icon")
        self.createWidgets()
        
        self.show()
    
    def createWidgets(self):
        info_label = QLabel("Click on the button and select a fruit")
        self.images = ["motivation.png","flexible.png","struggle.png","discipline.png"]
        
        self.icon_button = QPushButton(self)
        self.icon_button.setIcon(QIcon(random.choice(self.images)))
        self.icon_button.setIconSize(QSize(60,60))
        self.icon_button.clicked.connect(self.changeButtonIcon)
        # All the widgets support an icon which can put using the 
        # setIcon() method and the size of the icon can be varied
        # by using an instance of QSize(x,y) in the setIconSize() method
        
        # Create vertical layout and add widgets
        v_box = QVBoxLayout()
        v_box.addWidget(info_label)
        v_box.addWidget(self.icon_button)
        
        # Set main layout of window
        self.setLayout(v_box)
        
    def changeButtonIcon(self):
        
        self.icon_button.setIcon(QIcon(random.choice(self.images)))
        self.icon_button.setIconSize(QSize(60,60))
        
def main():
    app = QApplication(sys.argv)
    window = ChangeIcon()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
        