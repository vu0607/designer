import sys
import cv2
#from typing_extensions import Self
from PyQt5.QtWidgets import QApplication,QMainWindow
from designer import Ui_MainWindow

class MainWindow:  #laydulieubenfilegocqua
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        self.showtext()

    def show(self):
        self.main_win.show()
    # Hien thi thong tin 
    def showtext(self):
        self.uic.inforCCCD.setText('19212814931')
        self.uic.inforDoB.setText('06/07/2000')
        self.uic.inforName.setText('Dang Nguyen Vu')
        
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
