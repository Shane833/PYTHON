# Rich Text Notepad GUI with modern features
import sys
from PyQt5.QtWidgets import (QApplication,QMainWindow,QAction,QMessageBox,
                         QTextEdit,QFileDialog,QInputDialog,QFontDialog,
                         QColorDialog)
from PyQt5.QtGui import QIcon, QTextCursor, QColor
from PyQt5.QtCore import Qt

class Notepad(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initializeUI()
    
    def initializeUI(self):
        # Initialize the window display the contents to the screen
        self.setGeometry(100,100,400,500)
        self.setWindowTitle("Rich Notepad GUI")
        self.createNotepadWidget()
        self.notepadMenu()
        
        self.show()
    
    def createNotepadWidget(self):
        # Set the central widget for the window which the QTextEdit
        self.text_field = QTextEdit()
        self.setCentralWidget(self.text_field)
    
    def notepadMenu(self):
        # Create menu for Notepad GUI
        
        # Create actions for the file menu
        new_act = QAction('New',self)
        # You can also add an icon to the QAction by providing it int the arguments
        # => act = QAction(QIcon(Path),String,Parent)
        new_act.setShortcut('Ctrl+N')
        new_act.triggered.connect(self.clearText)
        
        open_act = QAction('Open',self)
        open_act.setShortcut('Ctrl+O')
        open_act.triggered.connect(self.openFile)
        
        save_act = QAction('Save',self)
        save_act.setShortcut('Ctrl+S')
        save_act.triggered.connect(self.saveToFile)
        
        exit_act = QAction('Exit',self)
        exit_act.setShortcut('Ctrl+Q')
        exit_act.triggered.connect(self.close)
        
        # Create actions for edit menu
        undo_act = QAction('Undo',self)
        undo_act.setShortcut('Ctrl+Z')
        undo_act.triggered.connect(self.text_field.undo)
        
        redo_act = QAction('Redo',self)
        redo_act.setShortcut('Ctrl+Shift+Z')
        redo_act.triggered.connect(self.text_field.redo)
        
        cut_act = QAction('Cut',self)
        cut_act.setShortcut('Ctrl+X')
        cut_act.triggered.connect(self.text_field.cut)
        
        copy_act = QAction('Copy',self)
        copy_act.setShortcut('Ctrl+C')
        copy_act.triggered.connect(self.text_field.copy)
        
        paste_act = QAction('Paste',self)
        paste_act.setShortcut('Ctrl+V')
        paste_act.triggered.connect(self.text_field.paste)
        
        find_act = QAction('Find',self)
        find_act.setShortcut('Ctrl+F')
        find_act.triggered.connect(self.findTextDialog)
        
        # Create actions for tools menu
        font_act = QAction('Font',self)
        font_act.setShortcut('Ctrl+F')
        font_act.triggered.connect(self.chooseFont)
        
        color_act = QAction('Color',self)
        color_act.setShortcut('Ctrl+Shift+C')
        color_act.triggered.connect(self.chooseFontColor)
        
        highlight_act = QAction('HighLight',self)
        highlight_act.setShortcut('Ctrl+Shift+H')
        highlight_act.triggered.connect(self.chooseFontBackgroundColor)
        
        about_act = QAction('About',self)
        about_act.triggered.connect(self.aboutDialog)
        
        # Create Menubar
        menu_bar = self.menuBar()
        
        # Create File menu and add actions
        file_menu = menu_bar.addMenu('File')
        file_menu.addAction(new_act)
        file_menu.addSeparator()
        file_menu.addAction(open_act)
        file_menu.addAction(save_act)
        file_menu.addSeparator()
        file_menu.addAction(exit_act)
        
        # Create edit menu and add actions
        edit_menu = menu_bar.addMenu('Edit')
        edit_menu.addAction(undo_act)
        edit_menu.addAction(redo_act)
        edit_menu.addSeparator()
        edit_menu.addAction(cut_act)
        edit_menu.addAction(copy_act)
        edit_menu.addAction(paste_act)
        edit_menu.addSeparator()
        edit_menu.addAction(find_act)
        
        # Create tools menu and add actions
        tools_menu = menu_bar.addMenu('Tools')
        tools_menu.addAction(font_act)
        tools_menu.addAction(color_act)
        tools_menu.addAction(highlight_act)
        
        # Create help menu and add actions
        help_menu = menu_bar.addMenu('Help')
        help_menu.addAction(about_act)
        
      
    def openFile(self):
        # To open a text or html file and display its contents on the screen
        file_name, _ = QFileDialog.getOpenFileName(self,"Open File","","HTML Files (*.html);;Text Files(*.txt)")
            
        if file_name:   
            with open(file_name,'r') as f:   
                notepad_text = f.read()
                self.text_field.setText(notepad_text)
        else:
            QMessageBox.information(self,"Error","Unable to Open File",QMessageBox.Ok)
    
    def saveToFile(self):
        # Saves the content of the textedit field to a file
        file_name, _ = QFileDialog.getSaveFileName(self,"Save File","","HTML Files(*.html);;Text Files(*.txt)")
        
        if file_name.endswith('.txt'):
            notepad_text = self.text_field.toPlainText()
            with open(file_name,'w') as f:
                f.write(notepad_text)
        elif file_name.endswith('.html'):
            notepad_rich_text = self.text_field.toHtml()
            with open(file_name,'w') as f:
                f.write(notepad_rich_text)
        else:
            QMessageBox.information(self,"Error","Unable to Save File",QMessageBox.Ok)
        
    def clearText(self):
        # When the new button is clicked, display a dialog asking if the
        # user want to clear the text field or not
        
        answer = QMessageBox.question(self,"Clear Text","Do you want to clear the text?",
                                      QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes) 
        
        if answer == QMessageBox.Yes:
            self.text_field.clear()
        else:
            pass
    
    def findTextDialog(self):
        # Search for the text in the text field and highlight the occurences
        
        # Display the Input Dialog box to take the input text from user
        find_text, ok = QInputDialog.getText(self,"Search Text","Find:")
        
        extra_selection = []
        
        # Check to make the sure the text can be modified
        if ok and not self.text_field.isReadOnly():
            # Set the text cursor to the beginning
            self.text_field.moveCursor(QTextCursor.Start)
            color = QColor(Qt.yellow)
            
            # Look for the next occurence of the text
            while(self.text_field.find(find_text)):
                # Use ExtraSelections() to mark the text you are looking for
                # as yellow
                selection = QTextEdit.ExtraSelection()
                selection.format.setBackgroundColor(color)
            
                # Set the cursor of the selection
                selection.cursor = self.text_field.textCursor()
                
                # Add the selections to the list
                extra_selections.append(selection)
            
            # Highlight the sections in the text widget
            for i in extra_selection:   
                self.text_field.setExtraSelections(extra_selections)
                
    def chooseFont(self):
        # Select the font for the text
        current = self.text_field.currentFont()
        font, ok = QFontDialog.getFont(current,self)
        
        if ok:
            self.text_field.setCurrentFont(font)
            # You can use the setFont() to set that font for all text
        
    def chooseFontColor(self):
        # Select color for text
        color = QColorDialog.getColor()
        if color.isValid():
            self.text_field.setTextColor(color)
    
    def chooseFontBackgroundColor(self):
        # Select color for text's background
        color = QColorDialog.getColor()
        if color.isValid():
            self.text_field.setTextBackgroundColor(color)
    
    def aboutDialog(self):
        # Displays information about the program
        QMessageBox.about(self,"About Notepad","Notepad GUI")
        
    
def main():
    app = QApplication(sys.argv)
    window = Notepad()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
        
        
        
        
        