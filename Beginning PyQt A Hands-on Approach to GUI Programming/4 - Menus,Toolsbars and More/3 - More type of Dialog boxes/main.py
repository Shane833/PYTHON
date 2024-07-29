# Implementing the various kinds of dialog boxes with buttons for each
# one of them

import sys
from PyQt5.QtWidgets import (QApplication,QWidget,QPushButton,QInputDialog,
                             QFontDialog,QColorDialog,QMessageBox,QVBoxLayout)
                             
class DialogBoxes(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()
    
    def initializeUI(self):
        self.setWindowTitle("Dialog Boxes")
        self.setGeometry(100,100,300,300)
        self.dialogs()
        
        self.show()
    
    def dialogs(self):
        # Creating buttons 
        input_button = QPushButton("Input Dialog",self)
        input_button.clicked.connect(self.inputDialog)
        
        font_button = QPushButton("Font Dialog",self)
        font_button.clicked.connect(self.fontDialog)
        
        color_button = QPushButton("Color Dialog",self)
        color_button.clicked.connect(self.colorDialog)
        
        about_button = QPushButton("About Dialog",self)
        about_button.clicked.connect(self.aboutDialog)
        
        
        # Layout to hold the buttons
        v_box = QVBoxLayout()
        
        # Adding the buttons
        v_box.addWidget(input_button)
        v_box.addWidget(font_button)
        v_box.addWidget(color_button)
        v_box.addWidget(about_button)

        
        # Setting the main layout
        self.setLayout(v_box)
        
    def inputDialog(self):
        say_something, ok = QInputDialog.getText(self,"Whats on your mind","Tell me")
        # Using the QInputDialog you can read string, numbers and lists of things from
        # the users, You use the getText(parent,message) to get a single line of string
        # from the user. the second variable returned is a boolean if its true that means
        # the user has pressed the OK button
        
        # Along with getText() method there are several other methods for specific use
        # getMultiLineText()
        # getInt()
        # getDouble()
        # getItem() - lets the select an item from a list of strings
        
    def fontDialog(self):
        font, ok = QFontDialog.getFont()
        # The ok variables behaves the same way as in the QInputDialog
        # So when the user clicks the ok button a font is set to a QFont object
        # If cancel is clicked then its position reverts back to the default
        # If you don't want it to revert back to the default then declare like this
        # font,ok = QFontDialog.getFont(QFont("Helvetica",10),self)
        # self.text_edit.setCurrentFont(font)
        
    def colorDialog(self):
        color = QColorDialog.getColor()
        # There is no OK variables however you can check isValid() method to do the same
        # if color.isValid():
        #   self.text_field.setTextColor(color)
        # You can also use setBackgroundColor() to change the background color
    
    def aboutDialog(self):
        QMessageBox.about(self,"Testing","This is a test for about dialog box")
        # An Icon must be provided to the dialog box if no icon is provided it looks for
        # the icon on the parent
        # So you may set the icon like app.setWindowIcon(QIcon()) to display the same on
        # the about dialog box
        
def main():
    app = QApplication(sys.argv)
    window = DialogBoxes()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
        