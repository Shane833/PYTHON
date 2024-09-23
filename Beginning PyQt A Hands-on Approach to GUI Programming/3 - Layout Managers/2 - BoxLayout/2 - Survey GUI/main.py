# Project 4.2 Survey GUI
# Aim of this project is to exercise BoxLayouts
# There are mainly 2 types : 1. QHBoxLayout (arranges horizontally) 2. QVBoxLayout (arranges vertically)
# and the best thing is that these layouts can be nested/embedded into one another

import sys
from PyQt5.QtWidgets import (QApplication,QWidget,QLabel,QPushButton,QCheckBox,
                             QButtonGroup,QHBoxLayout,QVBoxLayout)
from PyQt5.QtGui import QFont

class DisplaySurvey(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initializeUI()
        
    def initializeUI(self):
        self.setWindowTitle("Survey GUI")
        self.setGeometry(100,100,400,230)
        self.displayWidgets()
        
        self.show()
    
    def displayWidgets(self):
        # To set up both the box layouts
        title = QLabel("Restaurant Name",self)
        title.setFont(QFont('Ariel',17))
        question = QLabel("How would you rate your service today?")
        # Note : If you are going to add widgets in a layout you need not
        # specify their parent, even if you do it  won't make a difference
        
        # Create a horizontal layout
        title_h_box = QHBoxLayout()
        title_h_box.addStretch() 
        title_h_box.addWidget(title)
        title_h_box.addStretch()
        # Here we added stretch before and after is
        '''
        The addStretch() method acts like an invisible widget that can be used to help 
        arrange widgets in a layout manager. Widgets in QHBoxLayout are organized left to right, 
        so in title_h_box, addStretch is added to the left, title in the middle, and another 
        addStretch to the right. This centers the title in title_h_box
        '''
        ratings = ['Not Satisfied','Average','Satisfied']
        
        ratings_h_box = QHBoxLayout()
        ratings_h_box.setSpacing(60) # Sets space b/w the widgets
        ratings_h_box.addStretch()
        
        for rating in ratings:
            rate_label = QLabel(rating,self)
            ratings_h_box.addWidget(rate_label)
        
        ratings_h_box.addStretch()
        
        cb_h_box = QHBoxLayout()
        cb_h_box.setSpacing(100)
        scale_bg = QButtonGroup(self) # button group to contain checkboxes
        
        cb_h_box.addStretch()
        
        for cb in range(len(ratings)):
            scale_cb = QCheckBox(str(cb),self) # Gives values 0,1,2
            cb_h_box.addWidget(scale_cb)
            scale_bg.addButton(scale_cb)
        
        cb_h_box.addStretch()
        
        # Check for signal when checkboxes are clicked
        scale_bg.buttonClicked.connect(self.checkboxClicked)
        
        close_button = QPushButton('Close',self)
        close_button.clicked.connect(self.close)
        
        # Create veritcal layout and add widgets and h_box layouts
        v_box = QVBoxLayout()
        v_box.addLayout(title_h_box)
        v_box.addWidget(question)
        v_box.addStretch(1)
        v_box.addLayout(ratings_h_box)
        v_box.addLayout(cb_h_box)
        v_box.addStretch(2)
        v_box.addWidget(close_button)
        
        '''
        The addStretch method adds a QSpacerItem to the end of a box layout. A QSpacerItem is an adjustable blank space.
        Using vbox.addStretch(1) will add a zero-width spacer-item that expands vertically from the top of the layout downwards.
        Using hbox.addStretch(1) will add a zero-height spacer-item that expands horizontally from the left of the layout rightwards.
        
        The argument passed to addStretch changes the stretch factor. If you add a second stretch after the first item
        then you will see that the second spacer item grows twice as fast as the first. And if you set the first stretch to zero, it won't grow at all.
        '''
        
        # Set the main layout of the window
        self.setLayout(v_box)
        
    def checkboxClicked(self,cb):
        # Print the text of the checkbox
        print("{} Selected".format(cb.text()))

def main():
    app = QApplication(sys.argv)
    window = DisplaySurvey()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()