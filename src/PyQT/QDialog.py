import sys
from PyQt5.QtWidgets import QApplication, QDialog

# application object
app = QApplication(sys.argv)  # QApplication([])
window = QDialog()
window.setWindowTitle("Main Window - QDialog")
window.show()
# Start the event loop.
app.exec_()
