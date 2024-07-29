import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton

# Importing the 

class ButtonWindow(QWidget):
    # Construcutor
    def __init__(self):
        super().__init__()
        self.initializeUI()
    
    def initializeUI(self):
        self.setGeometry(100,100,200,150)
        self.setWindowTitle("QPushButton Widget")
        # Functin to display the buttons to the screen
        self.displayButton()
        
        self.show()
    
    def displayButton(self):
        # Creating a label
        name_label = QLabel(self)
        name_label.setText("Don't push the button")
        name_label.move(50,30)
        
        # Creating QPushButton
        # You should use the following convention
        # button = QPushButton('Button Message here',QWidget)
        # The first argument is the message to be displayed on the button
        # and the second is the instance of QWidget / window where it is to be displayed
        button = QPushButton('Push me',self) 
        # Alternatively you could also set the text on the button as
        # button.setText("Text here")
        
        # Connecting a button click to a functiion
        # In order to specify what would happend when the button is clicked
        # You must connect that event with a function
        # In order to do so, You must follow the given convention
        # button_obg.clicked.connect(function_name)
        button.clicked.connect(self.buttonClicked)
        # So the working of this is as follows
        # 1. Whenever your button is clicked it sends out a singal'clicked()'
        # 2. So after we receive the signal we use'connect()' to connect the signal
        # to the action we want the button to perform
        
        # Along with getting activated by a click of the mouse we can activate
        # the button with either the spacebar or a keyboard shotcut
        # In addtion to the signal clicked(), there exits pressed(), released(), and toggled()
        
        button.move(60,70)
    
    def buttonClicked(self):
        # This function will be called when the button is cliked
        # The functionality of this function will be to print a message and then close the app
        print("The window has been closed")
        # In order to close any widget we use the QWidget.close() function
        self.close() # This is close the widget
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ButtonWindow()
    sys.exit(app.exec_())