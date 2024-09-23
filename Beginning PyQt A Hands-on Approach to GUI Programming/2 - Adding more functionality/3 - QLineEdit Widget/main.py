import sys
from PyQt5.QtWidgets import (QApplication,QWidget,QLabel,
QLineEdit,QPushButton)
from PyQt5.QtCore import Qt
# Addtional imports in this script are QLineEdit which is used
# to display an entry box where the user can enter information

# Secondly, we also imported Qt which contains various miscellaneous
# functions whcih are essential for createing GUIs

class EntryWindow(QWidget):
    # Constructor
    def __init__(self):
        super().__init__()
        self.initializeUI()
    
    def initializeUI(self):
        self.setGeometry(100,100,400,200)
        self.setWindowTitle("QLineEdit Widget")
        self.displayWidgets()
        
        self.show()
    
    def displayWidgets(self):
        # Creating required labels, buttons and LineEdit
        # If you don't want to create objects of any widget
        # you can directly create it, For eg:
        QLabel('Please enter your name below',self).move(100,10)
        # Here we directly called the QLabel without assigning it to an object
        name_label = QLabel("Name:",self)
        name_label.move(70,50)
        
        # Now we will create a lineedit widget which will be a class data member
        # You can create an object of QLineEdit widget by following the previous 
        # conventions such as : obj = QLineEdit(QWidget)
        self.name_entry = QLineEdit(self)
        # You can ajust the alignment of the imput cursor using
        # QLineEdit.setAlignment(Qt.Alignments)
        # THe various Alignments include Qt.AlignLeft, Qt.AlighnRight, Qt.ALignHCenter
        self.name_entry.setAlignment(Qt.AlignLeft)
        self.name_entry.move(130,50)
        # You can resize the size of the QLineEdit Widget by using the 
        # QLineEdit.resize(x,y) function
        self.name_entry.resize(200,20)
        
        # If you need the user to enter multiple lines of text then you must use
        # QTextEdit instead of QLineEdit
        
        # Creating a clear button
        self.clear_button = QPushButton('Clear',self)
        self.clear_button.clicked.connect(self.clearEntries)
        self.clear_button.move(160,110)
    
    def clearEntries(self):
        # Function to clear the text on the QlineEdit
        # We use the sender() to identify the source of the signal
        # Here as we have named our button 'Clear' therefore if the
        # sender receives a signal with the text 'Clear' we can confirm
        # that it is our button which has sent the signal
        sender = self.sender()
        if sender.text() == 'Clear':
            self.name_entry.clear()
            # We user QLineEdit.clear() function to clear the text in the LineEdit

# Running the program
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EntryWindow()
    sys.exit(app.exec_())
        
        