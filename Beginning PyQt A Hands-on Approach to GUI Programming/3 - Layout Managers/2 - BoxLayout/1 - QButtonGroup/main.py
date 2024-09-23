# Learning about grouping buttons together
import sys
from PyQt5.QtWidgets import QWidget,QApplication,QCheckBox,QButtonGroup

class ButtonGroup(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()
   
    def initializeUI(self):
        self.setWindowTitle("Button Grouping")
        self.setGeometry(100,100,200,200)
        self.buttons();
        
        self.show()
    
    def buttons(self):
    
        # Create an instance of QButtonGroup
        b_group = QButtonGroup(self)
        # Create two checkboxes
        cb_1 = QCheckBox("CB 1",self)
        cb_1.move(10,20)
        cb_2 = QCheckBox("CB 2",self)
        cb_2.move(80,20)
        # Now we add them to the group 
        b_group.addButton(cb_1)
        b_group.addButton(cb_2)
        # Using this we can connect all of them to a single single
        b_group.buttonClicked.connect(self.cbChecked)
        # This can automatically put mutual exclusion on buttons
        
    def cbChecked(self,button):
        print(button)
    
def main():
    app = QApplication(sys.argv)
    window = ButtonGroup()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
        
        
        