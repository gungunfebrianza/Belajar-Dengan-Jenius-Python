import sys
from PyQt5.QtWidgets import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Form")
        self.resize(400, 400)

        self.btn = QPushButton("Show Message", self)
        self.btn.move(40,40)
        self.btn.clicked.connect(self.evt_btn_clicked)

    def evt_btn_clicked(self):
        res = QMessageBox.question(self, "Hello", "Hello, World Gun !")
        print(res)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgmain = DlgMain()
    dlgmain.show()
    sys.exit(app.exec())


