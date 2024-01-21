# This is a procedural way to perfom the same task of creating an empty window
import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    window.setGeometry(100,100,200,100)
    window.show()
    sys.exit(app.exec_())