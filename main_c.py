import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor
from random import choice
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(575, 451)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(210, 180, 151, 27))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 575, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Нарисовать круги"))


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.flag = False
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Рисование')
        self.pushButton.clicked.connect(self.flag_change)

    def flag_change(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            self.drawFlag(qp)
            qp.end()
            self.flag = False

    def drawFlag(self, qp):
        for _ in range(4):
            r = choice(range(0, 255))
            g = choice(range(0, 255))
            b = choice(range(0, 255))
            qp.setBrush(QColor(r, g, b))
            x = choice(range(0, 575))
            y = choice(range(0, 451))
            rad = choice(range(1, 200))
            qp.drawEllipse(x, y, rad, rad)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
