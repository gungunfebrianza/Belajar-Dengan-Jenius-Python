import sys
from PyQt6.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        # Add ListBox / QListBox
        self.listbox1 = QListWidget()
        # Add MessageBox / QMessageBox
        self.mbox1 = QMessageBox()
        self.listbox1.insertItem(0, "Maudy")
        self.listbox1.insertItem(1, "Ayunda")
        self.listbox1.insertItem(2, "Gun Gun")
        self.listbox1.insertItem(3, "Febrianza")
        self.listbox1.clicked.connect(self.event_listbox1_clicked)
        layout.addWidget(self.listbox1)

    def event_listbox1_clicked(self):
        item = self.listbox1.currentItem()
        print(item.text())
        self.display_message("MessageBox", "Item : " + item.text())

    def display_message(self, title, text):
        self.mbox1.setWindowTitle(title)
        self.mbox1.setText(text)
        self.mbox1.setDetailedText("Place for more details information.")
        self.mbox1.exec()
        # QMessageBox.information(self, title, text)


app = QApplication(sys.argv)  # QApplication([])
window = Window()
window.setWindowTitle("Main Window - QListBox")  # Window Title
window.resize(400, 400)  # Resize Window
window.show()
# Start the event loop.
sys.exit(app.exec())  # Zero is considered “successful termination”
