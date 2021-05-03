import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox


def displaymessage():
    # Add MessageBox / QMessageBox
    mbox1 = QMessageBox()
    # Set MessageBox Properties
    mbox1.setWindowTitle("Message Box")
    mbox1.setText("Hello World, Maudy !")
    mbox1.setDetailedText("Place for more details information.")
    mbox1.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    mbox1.exec()


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Main Window - QMessageBox")  # Window Title
window.resize(400, 400)  # Resize Window

# Add Button / QPushButton
btn1 = QPushButton(window)
# Set Button Properties
btn1.setText("Click Here")
btn1.move(100, 40)
btn1.clicked.connect(displaymessage)

window.show()
sys.exit(app.exec_())
