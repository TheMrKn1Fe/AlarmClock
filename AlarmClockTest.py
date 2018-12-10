import sys
from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLCDNumber, QMessageBox
from PyQt5.QtCore import QTimer, QTime
from DigitalClock import DigitalClock


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('AlarmClock.ui', self)
        self.DigitalClock = DigitalClock(self.centralwidget)
        self.DigitalClock.setGeometry(QtCore.QRect(315, 18, 182, 80))

    def initUI(self):

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Message box')
        self.show()

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Выход',
                                     "Вы уверены что хотите выйти?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())