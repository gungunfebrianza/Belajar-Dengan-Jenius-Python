import sys
from PyQt5.QtWidgets import *


def list1clicked():
    QMessageBox.information(window, "MessageBox", "List Item Clicked")


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Main Window - QListBox")  # Window Title
window.resize(400, 400)  # Resize Window

# Add Listbox / QListBox
listbox1 = QListWidget(window)

# Set List Properties
listbox1.resize(390, 390)
listbox1.addItem("Maudy Ayunda")
listbox1.addItem("Gun Gun Febrianza")
listbox1.itemClicked.connect(list1clicked)

window.show()
sys.exit(app.exec_())
