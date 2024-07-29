# Project 4.1 Notepad GUI
import sys
from PyQt5.QtWidgets import (QApplication,QWidget,QPushButton,QLabel,QTextEdit,
                            QMessageBox,QFileDialog)

class notepad(QWidget):

    # Constructor
    def __init__(self):
        super().__init__()
        self.initializeUI()
        
    # Initialization function
    def initializeUI(self):
        self.setGeometry(100,100,300,400)
        self.setWindowTitle("Notepad GUI")
        self.notepadWidgets()
        
        self.show()
    
    def notepadWidgets(self):
        # Two push buttons for new and save
        new_button = QPushButton("New",self)
        new_button.move(10,20)
        new_button.clicked.connect(self.clearText)
        
        save_button = QPushButton("Save",self)
        save_button.move(80,20)
        save_button.clicked.connect(self.saveText)
    
        # Text field for user data
        self.text_field = QTextEdit(self)
        self.text_field.resize(280,330)
        self.text_field.move(10,60)
    
    def clearText(self):
        # Ask the user first if he really want to clear text
        answer = QMessageBox.question(self,"Clear Text","Do you want to clear the text",
                                      QMessageBox.No | QMessageBox.Yes,QMessageBox.Yes)
        
        if answer == QMessageBox.Yes:
            self.text_field.clear()
        else:
            pass
    
    def saveText(self):
        # This will display a file dialog to let the user save his data to a text file
        # To create a file dialog follow the given steps
        # file_diag_obj = QFileDialog.get____FileName(parent,"Title","Default directory path",
        #                                            "File type to be searched separated by ';;'",options = QFileDialog.Options())
        # The ____ is for either Open or Save depending upon what you want
        # The look of the file dialog will be system specific if you don't want that, the modify QFileDialog.Options()
        # For eg:
        #       options = QFileDialog.Options()
        #       options = QFileDialog.DontUseNativeDialog
        #       pass this as the options by using the QFileDialog
        
        options = QFileDialog.Options()
        # You can obtain the text from text field using this method
        notepad_text = self.text_field.toPlainText()
        
        file_name = QFileDialog.getSaveFileName(self,"Save File","","All Files (*) ;; Text Files(*.txt)",
                                                options = options)
        # Checking the path is valid then create the file and save content to it
        if file_name:
            f = open(file_name[0],'w')
            f.write(notepad_text)
            
def main():
    # Main Entry point
    app = QApplication(sys.argv)
    window = notepad()
    sys.exit(app.exec_())
    

if __name__ == "__main__":
    main()
    # The main purpose of this project was to showcase