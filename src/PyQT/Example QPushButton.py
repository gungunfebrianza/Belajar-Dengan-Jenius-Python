from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
import sys
from PyQt5.QtGui import QIcon


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 400, 300)
        self.setWindowTitle("Button")
        self.setWindowIcon(QIcon('python.png'))

        btn1 = QPushButton("Click Me", self)
        # btn1.setText("Our Second Text")
        # btn1.move(200,200)
        btn1.setGeometry(100, 100, 100, 100)
        btn1.setIcon(QIcon("cpp.png"))
        btn1.setStyleSheet('color:red')
        btn1.setStyleSheet('background-color:green')

        btn2 = QPushButton("Click Two", self)
        btn2.setGeometry(200, 100, 100, 100)
        btn2.setIcon(QIcon("pythonicon.png"))
        btn2.setStyleSheet('color:yellow')
        btn2.setStyleSheet('background-color:purple')


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
