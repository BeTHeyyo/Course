from multiprocessing import current_process
from PyQt5.QtCore import QTime, QDate, QDateTime, Qt 

current_day = QDate.currentDate()

print(current_day)

print(current_day.toString())

print(current_day.toString(Qt.ISODate))

print(current_day.toString(Qt.DefaultLocaleLongDate))

current_time = QTime.currentTime()

print(current_time)

current_datetime = QDateTime.currentDateTime()

print(current_datetime)

print(QDate.currentDate().daysInMonth())