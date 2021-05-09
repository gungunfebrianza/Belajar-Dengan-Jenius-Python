from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt


class window(object):
    def __init__(self):
        super().__init__()
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(windowQWidget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.tableWidget1 = QtWidgets.QTableWidget(windowQWidget)
        self.pushButton1 = QtWidgets.QPushButton(windowQWidget)
        self.mbox1 = QtWidgets.QMessageBox(windowQWidget)
        self.inputDialog1 = QtWidgets.QInputDialog()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(473, 487)

        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout.setObjectName("verticalLayout")

        self.tableWidget1.setObjectName("tableWidget1")
        self.tableWidget1.setColumnCount(4)
        self.tableWidget1.setRowCount(1)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setVerticalHeaderItem(0, item)

        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget1.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget1.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget1.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget1.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setItem(0, 3, item)
        self.verticalLayout.addWidget(self.tableWidget1)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)

        self.pushButton1.setFont(font)
        self.pushButton1.setObjectName("pushButton1")
        self.pushButton1.clicked.connect(self.get_item)

        self.verticalLayout_2.addWidget(self.pushButton1)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        #

    # Todo : Add UI to Insert New Row At Specific Index
    def event_add_row(self):
        self.tableWidget1.insertRow(1)

    # Todo : Add UI to Set Item At Specific Row
    def event_set_item(self):
        self.tableWidget1.setItem(0, 0, QtWidgets.QTableWidgetItem("0,0"))
        self.tableWidget1.setItem(0, 1, QtWidgets.QTableWidgetItem("0,1"))
        self.tableWidget1.setItem(0, 2, QtWidgets.QTableWidgetItem("0,2"))
        self.tableWidget1.setItem(0, 3, QtWidgets.QTableWidgetItem("0,3"))

    # Todo : Add UI To Remove At Specific Row
    def event_remove_row(self):
        self.tableWidget1.removeRow(0)  # Static Example, Use Parameter!

    def count_row(self):
        self.mbox1.setWindowTitle("Message Box")
        self.mbox1.setText("Total Rows : " + str(self.tableWidget1.rowCount()))
        self.mbox1.exec()

    # Todo : Add UI To Sort At Specific Column
    def sort_asc(self):
        self.tableWidget1.sortItems(0, Qt.AscendingOrder)

    # https://bugs.python.org/issue39423
    def get_item(self):
        text, ok = self.inputDialog1.getText(self, 'input dialog', 'Input Your Name')
        if ok:
            print(text)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Password Manager - QTableWidget"))
        item = self.tableWidget1.verticalHeaderItem(0)
        item.setText(_translate("Form", "1"))
        item = self.tableWidget1.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Account"))
        item = self.tableWidget1.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Username"))
        item = self.tableWidget1.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Password"))
        item = self.tableWidget1.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Description"))
        __sortingEnabled = self.tableWidget1.isSortingEnabled()
        self.tableWidget1.setSortingEnabled(False)
        item = self.tableWidget1.item(0, 0)
        item.setText(_translate("Form", "Coinmarketcap"))
        item = self.tableWidget1.item(0, 1)
        item.setText(_translate("Form", "febrianza@gmail.com"))
        item = self.tableWidget1.item(0, 2)
        item.setText(_translate("Form", "***************"))
        item = self.tableWidget1.item(0, 3)
        item.setText(_translate("Form", "For API Development Purpose"))
        self.tableWidget1.setSortingEnabled(__sortingEnabled)
        self.pushButton1.setText(_translate("Form", "Add Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    windowQWidget = QtWidgets.QWidget()
    gui = window()
    gui.setupUi(windowQWidget)
    windowQWidget.show()
    sys.exit(app.exec())
