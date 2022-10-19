import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

def btn1Clicked():
    print("click1")

def btn2Clicked():
    print("click2")

app = QApplication(sys.argv)

w = QDialog()

btn1 = QPushButton("Push", w)

btn2 = QPushButton("asdf", w)
btn2.move(10,50)

btn1.clicked.connect(btn1Clicked)
btn2.clicked.connect(btn2Clicked)

w.setGeometry(700,400,500,400)

w.show()



sys.exit(app.exec_())