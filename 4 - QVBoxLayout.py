import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

app = QApplication(sys.argv)

wid = QWidget()

lay = QVBoxLayout()

btn1 = QPushButton("first")
btn2 = QPushButton("second")

lay.addStretch()
lay.addWidget(btn1)
lay.addStretch()
lay.addWidget(btn2)
lay.addStretch()

wid.setLayout(lay)
wid.show()

sys.exit(app.exec_())


