from PyQt5.QtWidgets import *
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        title = "Tile of window"
        self.setWindowTitle(title)
        self.setGeometry(800, 400, 500, 300)
        self.show()


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
