import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        layout = QGridLayout()
        self.setLayout(layout)
        # Add Button / QPushButton
        self.btn1 = QPushButton('Show Dialog', self)
        # Set Button Properties
        # self.btn1.move(20, 20)  # No Layout Mode
        self.btn1.clicked.connect(self.show_int_input_dialog)

        self.line1 = QLineEdit(self)
        # self.line1.move(130, 22)  # No Layout Mode
        layout.addWidget(self.btn1)
        layout.addWidget(self.line1)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Main Window - QListBox')

    def show_text_input_dialog(self):
        text, ok = QInputDialog.getText(self, 'input dialog', 'Input Your Name')
        if ok:
            self.line1.setText(str(text))

    def show_multi_line_input_dialog(self):
        text, ok = QInputDialog.getMultiLineText(self, 'getMultiLineText', 'Story', "Enter story")
        if ok and text:
            print(text)

    def show_item_input_dialog(self):
        items = ["Maudy", "Ayunda", "Gun Gun", "Febrianza"]
        item, ok = QInputDialog.getItem(self, 'getItem', 'Favourite Person', items, 0, False)

        if ok and item:
            print(item)

    def show_double_input_dialog(self):
        double, ok = QInputDialog.getDouble(self, 'getDouble', 'Enter double', 22.33, -10000, 10000, 2)
        if ok:
            print(double)

    def show_int_input_dialog(self):
        int, ok = QInputDialog.getInt(self, 'getInteger', 'Enter number', 25, 0, 100, 1)
        if ok:
            print(int)


app = QApplication(sys.argv)
window = Window()
window.show()
# Start the event loop.
sys.exit(app.exec_())  # Zero is considered “successful termination”
