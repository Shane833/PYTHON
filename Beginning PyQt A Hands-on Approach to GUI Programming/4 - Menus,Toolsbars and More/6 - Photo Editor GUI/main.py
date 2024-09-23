import sys
from PyQt5.QtWidgets import (QApplication,QMainWindow,QWidget,QLabel,QAction,
                             QFileDialog,QDesktopWidget,QMessageBox,QSizePolicy,
                             QToolBar,QStatusBar,QDockWidget,QVBoxLayout,QPushButton)
from PyQt5.QtGui import QIcon,QPixmap,QTransform,QPainter
from PyQt5.QtCore import Qt,QSize,QRect
from PyQt5.QtPrintSupport import QPrinter,QPrintDialog

class PhotoEditor(QMainWindow):
    # Constructor
    def __init__(self):
        super().__init__()
        self.initializeUI()
    
    def initializeUI(self):
        # Initialize the window and display its contents to the screen
        self.setFixedSize(650,650) # Fixes the size of the window
        self.setWindowTitle('5.2 - Photo Editor GUI')
        self.centerMainWindow()
        self.createToolsDockWidget()
        self.createMenu()
        self.createToolBar()
        self.photoEditorWidgets()
        
        self.show()
    
    def createMenu(self):
        # Create menu for photo editor GUI
        
        # Create actions for the file menu
        self.open_act = QAction("Open",self)
        self.open_act.setShortcut("Ctrl+O")
        self.open_act.setStatusTip("Open a new Image")
        self.open_act.triggered.connect(self.openImage)

        self.save_act = QAction("Save",self)
        self.save_act.setShortcut("Ctrl+S")
        self.save_act.setStatusTip("Save Image")
        self.save_act.triggered.connect(self.saveImage)
        
        self.print_act = QAction("Print",self)
        self.print_act.setShortcut("Ctrl+P")
        self.print_act.setStatusTip("Print Image")
        self.print_act.triggered.connect(self.printImage)
        self.print_act.setEnabled(False) # Comment here
        
        self.exit_act = QAction("Exit",self)
        self.exit_act.setShortcut("Ctrl+Q")
        self.exit_act.setStatusTip("Quit Program")
        self.exit_act.triggered.connect(self.close)
        
        # Create actions for the edit menu
        self.rotate90_act = QAction("Rotate 90",self)
        self.rotate90_act.setStatusTip("Rotate Image 90 clockwise")
        self.rotate90_act.triggered.connect(self.rotateImage90)
        
        self.rotate180_act = QAction("Rotate 180",self)
        self.rotate180_act.setStatusTip("Rotate Image 180 clockwise")
        self.rotate180_act.triggered.connect(self.rotateImage180)
        
        self.flip_hor_act = QAction("Flip Horizontal",self)
        self.flip_hor_act.setStatusTip("Flip Image across Horizontal Axis")
        self.flip_hor_act.triggered.connect(self.flipImageHorizontal)
        
        self.flip_ver_act = QAction("Flip Veritcal",self)
        self.flip_ver_act.setStatusTip("Flip Image across Vertical Axis")
        self.flip_ver_act.triggered.connect(self.flipImageVertical)
        
        self.resize_act = QAction("Resize Half",self)
        self.resize_act.setStatusTip("Resize image to Half the original size")
        self.resize_act.triggered.connect(self.resizeImageHalf)
        
        self.clear_act = QAction("Clear Image",self)
        self.clear_act.setShortcut("Ctrl+D")
        self.clear_act.setStatusTip("Clear the Current Image")
        self.clear_act.triggered.connect(self.clearImage)
        
        # Create a Menubar
        menu_bar = self.menuBar()
        menu_bar.setNativeMenuBar(False)
        
        # Create File Menu and add actions
        file_menu = menu_bar.addMenu('File')
        file_menu.addAction(self.open_act)
        file_menu.addAction(self.save_act)
        file_menu.addSeparator()
        file_menu.addAction(self.print_act)
        file_menu.addSeparator()
        file_menu.addAction(self.exit_act)
        
        # Create Edit Menu and add Actions
        edit_menu = menu_bar.addMenu('Edit')
        edit_menu.addAction(self.rotate90_act)
        edit_menu.addAction(self.rotate180_act)
        edit_menu.addSeparator()
        edit_menu.addAction(self.flip_hor_act)
        edit_menu.addAction(self.flip_ver_act)
        edit_menu.addSeparator()
        edit_menu.addAction(self.resize_act)
        edit_menu.addSeparator()
        edit_menu.addAction(self.print_act)
        
        # Create View Menu and add Widget
        view_menu = menu_bar.addMenu("View")
        view_menu.addAction(self.toggle_dock_tools_act)
        
        # Display information about the tools, menu and view in the status bar
        self.setStatusBar(QStatusBar(self))
        
        
    def centerMainWindow(self):
        pass
        
    def createToolBar(self):    
        # Create toolbar for photo editor GUI
        
        tool_bar = QToolBar("Photo Editor ToolBar")
        tool_bar.setIconSize(QSize(24,24))
        self.addToolBar(tool_bar)
        
        # Add Actions to toolbar
        tool_bar.addAction(self.open_act)
        tool_bar.addAction(self.save_act)
        tool_bar.addAction(self.print_act)
        tool_bar.addAction(self.clear_act)
        tool_bar.addSeparator()
        tool_bar.addAction(self.exit_act)
    
    def createToolsDockWidget(self):
        # Use View -> Edit Image Tool menu and click the dock widget on or off
        # Tools dock can be placed on left or right side of the window
        
        # Setup DockWidget
        self.dock_tools_view = QDockWidget()
        self.dock_tools_view.setWindowTitle("Edit Image Tools")
        self.dock_tools_view.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        
        # Create a container to hold all the widgets inside dock widget
        self.tools_content = QWidget()
        
        # Create tools push button
        self.rotate90 = QPushButton("Rotate 90")
        self.rotate90.setMinimumSize(QSize(130,40))
        self.rotate90.setStatusTip('Rotate Image 90 Clockwise')
        self.rotate90.clicked.connect(self.rotateImage90)
        
        self.rotate180 = QPushButton("Rotate 180")
        self.rotate180.setMinimumSize(QSize(130,40))
        self.rotate180.setStatusTip('Rotate Image 180 Clockwise')
        self.rotate180.clicked.connect(self.rotateImage180)
        
        self.flip_horizontal = QPushButton("Flip Horizontal")
        self.flip_horizontal.setMinimumSize(QSize(130,40))
        self.flip_horizontal.setStatusTip('Flip Image across Horizontal Axis')
        self.flip_horizontal.clicked.connect(self.flipImageHorizontal)

        self.flip_vertical = QPushButton("Flip Vertical")
        self.flip_vertical.setMinimumSize(QSize(130,40))
        self.flip_vertical.setStatusTip('Flip Image across Vertical Axis')
        self.flip_vertical.clicked.connect(self.flipImageVertical)
        
        self.resize_half = QPushButton("Resize Half")
        self.resize_half.setMinimumSize(QSize(130,40))
        self.resize_half.setStatusTip("Resize image to half the original size")
        self.resize_half.clicked.connect(self.resizeImageHalf)
        
        # Setup Vertical layout to contain all the button
        dock_v_box = QVBoxLayout()
        dock_v_box.addWidget(self.rotate90)
        dock_v_box.addWidget(self.rotate180)
        dock_v_box.addStretch(1)
        dock_v_box.addWidget(self.flip_horizontal)
        dock_v_box.addWidget(self.flip_vertical)
        dock_v_box.addStretch(1)
        dock_v_box.addWidget(self.resize_half)
        dock_v_box.addStretch(6)
        
        # Set the main layout for QWidget,tool_content and then set the layout
        # for the main dock widget
        self.tools_content.setLayout(dock_v_box)
        self.dock_tools_view.setWidget(self.tools_content)
        
        # Set initial location of dock widget
        self.addDockWidget(Qt.RightDockWidgetArea,self.dock_tools_view)
        
        # Handles the visibility of the dock widget
        self.toggle_dock_tools_act = self.dock_tools_view.toggleViewAction()
    
    def photoEditorWidgets(self):
        # Setup Instances of Widget for PhotoEditor GUI
        self.image = QPixmap()
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        # Use setSizePolicy() to specify how the widget can be resized
        # horizontally and vertically. Here, the image will stretch 
        # horizontally but not vertically.
        self.image_label.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Ignored)
        self.setCentralWidget(self.image_label)
        
    def openImage(self):
        # Open an image file and display its contents in label widget
        # Display error message if image can't opened.
        
        image_file, _ = QFileDialog.getOpenFileName(self,"Open Image","",
                        "JPG Files (*.jpeg *.jpg);;PNG Files (*.png);;BitMap Files (*.bmp)")
                        
        if image_file:
            self.image = QPixmap(image_file)
            self.image_label.setPixmap(self.image.scaled(self.image_label.size(),
                                       Qt.KeepAspectRatio,Qt.SmoothTransformation))

        else:
            QMessageBox.information(self,"Error","Unable to open image",QMessageBox.Ok)
        
        self.print_act.setEnabled(True)
            
    
    def saveImage(self):    
        # Saves the image, displays error if image can't be saved
        image_file, _ = QFileDialog.getSaveFileName(self,"Save Image","",
                        "JPG Files (*.jpeg *.jpg);;PNG Files (*.png);;BitMap Files (*.bmp)")
                    
        if image_file and self.image.isNull() == False:
            self.image.save(image_file)
        else:
            QMessageBox.information(self,"Error","Unable to save image",QMessageBox.Ok)
               
    
    def printImage(self):
        # Print the image
        # Create a printer object and print output defined by the platform the
        # program is being run on.
        # QPrinter.NativeFormat is the default.
        
        printer = QPrinter()
        printer.setOutputFormat(QPrinter.NativeFormat)
        
        # Create a printer dialog to configure printer
        print_dialog = QPrintDialog(printer)
        
        # If the dialog is accpeted by user begin printing
        if (print_dialog.exec_() == QPrintDialog.Accepted):
            # Use QPainter to output a pdf file
            painter = QPainter()
            # Begin Painting device
            painter.begin(printer)
            # Set QRect to hold the painter's current viewport which is the image label
            rect = QRect(paitner.viewport())
            # Get the size of the image_label and use it to set the size of the viewport
            size = QSize(self.image_label.pixmap().size())
            size.scale(rect.size(),Qt.KeepAspectRatio)
            painter.setViewport(rect.x(),rect.y(),size.width(),size.height())
            painter.setWindow(self.image_label.pixmap().rect())
            # Scale the image to fit the rect source (0,0)
            painter.drawPixmap(0,0,self.image_label.pixmap())
            # End Painting
            painter.end()
            
    def clearImage(self):
        # Clear's current image in QLabel Widget
        self.image_label.clear()
        self.image = QPixmap() # reset pixmap so that isNull() = True
    
    def rotateImage90(self):
        # Rotate Image 90 clockwise
        
        if self.image.isNull() == False:
            transform90 = QTransform().rotate(90)
            pixmap = QPixmap(self.image)
            
            rotated = pixmap.transformed(transform90,mode=Qt.SmoothTransformation)
            self.image_label.setPixmap(rotated.scaled(self.image_label.size(),Qt.KeepAspectRatio,
                                                      Qt.SmoothTransformation))
            self.image = QPixmap(rotated)
            self.image_label.repaint() # repaint the child widget
        else:
            pass # No image to rotate
    
    def rotateImage180(self):
        # Rotate Image 90 clockwise
        
        if self.image.isNull() == False:
            transform180 = QTransform().rotate(180)
            pixmap = QPixmap(self.image)
            
            rotated = pixmap.transformed(transform180,mode=Qt.SmoothTransformation)
            self.image_label.setPixmap(rotated.scaled(self.image_label.size(),Qt.KeepAspectRatio,
                                                      Qt.SmoothTransformation))
            self.image = QPixmap(rotated)
            self.image_label.repaint() # repaint the child widget
        else:
            pass # No image to rotate
    
    def flipImageHorizontal(self):
        # Mirror the image across horizontal axis
        
        if self.image.isNull() == False:
            flip_h = QTransform().scale(-1,1)
            pixmap = QPixmap(self.image)
            
            flipped = pixmap.transformed(flip_h)
            self.image_label.setPixmap(flipped.scaled(self.image_label.size(),Qt.KeepAspectRatio,
                                       Qt.SmoothTransformation))
            
            self.image = QPixmap(flipped)
            self.image_label.repaint()
        else:
            pass # No image to flip
            
    def flipImageVertical(self):
        # Mirror the image across vertical axis
        
        if self.image.isNull() == False:
            flip_v = QTransform().scale(1,-1)
            pixmap = QPixmap(self.image)
            
            flipped = pixmap.transformed(flip_v)
            self.image_label.setPixmap(flipped.scaled(self.image_label.size(),Qt.KeepAspectRatio,
                                       Qt.SmoothTransformation))
            
            self.image = QPixmap(flipped)
            self.image_label.repaint()
        else:
            pass # No image to flip
    
    def resizeImageHalf(self):
        # Resize the image to half its current size
        
        if self.image.isNull() == False:
            resize = QTransform().scale(0.5,0.5)
            pixmap = QPixmap(self.image)
            
            resized = pixmap.transformed(resize)
            
            self.image_label.setPixmap(resized.scaled(self.image_label.size(),Qt.KeepAspectRatio,
                                                      Qt.SmoothTransformation))
            
            self.image = QPixmap(resized)
            self.image_label.repaint()
        else:
            pass # No image to resize
        

        
def main():
    app = QApplication(sys.argv)
    window = PhotoEditor()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
    
    
        
        
        