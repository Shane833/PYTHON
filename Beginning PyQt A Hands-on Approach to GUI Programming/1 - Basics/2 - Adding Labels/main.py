import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap
# We import QLabel widget whose object can act as a non-editable place-holder for
# text, image or movies
# QLabel widgets can display plain text, hyperlinks and rich text

# Alongside importing the QLabel form QtWidgets, we also import the QtGui module
# QtGui is responsible for handling various GUI elements
# QPixmap is Qt class optimized for showing images on the screen

class HelloPeter(QWidget):
    # Constructor
    def __init__(self):
        super().__init__()
        self.initializeUI()
    
    def initializeUI(self):
        self.setWindowTitle("Hello from Peter")
        self.setGeometry(100,100,400,400)
        self.displayLabels() # Custom function to declare and display labels
        
        self.show()
    
    def displayLabels(self):
        # Displaying text and images
        text = QLabel(self) 
        # To create an object of the QLabel we use the following convention
        # obj = QLable(widget_obj)
        # It is necessary to provide the widget where you wish to display the Label
        
        # some of the methods that can be used on QLable objects are:
        # 1. QLabel.setText("Your message here")
        text.setText("Hello from Joker Peter hehe!!")
        # 2. QLabel.move(x,y) : This depicts the position of the label within
        # the specified QWidget
        text.move(205,15)
        
        # Storing the path the image
        image = "Peter.gif"
        
        # Opening the image
        try:
            with open(image):
                # First we declare a label
                peter_image = QLabel(self)
                # Then we create an object of QPixmap to hold our image
                pixmap = QPixmap(image)
                # Then we provide it to the QLabel
                peter_image.setPixmap(pixmap)
                # Then we finally define its position on the screen
                peter_image.move(100,100)
                
        except FileNotFoundError:
            print("Image not found")

# Finally running the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HelloPeter()
    sys.exit(app.exec_())