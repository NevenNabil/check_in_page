from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType

import sys
from check_in_design import Ui_MainWindow

class Main(QMainWindow , Ui_MainWindow):
    def __init__(self, parent=None):
        super(Main, self). __init__(parent)
        QMainWindow. __init__(self)
        self.setupUi(self)
        self.setWindowTitle("Pure life hotels")


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
