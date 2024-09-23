# Creating a user profile
import sys,os.path
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap, QFont
# The only additional things we have imported this time are the QFont which lets
# us choose a variety of fonts along with specifying the text size
# and additionally we have also imported os.path

class UserProfile(QWidget):
    # Constructor
    def __init__(self):
        super().__init__() # Calling the super constructor
        self.initializeUI()
     
    def initializeUI(self):
        self.setGeometry(50,50,250,400)
        self.setWindowTitle("User Profile")
        # The order of calling these functions is important as they act as layer
        # The layer that is created first (say background) will be displayed in
        # last and vice versa
        self.displayImages()
        self.displayUserInfo()
        
        self.show()
    
    def displayImages(self):
        image = "Peter.gif"
        
        try:
            with open(image):
                bg_image = QLabel(self)
                pixmap = QPixmap(image)
                bg_image.setPixmap(pixmap)
                
        except FileNotFoundError:
            print("Image not found")
            
    
    def displayUserInfo(self):
        # Creating labels to display text to the screen
        user_name = QLabel(self)
        user_name.setText("Shane da Man")
        user_name.move(85,140)
        # Using QFont to add different fonts and style to your texts
        # So the way to user it you proive 2 arguments to the QFont
        # font = QFont('Font_name',font_size)
        user_name.setFont(QFont('Ariel',20))
        
        bio_title = QLabel(self)
        bio_title.setText("Biography")
        bio_title.move(15,170)
        bio_title.setFont(QFont('Ariel',17))
        
        about = QLabel(self)
        about.setText("I am a student and computer enthusiast who is learning new things")
        # Word Wrap is a feature in word processors which automatically wraps/
        # shifts the words to the next line afer reaching a specified margin
        about.setWordWrap(True)
        about.move(15,200)
        
        skills_title = QLabel(self)
        skills_title.setText("Skills")
        skills_title.move(15,240)
        skills_title.setFont(QFont('Ariel',17))
        
        skills = QLabel(self)
        skills.setText("C/C++ | Python | Java")
        skills.move(15,270)
        
        exp_title = QLabel(self)
        exp_title.setText("Experience")
        exp_title.move(15,290)
        exp_title.setFont(QFont('Ariel',17))
        
        experience = QLabel(self)
        experience.setText("Software Developer")
        experience.move(15,320)
        experience.setFont(QFont('Ariel',12))
        
        dates = QLabel(self)
        dates.setText("Oct 2021 - Present")
        dates.move(15,340)
        dates.setFont(QFont('Ariel',10))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    resume = UserProfile()
    sys.exit(app.exec_())