import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 400, 300)
        self.setWindowTitle("Form 1")
        self.setWindowIcon(QIcon('python.png'))
        self.setStyleSheet('background-color:green')
        self.show()


app = QApplication(sys.argv)  # QApplication([])
window = Window()
window.show()
# Start the event loop.
sys.exit(app.exec_())  # Zero is considered “successful termination”

