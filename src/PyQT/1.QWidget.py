import sys
from PyQt6.QtWidgets import QApplication, QWidget

# application object
app = QApplication(sys.argv)  # QApplication([])
window = QWidget()
window.setWindowTitle("Main Window - QWindow")
window.show()
# Start the event loop.
sys.exit(app.exec())  # Zero is considered “successful termination”
