from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
import sys
from PyQt5.QtGui import QIcon


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 400, 300)
        self.setWindowTitle("QPushButton")
        self.setWindowIcon(QIcon('python.png'))

        self.create_buttons()

        # self.show()

    def create_buttons(self):
        btn1 = QPushButton("Click Me", self)
        # btn1.setText("Our Second Text")
        # btn1.move(200,200)
        btn1.setGeometry(100, 100, 100, 100)
        btn1.setIcon(QIcon("cpp.png"))
        btn1.setStyleSheet('color:red')
        btn1.setStyleSheet('background-color:green')
        btn1.clicked.connect(self.clicked_btn)

        btn2 = QPushButton("Click Two", self)
        btn2.setGeometry(200, 100, 100, 100)
        btn2.setIcon(QIcon("pythonicon.png"))
        btn2.setStyleSheet('color:yellow')
        btn2.setStyleSheet('background-color:purple')
        btn2.clicked.connect(self.second_clicked)

    def clicked_btn(self):
        print("Button One Clicked")

    def second_clicked(self):
        print("Second Button Clicked")


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())