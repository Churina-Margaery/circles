import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtGui import QPainter, QColor
from random import choice
from PyQt5 import uic


class MainForm(QMainWindow):
    def __init__(self, circle):
        super().__init__()
        self.circle = circle
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 575, 451)
        self.setWindowTitle('Круги')
        self.btn = QPushButton('Рисовать круги', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(200, 200)
        self.btn.clicked.connect(lambda: self.circle.initUI)


class Circle(QMainWindow):
    def __init__(self):
        super().__init__()
        self.flag = False
        self.initUI()

    def initUI(self):
        self.flag_change()

    def flag_change(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
            self.flag = False

    def draw_flag(self, qp):
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
    drawing = Circle()
    ex = MainForm(drawing)
    ex.show()
    sys.exit(app.exec_())
