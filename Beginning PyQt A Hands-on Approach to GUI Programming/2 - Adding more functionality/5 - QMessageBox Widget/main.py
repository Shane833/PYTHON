import sys
from PyQt5.QtWidgets import (QApplication, QLabel, QWidget, QPushButton,
QLineEdit, QMessageBox)
from PyQt5.QtGui import QFont

# Imported an additional QMessageBox module to be used in the program
# MessageBoxes are helpful not only to alert the user but also allow
# them to decide how to handle the situation

# There are mainly 4 types of QMessageBox
# 1. Question : Ask the user question
# 2. Information : Display information during normal operations
# 3. Warning : Report critical errors
# 4. Critical : Report critical errors

class DisplayMessageBox(QWidget):
    # Constructor
    def __init__(self):
        super().__init__()
        self.initializeUI()
    
    def initializeUI(self):
        self.setGeometry(100,100,400,200)
        self.setWindowTitle("QMessageBox Window")
        self.displayWidgets()
        
        self.show()
        
    def displayWidgets(self):
        
        catalogue_label = QLabel("Author Catalogue",self)
        catalogue_label.move(20,20)
        catalogue_label.setFont(QFont('Ariel',20))
        
        auth_label = QLabel("Enter the name of the author you are searching for :",self)
        auth_label.move(40,60)
        
        # Creating author label and line edit widget
        author_name = QLabel("Name:",self)
        author_name.move(50,90)
        
        self.auth_entry = QLineEdit(self)
        self.auth_entry.move(95,90)
        self.auth_entry.resize(240,20)
        # Provide some initial text in the QLineEdit instead of an empty field
        # with the help of setPlaceholderText("Message") method
        self.auth_entry.setPlaceholderText("firstname lastname")
        
        # Creating a search button
        search_button = QPushButton('Search',self)
        search_button.move(125,130)
        search_button.resize(150,40)
        search_button.clicked.connect(self.displayMessageBox)
            
    def displayMessageBox(self):
        # This function will be called when the search button is clicked
        # It will simply read the contents of the QLineEdit and search for
        # the author name in the list, and if found display the Author found dialog
        # else Author not found dialog
        
        # Check if the author's file exists
        try:
            with open("authors.txt","r") as f:
                authors = [line.rstrip('\n') for line in f]
        except FileNotFoundError:
            print("The file cannot be found")
        
        # Checking for name in the list
        not_found_msg = QMessageBox()
        # We create this object prior in order to avoid 'referenced before
        # assignment' error
        
        # In this section we are searching if the input string exists in the
        # authors list
        if self.auth_entry.text() in authors:
        # If we do find that author in the list then we can display a messagebox
        # indicating that the entered author was found
        
            # In order to create a MessageBox dialogbox follow the given convention
            # Your first step is to identify the kind of MessageBox you require
            # You can choose from the above discussed types like:
            # 1. information 2. question 3. warning 4. critical
            # message_box = QMessageBox.type(parent QWidget,"Title here","Actual message here",
                                           # QMessageBox.Button | QMessageBox.Button,QMessageBox.Button)
            # The second last parameter includes all the buttons to be included in the dialog box
            # Different buttons include: 1.Yes 2.No 3.Ok 4.Save 5.Open 6.Cancel 7.Reset
            # All the included buttons must be included by the pipe operation '|'
            # The last argument depicts which button is to be selected by default
            QMessageBox.information(self,"Author Found","Author found in Catalogue",
                                    QMessageBox.Ok,QMessageBox.Ok)
            # Instead of providing the title and text at the time of initialization
            # You can provide these informations separately using setWindowTitle() and setText() methods
        else:
            not_found_msg = QMessageBox.question(self,"Author not found",
                        "Author not found in the catalogue.\nDo you wish to continue?",
                        QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
        
        # At the last we will ckeck which button was pressed and if No was selected we exit the app
        if not_found_msg == QMessageBox.No:
            print("Closing Application")
            self.close()
            
# Running the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DisplayMessageBox()
    sys.exit(app.exec_())