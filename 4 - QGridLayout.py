import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

app = QApplication(sys.argv)

win = QWidget()

grid = QGridLayout()

btn1 = QPushButton("btn1")
btn2 = QPushButton("btn2")
btn3 = QPushButton("btn3")
btn4 = QPushButton("btn4")

grid.addWidget(btn1, 1,1)
grid.addWidget(btn2, 1,2)
grid.addWidget(btn3, 3,1)
grid.addWidget(btn4, 2,2)

win.setLayout(grid)
win.show()

sys.exit(app.exec_())