import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox


def displaymessage():
    # Add MessageBox / QMessageBox
    mbox1 = QMessageBox()
    # Set Properties
    mbox1.setWindowTitle("Message Box")
    mbox1.setText("Hello World, Maudy !")
    mbox1.setDetailedText("Place for more details information.")
    mbox1.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    mbox1.exec_()


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Main Window - QMessageBox")
window.resize(400, 400)  # Resize Window

# Add Button / QPushButton
btn1 = QPushButton(window)
# Set Properties
btn1.setText("Click Here")
btn1.move(100, 40)
btn1.clicked.connect(displaymessage)

window.show()
sys.exit(app.exec_())
