import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from UI.rsa import Ui_MainWindow

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        super.ui = Ui_MainWindow()
        self.ui.setupUi()
        self.ui.gen_btn