# This project is aimed around the QGridLayout
# Project - to-do list
import sys
from PyQt5.QtWidgets import (QApplication,QWidget,QLabel,QTextEdit,QLineEdit,
                             QPushButton,QCheckBox,QVBoxLayout,QGridLayout)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class ToDoList(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()
    
    def initializeUI(self):
        self.setGeometry(100,100,500,350)
        self.setWindowTitle("To Do List")
        self.setupWidgets()
        
        self.show()
    
    def setupWidgets(self):
        # Create widgets and arrange them in the window
        # Create the grid layout
        main_grid = QGridLayout()
        
        todo_title = QLabel("To Do List")
        todo_title.setFont(QFont('Ariel',24))
        todo_title.setAlignment(Qt.AlignCenter)
        
        close_button = QPushButton("Close")
        close_button.clicked.connect(self.close)
        
        # Create labels for different sections
        mustdo_label = QLabel("Must Dos")
        mustdo_label.setFont(QFont('Ariel',20))
        mustdo_label.setAlignment(Qt.AlignCenter)
        appts_label = QLabel("Appointments")
        appts_label.setFont(QFont('Ariel',20))
        appts_label.setAlignment(Qt.AlignCenter)
        
        # Create must do section
        mustdo_grid = QGridLayout()
        mustdo_grid.setContentsMargins(5,5,5,5)
        # The setContentsMargins defines the border in pixels from left,top,right,bottom
        mustdo_grid.addWidget(mustdo_label,0,0,1,2)
        
        # Create checkboxes and line edit widgets
        for position in range(1,15):
            checkbox = QCheckBox()
            checkbox.setChecked(False)
            linedit = QLineEdit()
            linedit.setMinimumWidth(200)
            mustdo_grid.addWidget(checkbox,position,0)
            mustdo_grid.addWidget(linedit,position,1)
            # Adding widgets to the grid layout is very easy
            # Just follow this convention
            # grid.addWidget/Layout(obj_name,row_no,col_no)
            
        # Create labels for appointment section
        morning_label = QLabel("Morning")
        morning_label.setFont(QFont('Ariel',16))
        morning_entry = QTextEdit()
        noon_label = QLabel("Noon")
        noon_label.setFont(QFont('Ariel',16))
        noon_entry = QTextEdit()
        evening_label = QLabel("Evening")
        evening_label.setFont(QFont('Ariel',16))
        evening_entry = QTextEdit()
        
        # Create veritcal layout and add widgets
        appt_v_box = QVBoxLayout()
        appt_v_box.setContentsMargins(5,5,5,5)
        
        appt_v_box.addWidget(appts_label)
        appt_v_box.addWidget(morning_label)
        appt_v_box.addWidget(morning_entry)
        appt_v_box.addWidget(noon_label)
        appt_v_box.addWidget(noon_entry)
        appt_v_box.addWidget(evening_label)
        appt_v_box.addWidget(evening_entry)
        
        # Add other layouts to the main grid
        main_grid.addWidget(todo_title,0,0,1,2)
        # While adding widgets you can specify how much area should it span/cover
        # The two addtional arguments determines that how many rows and columns it
        # should cover, so in this case it is going to cover 1 row and 2 columns
        main_grid.addLayout(mustdo_grid,1,0)
        main_grid.addLayout(appt_v_box,1,1)
        main_grid.addWidget(close_button,2,0,1,2)
        
        self.setLayout(main_grid)
    
def main():
    app = QApplication(sys.argv)
    window = ToDoList()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()