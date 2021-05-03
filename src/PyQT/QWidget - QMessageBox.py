import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox


def display_message():
    # Add MessageBox / QMessageBox
    mbox1 = QMessageBox()
    # Set MessageBox Properties
    mbox1.setWindowTitle("Message Box")
    mbox1.setText("Hello World, Maudy !")
    mbox1.setDetailedText("Place for more details information.")
    mbox1.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    return_value = mbox1.exec()
    if return_value == QMessageBox.Ok:
        print('OK clicked')


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Main Window - QMessageBox")  # Window Title
window.resize(400, 400)  # Resize Window

# Add Button / QPushButton
btn1 = QPushButton(window)
# Set Button Properties
btn1.setText("Click Here")
btn1.move(100, 40)
btn1.clicked.connect(display_message)

window.show()
# Start the event loop.
sys.exit(app.exec_())  # Zero is considered “successful termination”
