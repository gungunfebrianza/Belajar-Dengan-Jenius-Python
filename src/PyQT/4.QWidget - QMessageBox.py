import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtWidgets


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        # Add MessageBox / QMessageBox
        self.mbox1 = QMessageBox()

        # Add Button / QPushButton
        self.btn1 = QPushButton()
        # self.btn1 = QtWidgets.QPushButton(self)
        # Set Button Properties
        self.btn1.setText("Click Here")
        # self.btn1.setGeometry(QtCore.QRect(170, 50, 75, 23))
        self.btn1.clicked.connect(self.display_message)
        layout.addWidget(self.btn1)

    def display_message(self):
        # Set MessageBox Properties
        self.mbox1.setWindowTitle("Message Box")
        self.mbox1.setText("Hello World, Maudy !")
        self.mbox1.setDetailedText("Place for more details information.")
        self.mbox1.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        return_value = self.mbox1.exec()
        if return_value == QMessageBox.Ok:
            print('OK clicked')


app = QApplication(sys.argv)  # QApplication([])
window = Window()
window.setWindowTitle("Main Window - QMessageBox")  # Window Title
window.resize(400, 400)  # Resize Window

window.show()
# Start the event loop.
sys.exit(app.exec_())  # Zero is considered “successful termination”
