import sys
from PyQt5.QtWidgets import QApplication, QWidget

# application object
app = QApplication(sys.argv)  # QApplication([])
window = QWidget()
window.setWindowTitle("Main Window - QWindow")
window.show()
# Start the event loop.
app.exec_()