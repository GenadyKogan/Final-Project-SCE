





from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets, QtGui
import sys 
# window class 
class AboutW(QWidget):
     def __init__(self):
        super().__init__()

        self.initUI()
        
        self.labelA = QLabel('Times Font',self)

        self.labelA.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
        
        self.label_1 = QLabel('Left', self)
        self.label_1.setFont(QFont('Times', 10)) 
        self.label_1.move(10,10)
         
        self.label_1.setGeometry(10, 10, 100, 200)
       
     def initUI(self):
        # Cancel button 
        cancelButton = QPushButton("Cancel")
        # Clossing AboutWindow action

        cancelButton.clicked.connect(lambda:self.close())
        
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(600, 100, 400, 400)
        self.setWindowTitle('About')
       



# create pyqt5 app 
#App = QApplication(sys.argv) 

# create the instance of our Window 
#window = AboutW() 

# showing the wwindow 
#window.show() 

# start the app 
sys.exit(App.exec()) 
 
