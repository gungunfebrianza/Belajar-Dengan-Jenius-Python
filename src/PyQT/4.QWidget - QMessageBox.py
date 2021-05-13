import sys
from PyQt6.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
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

        # clicked signal
        self.btn1.clicked.connect(self.new_custom_button)

        layout.addWidget(self.btn1)

        # Add Custom Button
        self.btn2 = QPushButton()
        self.mbox2 = QMessageBox()
        self.btn2 = self.mbox2.addButton("Yeaah", QMessageBox.ButtonRole.AcceptRole)
        # https://doc.qt.io/qt-6/qmessagebox.html#ButtonRole-enum

        # self.mbox2.buttonClicked.connect(self.display_warning)  # buttonClicked Signal

    def display_warning(self):
        # Set MessageBox Properties
        self.mbox1.setWindowTitle("Message Box")
        self.mbox1.setText("Hello World, Maudy !")
        self.mbox1.setIcon(QMessageBox.Icon.Warning)  # https://doc.qt.io/qt-6/qmessagebox.html#Icon-enum
        self.mbox1.setDetailedText("Place for more details information.")
        self.mbox1.exec()

    def display_information(self):
        self.mbox1.setWindowTitle("Message Box")
        self.mbox1.setText("Hello World, Maudy !")
        self.mbox1.setIcon(QMessageBox.Icon.Information)  # https://doc.qt.io/qt-6/qmessagebox.html#Icon-enum
        self.mbox1.setStandardButtons(QMessageBox.StandardButtons.Yes |
                                      QMessageBox.StandardButtons.Close |
                                      QMessageBox.StandardButtons.Help)  # https://doc.qt.io/qt-6/qmessagebox.html#StandardButton-enum
        self.mbox1.setDefaultButton(QMessageBox.StandardButtons.Help)
        result = self.mbox1.exec()
        if result == QMessageBox.StandardButtons.Yes:
            print(result)

    def static_way(self):
        result = QMessageBox.information(self, "Title Here..", "Message here..",
                                         QMessageBox.StandardButtons.Help | QMessageBox.StandardButtons.No,
                                         QMessageBox.StandardButtons.Help)
        print(result)

    def new_custom_button(self):
        self.mbox2.setWindowTitle("Message Box")
        self.mbox2.setText("Hello World, Maudy !")
        self.mbox2.exec()


app = QApplication(sys.argv)  # QApplication([])
window = Window()
window.setWindowTitle("Main Window - QMessageBox")  # Window Title
window.resize(400, 400)  # Resize Window

window.show()
# Start the event loop.
sys.exit(app.exec())  # Zero is considered “successful termination”
