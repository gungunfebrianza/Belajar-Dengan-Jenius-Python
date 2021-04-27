from PyQt5.QtWidgets import QApplication, QWidget
import sys
from PyQt5.QtGui import QIcon


class WindowExample(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 400, 300)
        self.setWindowTitle("Form 1")
        self.setWindowIcon(QIcon('python.png'))

        # self.setFixedHeight(400)
        # self.setFixedWidth(300)

        # self.setWindowOpacity(0.5)
        self.setStyleSheet('background-color:green')

        self.show()


app = QApplication(sys.argv)
window = WindowExample()
sys.exit(app.exec_())  # Zero is considered “successful termination”

