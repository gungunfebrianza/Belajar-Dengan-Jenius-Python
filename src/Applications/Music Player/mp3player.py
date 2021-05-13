# Form implementation generated from reading ui file 'mp3player.ui'
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
        self.listWidget = QtWidgets.QListWidget(windowQWidget)
        self.btnAddFile = QtWidgets.QPushButton(windowQWidget)
        self.btnRemove = QtWidgets.QPushButton(windowQWidget)
        self.btnClearList = QtWidgets.QPushButton(windowQWidget)
        self.btnPlay = QtWidgets.QPushButton(windowQWidget)
        self.btnPause = QtWidgets.QPushButton(windowQWidget)
        self.btnStop = QtWidgets.QPushButton(windowQWidget)
        self.btnNext = QtWidgets.QPushButton(windowQWidget)
        self.btnPrev = QtWidgets.QPushButton(windowQWidget)
        self.labelPlayed = QtWidgets.QLabel(windowQWidget)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(650, 297)

        self.listWidget.setGeometry(QtCore.QRect(10, 10, 491, 192))
        self.listWidget.setObjectName("listWidget")

        self.btnAddFile.setGeometry(QtCore.QRect(510, 10, 131, 24))
        self.btnAddFile.setObjectName("btnAddFile")

        self.btnRemove.setGeometry(QtCore.QRect(510, 40, 131, 24))
        self.btnRemove.setObjectName("btnRemove")

        self.btnClearList.setGeometry(QtCore.QRect(510, 70, 131, 24))
        self.btnClearList.setObjectName("btnClearList")

        self.btnPlay.setGeometry(QtCore.QRect(10, 210, 91, 41))
        self.btnPlay.setObjectName("btnPlay")
        self.btnPlay.setIcon(QtGui.QIcon("Play.png"))

        self.btnPause.setGeometry(QtCore.QRect(110, 210, 91, 41))
        self.btnPause.setObjectName("btnPause")

        self.btnStop.setGeometry(QtCore.QRect(210, 210, 91, 41))
        self.btnStop.setObjectName("btnStop")

        self.btnNext.setGeometry(QtCore.QRect(310, 210, 91, 41))
        self.btnNext.setObjectName("btnNext")

        self.btnPrev.setGeometry(QtCore.QRect(410, 210, 91, 41))
        self.btnPrev.setObjectName("btnPrev")

        self.labelPlayed.setGeometry(QtCore.QRect(10, 270, 331, 16))
        self.labelPlayed.setObjectName("labelPlayed")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowIcon(QtGui.QIcon('Audio.ico'))
        Form.setWindowTitle(_translate("Form", "Mp3 Player"))
        self.btnAddFile.setText(_translate("Form", "Add New Music File"))
        self.btnRemove.setText(_translate("Form", "Remove Selected File"))
        self.btnClearList.setText(_translate("Form", "Clear List"))
        self.btnPlay.setText(_translate("Form", ""))
        self.btnPause.setText(_translate("Form", "Pause"))
        self.btnStop.setText(_translate("Form", "Stop"))
        self.btnNext.setText(_translate("Form", "Next"))
        self.btnPrev.setText(_translate("Form", "Prev"))
        self.labelPlayed.setText(_translate("Form", "Music Played : "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication([])
    windowQWidget = QWidget()
    gui = window()
    gui.setupUi(windowQWidget)
    windowQWidget.show()
    sys.exit(app.exec())