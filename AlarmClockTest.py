import sys
from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLCDNumber, QMessageBox, QTimeEdit
from PyQt5.QtCore import QTimer, QTime
from DigitalClock import DigitalClock


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('AlarmClock.ui', self)
        self.DigitalClock = DigitalClock(self.centralwidget)
        self.DigitalClock.setGeometry(QtCore.QRect(375, 20, 170, 80))
        self.pushButton.clicked.connect(self.add)

    def initUI(self):

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Message box')
        self.show()

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Выход',
                                     "Вы уверены что хотите выйти? Будильники перестанут работать", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def add(self):
        name = self.lineEdit.text()
        time = self.timeEdit.time().toString('hh:mm')
        if self.spinBox.text() == '1':
            self.label_7.setText(name)
            self.label_18.setText(time)
        elif self.spinBox.text() == '2':
            self.label_14.setText(name)
            self.label_19.setText(time)
        elif self.spinBox.text() == '3':
            self.label_15.setText(name)
            self.label_20.setText(time)
        elif self.spinBox.text() == '4':
            self.label_16.setText(name)
            self.label_21.setText(time)
        elif self.spinBox.text() == '5':
            self.label_17.setText(name)
            self.label_22.setText(time)

app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())