from PyQt5.QtWidgets import QApplication, QPushButton


def submit():
    print("OK")


app = QApplication([])
app.setStyleSheet(
    "QPushButton {  background-color:yellow; font-size:24px  }"
)

button = QPushButton('Hello Qt5')

# Event Click
button.clicked.connect(submit)

button.show()
app.exec_()
