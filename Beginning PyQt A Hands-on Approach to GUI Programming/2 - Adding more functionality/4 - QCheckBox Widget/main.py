import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QCheckBox
from PyQt5.QtCore import Qt
# Importing one extra module : QCheckBox
# Check boxes act as binary switches and are great for representing
# elements which have only 2 states i.e. either on or off

class CheckBoxWindow(QWidget):
    # Constructor
    def __init__(self):
        super().__init__()
        self.initializeUI()
    
    def initializeUI(self):
        self.setGeometry(100,100,250,250)
        self.setWindowTitle("QCheckBox Widget")
        self.displayCheckBoxes()
        
        self.show()
    
    def displayCheckBoxes(self):
        # Setting up checkboxes and other widgets
        header_label = QLabel(self)
        header_label.setText("Which shifts can you work? (Please check all that apply)")
        header_label.setWordWrap(True)
        header_label.move(10,10)
        header_label.resize(230,60)
        
        # Setting up checkboxes
        # Just follow the same convention as any other element
        # QCheckBox("Text",QWidget)
        morning_cb = QCheckBox("Moring [8 AM - 2 PM]",self)
        morning_cb.move(20,80)
        morning_cb.toggle()
        # You can change the state of the checkbox using toggle() method
        # By default it is unchecked and by calling it at initialization it will
        # become checked
        
        # Handling the state change signal
        # In order to handle the state change we use the stateChanged() method
        # and then we can use the connect() method to connect it with a function
        morning_cb.stateChanged.connect(self.printToTerminal)
        
        after_cb = QCheckBox("Afternoon [1 PM - 8 PM]",self)
        after_cb.move(20,100)
        after_cb.stateChanged.connect(self.printToTerminal)
        
        night_cb = QCheckBox("Night [7 PM - 3 AM]",self)
        night_cb.move(20,120)
        night_cb.stateChanged.connect(self.printToTerminal)
        
    def printToTerminal(self,state):
        # This function determines the state of checkbox and exactly which
        # checkbox passed the signal and prints a messages accordingly
        
        sender = self.sender()
        
        if state == Qt.Checked:
            print("{} Selected".format(sender.text()))
        else:
            print("{} DeSelected".format(sender.text()))
        
        
# Running the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CheckBoxWindow()
    sys.exit(app.exec_())