# Project : Applicaiton Form
# This is will make use of QFormLayout which is especially designed to create forms
# i.e. label on the left and entry field on the rights

import sys
from PyQt5.QtWidgets import (QApplication,QWidget,QLabel,QPushButton,QFormLayout,
                             QHBoxLayout,QSpinBox,QComboBox,QLineEdit,
                             QTextEdit)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class GetApptForm(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initializeUI()
        
    def initializeUI(self):
        
        self.setGeometry(100,100,300,400)
        self.setWindowTitle("Application Form")
        self.formWidgets()
        
        self.show()
    
    def formWidgets(self):
        # Create widgets to be used in the form
        
        title = QLabel("Application Submission Form")
        title.setFont(QFont('Ariel',18))
        title.setAlignment(Qt.AlignCenter)
            
        name = QLineEdit()
        name.resize(100,100)
        address = QLineEdit()
        mobile_num = QLineEdit()
        mobile_num.setInputMask("000-000-0000")
        
        age_label = QLabel("Age")
        age = QSpinBox()
        age.setRange(1,110)
        height_label = QLabel("Height")
        height = QLineEdit()
        height.setPlaceholderText("cm")
        weight_label = QLabel("Weight")
        weight = QLineEdit()
        weight.setPlaceholderText("kg")
        
        gender = QComboBox()
        gender.addItems(['Male','Female'])
        
        surgery = QTextEdit()
        surgery.setPlaceholderText("separated by ','")
        blood_type = QComboBox()
        blood_type.addItems(['A','B','AB','O'])
        
        hours = QSpinBox()
        hours.setRange(1,12)
        minutes = QComboBox()
        minutes.addItems([':00',':15',':30',':45'])
        am_pm = QComboBox()
        am_pm.addItems(['AM','PM'])

        submit_button = QPushButton("Submit Appointment")
        submit_button.clicked.connect(self.close)
        
        # Create a horizontal layout and add age,weight and height
        h_box = QHBoxLayout()
        h_box.setSpacing(10)
        h_box.addWidget(age_label)
        h_box.addWidget(age)
        h_box.addWidget(height_label)
        h_box.addWidget(height)
        h_box.addWidget(weight_label)
        h_box.addWidget(weight)
        
        # Create horizontal layout and add time information
        time_h_box = QHBoxLayout()
        time_h_box.addSpacing(10)
        time_h_box.addWidget(hours)
        time_h_box.addWidget(minutes)
        time_h_box.addWidget(am_pm)
        
        # Create a form layout
        app_form_layout = QFormLayout()
        # Add components using the addRow('message',widget) method
        # The message is added automatically to the left side of the entry field
        app_form_layout.addRow(title)
        app_form_layout.addRow("Full Name",name)
        app_form_layout.addRow("Address",address)
        app_form_layout.addRow("Mobile Number",mobile_num)
        app_form_layout.addRow(h_box)
        app_form_layout.addRow("Gender",gender)
        app_form_layout.addRow("Past Surgeries",surgery)
        app_form_layout.addRow("Blood Type",blood_type)
        app_form_layout.addRow("Desired Time",time_h_box)
        app_form_layout.addRow(submit_button)
        
        self.setLayout(app_form_layout)
    
def main():
    app = QApplication(sys.argv)
    window = GetApptForm()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
        
        
        
        
        