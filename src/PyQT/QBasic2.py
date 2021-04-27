import sys
from PyQt5.QtWidgets import QApplication, QWidget

# application object
app = QApplication(sys.argv)  # QApplication([])

window = QWidget()

window.show()

# Start the event loop.
app.exec_()