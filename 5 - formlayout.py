from email.charset import QP
from msilib.schema import RadioButton
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

app =QApplication(sys.argv)

window = QWidget()

label1 = QLabel("First Name")
label2 = QLabel("Last Name")
label3 = QLabel("Extra")
label4 = QLabel("Choose catergory")

input1 = QLineEdit()
input2 = QLineEdit()
input3_1 = QLineEdit()
input3_2 = QLineEdit()

inputBox = QVBoxLayout()
inputBox.addWidget(input3_1)
inputBox.addWidget(input3_2)

categoryBox = QHBoxLayout()
categoryBox.addWidget(QRadioButton("Category 1"))
categoryBox.addWidget(QRadioButton("Category 2"))
categoryBox.addStretch()

formLayout = QFormLayout()
formLayout.addRow(label1,input1)
formLayout.addRow(label2,input2)
formLayout.addRow(label3,inputBox)
formLayout.addRow(label4,categoryBox)
formLayout.addRow(QPushButton("Submit"))


window.setLayout(formLayout)

window.show()

sys.exit(app.exec_())