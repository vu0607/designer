import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt5.QtGui import QPixmap
from designer import Ui_MainWindow
class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        self.addimage()
    def show(self):
        self.main_win.show()
    def addimage(self):
        qpixmap = QPixmap('pythonlogo.png')
        self.uic.image.setPixmap(qpixmap)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())

