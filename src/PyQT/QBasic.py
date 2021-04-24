import sys
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Form")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgmain = DlgMain()
    dlgmain.show()
    sys.exit(app.exec())


