# Form implementation generated from reading ui file 'DesignerQLineEdit.ui'
#
# Created by: PyQt6 UI code generator 6.0.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget


class window(QWidget):
    def __init__(self):
        super().__init__()
        self.lineEdit1 = QtWidgets.QLineEdit(windowQWidget)
        self.lineEdit2 = QtWidgets.QLineEdit(windowQWidget)
        self.widget = QtWidgets.QWidget(windowQWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.pushButtonSelectAll = QtWidgets.QPushButton(self.widget)
        self.pushButtonCopy = QtWidgets.QPushButton(self.widget)
        self.pushButtonUndo = QtWidgets.QPushButton(self.widget)
        self.pushButtonCut = QtWidgets.QPushButton(self.widget)
        self.pushButtonPaste = QtWidgets.QPushButton(self.widget)
        self.pushButtonRedo = QtWidgets.QPushButton(self.widget)
        self.pushButtonDeselect = QtWidgets.QPushButton(self.widget)
        self.widget1 = QtWidgets.QWidget(windowQWidget)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget1)
        self.pushButtonSetText = QtWidgets.QPushButton(self.widget1)
        self.pushButtonRead = QtWidgets.QPushButton(self.widget1)
        self.pushButtonReadPlaceHolder = QtWidgets.QPushButton(self.widget1)
        self.pushButtonReadSelectedText = QtWidgets.QPushButton(self.widget1)
        self.widget2 = QtWidgets.QWidget(windowQWidget)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget2)
        self.pushButtonSetMaxLen = QtWidgets.QPushButton(self.widget2)
        self.lineEditMaxLen = QtWidgets.QLineEdit(self.widget2)
        self.pushButtonSetInputMask = QtWidgets.QPushButton(self.widget2)
        self.lineEditInputMask = QtWidgets.QLineEdit(self.widget2)
        self.widget3 = QtWidgets.QWidget(windowQWidget)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget3)
        self.pushButtonSetAlign = QtWidgets.QPushButton(self.widget3)
        self.comboBox1 = QtWidgets.QComboBox(self.widget3)
        self.pushButtonSetEcho = QtWidgets.QPushButton(self.widget3)
        self.comboBox2 = QtWidgets.QComboBox(self.widget3)
        self.widget4 = QtWidgets.QWidget(windowQWidget)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget4)
        self.pushButtonSetReadOnly = QtWidgets.QPushButton(self.widget4)
        self.comboBox3 = QtWidgets.QComboBox(self.widget4)
        self.pushButtonSetCursor = QtWidgets.QPushButton(self.widget4)
        self.lineEditSetCursor = QtWidgets.QLineEdit(self.widget4)

        self.labelCursorPosition = QtWidgets.QLabel(windowQWidget)
        self.labelSelectionStart = QtWidgets.QLabel(windowQWidget)
        self.labelSelectedLen = QtWidgets.QLabel(windowQWidget)
        self.labelSelectionEnd = QtWidgets.QLabel(windowQWidget)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(661, 369)

        self.lineEdit1.setGeometry(QtCore.QRect(10, 10, 641, 121))
        self.lineEdit1.setObjectName("lineEdit1")

        self.lineEdit2.setGeometry(QtCore.QRect(10, 170, 641, 41))
        self.lineEdit2.setObjectName("lineEdit2")

        self.widget.setGeometry(QtCore.QRect(11, 140, 563, 26))
        self.widget.setObjectName("widget")

        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.pushButtonSelectAll.setObjectName("pushButtonSelectAll")
        self.horizontalLayout.addWidget(self.pushButtonSelectAll)

        self.pushButtonCopy.setObjectName("pushButtonCopy")
        self.horizontalLayout.addWidget(self.pushButtonCopy)

        self.pushButtonCut.setObjectName("pushButtonCut")
        self.horizontalLayout.addWidget(self.pushButtonCut)

        self.pushButtonPaste.setObjectName("pushButtonPaste")
        self.horizontalLayout.addWidget(self.pushButtonPaste)

        self.pushButtonUndo.setObjectName("pushButtonUndo")
        self.horizontalLayout.addWidget(self.pushButtonUndo)

        self.pushButtonRedo.setObjectName("pushButtonRedo")
        self.horizontalLayout.addWidget(self.pushButtonRedo)

        self.pushButtonDeselect.setObjectName("pushButtonDeselect")
        self.horizontalLayout.addWidget(self.pushButtonDeselect)

        self.widget1.setGeometry(QtCore.QRect(10, 220, 445, 26))
        self.widget1.setObjectName("widget1")

        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.pushButtonSetText.setObjectName("pushButtonSetText")
        self.horizontalLayout_3.addWidget(self.pushButtonSetText)

        self.pushButtonRead.setObjectName("pushButtonRead")
        self.horizontalLayout_3.addWidget(self.pushButtonRead)

        self.pushButtonReadPlaceHolder.setObjectName("pushButtonReadPlaceHolder")
        self.horizontalLayout_3.addWidget(self.pushButtonReadPlaceHolder)

        self.pushButtonReadSelectedText.setObjectName("pushButtonReadSelectedText")
        self.horizontalLayout_3.addWidget(self.pushButtonReadSelectedText)

        self.widget2.setGeometry(QtCore.QRect(10, 250, 608, 26))
        self.widget2.setObjectName("widget2")

        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.pushButtonSetMaxLen.setObjectName("pushButtonSetMaxLen")
        self.horizontalLayout_4.addWidget(self.pushButtonSetMaxLen)

        self.lineEditMaxLen.setObjectName("lineEditMaxLen")
        self.horizontalLayout_4.addWidget(self.lineEditMaxLen)

        self.pushButtonSetInputMask.setObjectName("pushButtonSetInputMask")
        self.horizontalLayout_4.addWidget(self.pushButtonSetInputMask)

        self.lineEditInputMask.setObjectName("lineEditInputMask")
        self.horizontalLayout_4.addWidget(self.lineEditInputMask)

        self.widget3.setGeometry(QtCore.QRect(10, 280, 486, 26))
        self.widget3.setObjectName("widget3")

        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")

        self.pushButtonSetAlign.setObjectName("pushButtonSetAlign")
        self.horizontalLayout_5.addWidget(self.pushButtonSetAlign)

        self.comboBox1.setObjectName("comboBox1")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.horizontalLayout_5.addWidget(self.comboBox1)

        self.pushButtonSetEcho.setObjectName("pushButtonSetEcho")
        self.horizontalLayout_5.addWidget(self.pushButtonSetEcho)

        self.comboBox2.setObjectName("comboBox2")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.horizontalLayout_5.addWidget(self.comboBox2)

        self.widget4.setGeometry(QtCore.QRect(10, 310, 464, 26))
        self.widget4.setObjectName("widget4")

        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")

        self.pushButtonSetReadOnly.setObjectName("pushButtonSetReadOnly")
        self.horizontalLayout_6.addWidget(self.pushButtonSetReadOnly)

        self.comboBox3.setObjectName("comboBox3")
        self.comboBox3.addItem("")
        self.comboBox3.addItem("")
        self.horizontalLayout_6.addWidget(self.comboBox3)

        self.pushButtonSetCursor.setObjectName("pushButtonSetCursor")
        self.horizontalLayout_6.addWidget(self.pushButtonSetCursor)

        self.lineEditSetCursor.setObjectName("lineEditSetCursor")
        self.horizontalLayout_6.addWidget(self.lineEditSetCursor)

        self.labelCursorPosition.setObjectName("labelCursorPosition")
        self.labelCursorPosition.setGeometry(QtCore.QRect(11, 341, 121, 16))

        self.labelSelectionStart.setObjectName("labelSelectionStart")
        self.labelSelectionStart.setGeometry(QtCore.QRect(180, 340, 121, 16))

        self.labelSelectedLen.setObjectName("labelSelectedLen")
        self.labelSelectedLen.setGeometry(QtCore.QRect(330, 340, 118, 16))

        self.labelSelectionEnd.setObjectName("labelSelectionEnd")
        self.labelSelectionEnd.setGeometry(QtCore.QRect(460, 340, 118, 16))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButtonSelectAll.clicked.connect(self.select_all())
        self.lineEdit1.cursorPositionChanged.connect(self.read_cursor_position)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "QWidget - QLineEdit"))
        self.pushButtonSelectAll.setText(_translate("Form", "Select All"))
        self.pushButtonCopy.setText(_translate("Form", "Copy"))
        self.pushButtonCut.setText(_translate("Form", "Cut"))
        self.pushButtonPaste.setText(_translate("Form", "Paste"))
        self.pushButtonUndo.setText(_translate("Form", "Undo"))
        self.pushButtonRedo.setText(_translate("Form", "Redo"))
        self.pushButtonDeselect.setText(_translate("Form", "Deselect"))
        self.pushButtonSetText.setText(_translate("Form", "Change Line Edit 1"))
        self.pushButtonRead.setText(_translate("Form", "Read Line Edit 1"))
        self.pushButtonReadPlaceHolder.setText(_translate("Form", "Read Placeholder Text"))
        self.pushButtonReadSelectedText.setText(_translate("Form", "Read Selected Text"))
        self.pushButtonSetMaxLen.setText(_translate("Form", "Set Maximum Length Line Edit 1"))
        self.pushButtonSetInputMask.setText(_translate("Form", "Set Input Mask Line Edit 1"))
        self.pushButtonSetAlign.setText(_translate("Form", "Set Align Line Edit 1"))
        self.comboBox1.setItemText(0, _translate("Form", "Center"))
        self.comboBox1.setItemText(1, _translate("Form", "Right"))
        self.comboBox1.setItemText(2, _translate("Form", "Left"))
        self.comboBox1.setItemText(3, _translate("Form", "Justify"))
        self.pushButtonSetEcho.setText(_translate("Form", "Set Echo Mode Line Edit 1"))
        self.comboBox2.setItemText(0, _translate("Form", "Password Mode"))
        self.comboBox2.setItemText(1, _translate("Form", "Password Echo On Edit"))
        self.comboBox2.setItemText(2, _translate("Form", "No Echo Mode"))
        self.comboBox2.setItemText(3, _translate("Form", "Normal Mode"))
        self.pushButtonSetReadOnly.setText(_translate("Form", "Set Read Only Line Edit 1"))
        self.comboBox3.setItemText(0, _translate("Form", "True"))
        self.comboBox3.setItemText(1, _translate("Form", "False"))
        self.pushButtonSetCursor.setText(_translate("Form", "Jump Cursor Position"))
        self.labelCursorPosition.setText(_translate("Form", "Cursor Position"))
        self.labelSelectionStart.setText(_translate("Form", "Selection Start At"))
        self.labelSelectedLen.setText(_translate("Form", "Selected Length"))
        self.labelSelectionEnd.setText(_translate("Form", "Selection End At"))

    def select_all(self):
        self.lineEdit1.selectAll()

    def read_cursor_position(self):
        self.labelCursorPosition.setText("Cursor Position : " + str(self.lineEdit1.cursorPosition()))
        if self.lineEdit1.hasSelectedText():
            self.labelSelectionStart.setText("Selection Start At : " + str(self.lineEdit1.selectionStart()))
            self.labelSelectedLen.setText("Selection Length : " + str(self.lineEdit1.selectionLength()))
            self.labelSelectionEnd.setText("Selection End At : " + str(self.lineEdit1.selectionEnd()))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication([])
    windowQWidget = QWidget()
    gui = window()
    gui.setupUi(windowQWidget)
    windowQWidget.show()
    sys.exit(app.exec())
