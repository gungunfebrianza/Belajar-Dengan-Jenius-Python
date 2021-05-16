# Form implementation generated from reading ui file 'DatabaseDisplayTable.ui'
#
# Created by: PyQt6 UI code generator 6.0.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

import mysql.connector as mc
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget, QApplication, QTableWidgetItem


class window(QWidget):
    def __init__(self):
        super().__init__()
        self.widget = QtWidgets.QWidget(windowQWidget)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.btnAuth = QtWidgets.QPushButton(self.widget)
        self.lineEdit1 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit2 = QtWidgets.QLineEdit(self.widget)
        self.tableWidget1 = QtWidgets.QTableWidget(self.widget)
        self.btnShowData = QtWidgets.QPushButton(self.widget)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(745, 415)

        self.widget.setGeometry(QtCore.QRect(10, 10, 721, 391))

        self.widget.setObjectName("widget")
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnAuth.setObjectName("btnAuth")
        self.lineEdit1.setObjectName("lineEdit1")
        self.lineEdit2.setObjectName("lineEdit2")
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget1.setObjectName("tableWidget1")
        self.btnShowData.setObjectName("btnShowData")

        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.btnAuth.setMaximumSize(QtCore.QSize(137, 16777215))

        self.horizontalLayout.addWidget(self.btnAuth)
        self.horizontalLayout.addWidget(self.lineEdit1)
        self.horizontalLayout.addWidget(self.lineEdit2)

        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.tableWidget1)
        self.verticalLayout.addWidget(self.btnShowData)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.btnShowData.clicked.connect(self.select_data)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Display Data MySQL"))
        self.btnAuth.setText(_translate("Form", "Set Database Credentials"))
        self.lineEdit1.setPlaceholderText(_translate("Form", "Database Name Here.."))
        self.lineEdit2.setPlaceholderText(_translate("Form", "Table Name here.."))
        self.btnShowData.setText(_translate("Form", "Show Data"))

    def select_data(self):
        try:
            database_name = self.lineEdit1.text()
            table_name = self.lineEdit2.text()

            my_database = mc.connect(
                host="localhost",
                user="root",
                passwd="",
                database=database_name,
            )

            print(database_name + " " + table_name)
            print("SELECT * FROM {}".format(table_name))

            my_cursor = my_database.cursor()
            my_cursor.execute("SELECT * FROM {}".format(table_name))
            result = my_cursor.fetchall()
            self.tableWidget1.setRowCount(len(result))
            self.tableWidget1.setColumnCount(len(result[0]))

            for row_number, row_data in enumerate(result):
                self.tableWidget1.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tableWidget1.setItem(row_number, column_number, QTableWidgetItem(str(data)))
            self.tableWidget1.setHorizontalHeaderItem(0, QTableWidgetItem("Name"))
            self.tableWidget1.setHorizontalHeaderItem(1, QTableWidgetItem("Email"))
            self.tableWidget1.setHorizontalHeaderItem(2, QTableWidgetItem("Age"))
            self.tableWidget1.setHorizontalHeaderItem(3, QTableWidgetItem("User ID"))

        except mc.Error as e:
            print("Error")


if __name__ == "__main__":
    import sys
    app = QApplication([])
    windowQWidget = QWidget()
    gui = window()
    gui.setupUi(windowQWidget)
    windowQWidget.show()
    sys.exit(app.exec())