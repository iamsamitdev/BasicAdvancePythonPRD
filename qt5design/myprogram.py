# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myprogram.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MyProgram(object):
    def setupUi(self, MyProgram):
        MyProgram.setObjectName("MyProgram")
        MyProgram.resize(566, 323)
        self.centralwidget = QtWidgets.QWidget(MyProgram)
        self.centralwidget.setObjectName("centralwidget")
        self.btn1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn1.setGeometry(QtCore.QRect(41, 69, 93, 41))
        self.btn1.setObjectName("btn1")
        self.btn2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn2.setGeometry(QtCore.QRect(40, 140, 93, 41))
        self.btn2.setObjectName("btn2")
        self.dial = QtWidgets.QDial(self.centralwidget)
        self.dial.setGeometry(QtCore.QRect(170, 60, 181, 121))
        self.dial.setObjectName("dial")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(370, 80, 151, 101))
        self.lcdNumber.setObjectName("lcdNumber")
        MyProgram.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MyProgram)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 566, 26))
        self.menubar.setObjectName("menubar")
        MyProgram.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MyProgram)
        self.statusbar.setObjectName("statusbar")
        MyProgram.setStatusBar(self.statusbar)

        self.retranslateUi(MyProgram)
        self.btn1.clicked.connect(self.dial.show)
        self.btn2.clicked.connect(self.dial.hide)
        self.dial.valueChanged['int'].connect(self.lcdNumber.display)
        QtCore.QMetaObject.connectSlotsByName(MyProgram)

    def retranslateUi(self, MyProgram):
        _translate = QtCore.QCoreApplication.translate
        MyProgram.setWindowTitle(_translate("MyProgram", "โปรแกรมแรก"))
        self.btn1.setText(_translate("MyProgram", "Show"))
        self.btn2.setText(_translate("MyProgram", "Hide"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MyProgram = QtWidgets.QMainWindow()
    ui = Ui_MyProgram()
    ui.setupUi(MyProgram)
    MyProgram.show()
    sys.exit(app.exec_())
