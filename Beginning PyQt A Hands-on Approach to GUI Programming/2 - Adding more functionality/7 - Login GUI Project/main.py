import sys
from PyQt5.QtWidgets import (QApplication,QWidget,QPushButton,QLabel,
                            QMessageBox,QCheckBox,QLineEdit)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from Registration import CreateNewUser

class LoginUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()
    
    def initializeUI(self):
        self.setGeometry(100,100,400,230)
        self.setWindowTitle("Login Screen")
        self.loginUserInterface()
        
        self.show()
    
    def loginUserInterface(self):
        
        login_label = QLabel("login",self)
        login_label.move(180,10)
        login_label.setFont(QFont('Ariel',20))
        
        # Username and password labels and lineedits
        name_label = QLabel("username:",self)
        name_label.move(30,60)
        
        self.name_entry = QLineEdit(self)
        self.name_entry.move(110,60)
        self.name_entry.resize(220,20)
        
        pswd_label = QLabel("password:",self)
        pswd_label.move(30,90)
        
        self.pswd_entry = QLineEdit(self)
        self.pswd_entry.move(110,90)
        self.pswd_entry.resize(220,20)
        
        # Sign in button
        sign_in_button = QPushButton("Sign-in",self)
        sign_in_button.move(100,140)
        sign_in_button.resize(200,40)
        sign_in_button.clicked.connect(self.clickLogin)
        
        # show password checkbox
        show_pswd_cb = QCheckBox("show password",self)
        show_pswd_cb.move(110,115)
        show_pswd_cb.stateChanged.connect(self.showPassword)
        show_pswd_cb.toggle()
        show_pswd_cb.setChecked(False)
        
        # Sign up label and push button
        not_a_member = QLabel("not a member?",self)
        not_a_member.move(70,200)
        
        sign_up = QPushButton("Sign up",self)
        sign_up.move(160,195)
        sign_up.clicked.connect(self.createNewUser)
    
    def clickLogin(self):
        # Check if the login credentials are valid or not
        # if valid - close program
        # if not - display error message
        
        # Empty dictionary to store user info
        users = {}
        
        try:
            with open("users.txt",'r') as f:
                for line in f:
                    user_fields = line.split(" ") # Splitting the string 
                    username = user_fields[0]
                    password = user_fields[1].strip('\n')
                    users[username] = password # adding entries to the dictionary
        except FileNotFoundError:
            print("The file does not exist. Creating a new file.")
            f = open("users.txt",'w')
        
        username = self.name_entry.text()
        password = self.pswd_entry.text()
        
        # Checking if the key-value pair exists
        if (username,password) in users.items():
            QMessageBox.information(self,"Login Succesful!!!","Login Successful!!!",
                                    QMessageBox.Close,QMessageBox.Close)
        else:
            QMessageBox.warning(self,"Error Message!!!","The username/password is incorrect",
                                QMessageBox.Close,QMessageBox.Close)
                                
    def showPassword(self,state):
        # If checked show password else don't
        if state == Qt.Checked:
            self.pswd_entry.setEchoMode(QLineEdit.Normal)
        else:
            self.pswd_entry.setEchoMode(QLineEdit.Password)
        
    def createNewUser(self):
        # Allow the user to create a new account by opening a new window
        self.create_new_user_dialog = CreateNewUser()
        # To display the widget on the screen user the show() method explicitely
        self.create_new_user_dialog.show()
    
    # Basically overwriting closeEvent(event) method
    # Whenever a QWidget gets closed it generated a QCloseEvent
    # We can either choose to accept this event or ignore it
    def closeEvent(self,event):
        # Asking user if they really want to quit
        
        quit_msg = QMessageBox.question(self,"Quit Application?",
                                        "Are you sure you want to Quit?",
                                        QMessageBox.No | QMessageBox.Yes,
                                        QMessageBox.Yes)
        
        if quit_msg == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

# Running the application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginUI()
    sys.exit(app.exec_())