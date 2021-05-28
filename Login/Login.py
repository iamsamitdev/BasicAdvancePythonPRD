from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Dashboard import Ui_DashboardWindows

class Ui_LoginWindow(object):

    def openDashbord(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_DashboardWindows()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(1123, 472)
        LoginWindow.setMinimumSize(QtCore.QSize(1123, 472))
        LoginWindow.setMaximumSize(QtCore.QSize(1123, 472))
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, -20, 541, 531))
        self.widget.setStyleSheet("background-color: rgb(85, 0, 255);")
        self.widget.setObjectName("widget")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(130, 190, 271, 91))
        self.label_3.setStyleSheet("font: 36pt \"Kanit\";\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(130, 280, 231, 41))
        self.label_4.setStyleSheet("font: 14pt \"Kanit\";\n"
"color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(731, 236, 281, 48))
        self.password.setStyleSheet("font: 14pt \"Kanit\";\n"
"padding: 5px;")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.btnLogin = QtWidgets.QPushButton(self.centralwidget)
        self.btnLogin.setGeometry(QtCore.QRect(730, 300, 121, 51))
        self.btnLogin.setStyleSheet("font: 14pt \"Kanit\";\n"
"background-color: rgb(0, 85, 255);\n"
"color: rgb(255, 255, 255);")
        self.btnLogin.setObjectName("btnLogin")

        # กำหนด Event Clicked ให้กับปุ่ม  Login
        self.btnLogin.clicked.connect(self.checkLogin)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(610, 180, 103, 34))
        self.label.setStyleSheet("font: 14pt \"Kanit\";")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.username = QtWidgets.QLineEdit(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(730, 170, 281, 48))
        self.username.setStyleSheet("font: 14pt \"Kanit\";\n"
"padding: 5px;")
        self.username.setObjectName("username")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(630, 240, 85, 34))
        self.label_2.setStyleSheet("font: 14pt \"Kanit\";")
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        LoginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def checkLogin(self):
        # รับค่า username และ password
        get_username = self.username.text()
        get_password = self.password.text()

        if get_username == 'admin' and get_password == '1234':
            # print('Login Success')
            LoginWindow.hide()  # ซ่อนหน้า Login
            self.openDashbord()  # เปิดหน้า Dashboard
        else:
            # print('Login Fail!')
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Login fail")
            msg.setInformativeText('Please try again')
            msg.setWindowTitle("Error")
            msg.exec_()

    # สร้างฟังก์ชันสำหรับเรียกเปิดหน้า dashboard

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Login"))
        self.label_3.setText(_translate("LoginWindow", "เข้าสู่ระบบ"))
        self.label_4.setText(_translate("LoginWindow", "ทดสอบด้านฝีมือแรงงาน"))
        self.btnLogin.setText(_translate("LoginWindow", "Login"))
        self.label.setText(_translate("LoginWindow", "Username"))
        self.label_2.setText(_translate("LoginWindow", "Pasword"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())
