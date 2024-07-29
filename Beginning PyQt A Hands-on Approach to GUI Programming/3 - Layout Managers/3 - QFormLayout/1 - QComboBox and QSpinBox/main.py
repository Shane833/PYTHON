# Learning about QSpinBox and QComboBox
# QSpinBox is similar to a input field but allows user to enter integer values
# either by typing or clicking up and down, limits can be set on the max and min
# QComboBox is a way to display a list of options and user can select from them

import sys
from PyQt5.QtWidgets import (QApplication,QWidget,QLabel,QComboBox,QSpinBox,
                             QHBoxLayout,QVBoxLayout)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class SelectItems(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()
        
    def initializeUI(self):
        self.setGeometry(100,100,300,200)
        self.setWindowTitle('Combobox and Spinbox')
        self.itemsAndPrices()
        
        self.show()
    
    def itemsAndPrices(self):
        # Creating items to let the user select item from combobox and price from spinbox
        info_label = QLabel("Select 2 items you had for lunch and their prices.")
        info_label.setFont(QFont('Ariel',16))
        info_label.setAlignment(Qt.AlignCenter)
        
        self.display_total_label = QLabel("Total Spend: $")
        self.display_total_label.setFont(QFont('Ariel',16))
        self.display_total_label.setAlignment(Qt.AlignRight)
        
        # Create list of food items and add them to 2 separate comboboxes
        lunch_list = ['egg','turkey sandwich','ham sandwich','cheese','hummus','yogurt',
                      'apple','banana','orange','waffle','baby carrots','pasta','crackers',
                      'pretzels','pita chips','coffee','soda','water']
                      
        lunch_cb1 = QComboBox()
        lunch_cb1.addItems(lunch_list)
        lunch_cb2 = QComboBox()
        lunch_cb2.addItems(lunch_list)
        
        # Create 2 separate spinboxes
        
        self.price_sb1 = QSpinBox()
        self.price_sb1.setRange(0,100)
        self.price_sb1.setPrefix("$")
        self.price_sb1.valueChanged.connect(self.calculateTotal)
        
        self.price_sb2 = QSpinBox()
        self.price_sb2.setRange(0,100)
        self.price_sb2.setPrefix("$")
        self.price_sb2.valueChanged.connect(self.calculateTotal)
        
        # Create horizontal boxes to hold comboboxes and spinboxes
        h_box1 = QHBoxLayout()
        h_box2 = QHBoxLayout()
        
        h_box1.addWidget(lunch_cb1)
        h_box1.addWidget(self.price_sb1)
        h_box2.addWidget(lunch_cb2)
        h_box2.addWidget(self.price_sb2)
        
        # Add widgets and layouts to the vertical box layout
        v_box = QVBoxLayout()
        v_box.addWidget(info_label)
        v_box.addLayout(h_box1)
        v_box.addLayout(h_box2)
        v_box.addWidget(self.display_total_label)
        
        self.setLayout(v_box)
    
    def calculateTotal(self):
        total = self.price_sb1.value() + self.price_sb2.value()
        
        self.display_total_label.setText("Total Spend: ${}".format(total))

def main(argc,argv):
    app = QApplication(argv)
    window = SelectItems()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main(len(sys.argv),sys.argv)