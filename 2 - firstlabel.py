import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

app = QApplication(sys.argv)

w = QWidget()
w.setWindowTitle("Simple as that")
w.setGeometry(700,400,500, 400)

b = QLabel(w)
b.setText("This is it")
b.move(100,100)

w.show()

sys.exit(app.exec_())