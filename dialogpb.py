
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QButtonGroup, QProgressBar
from interfaces.ui_pbmain import Ui_Dialog
from PySide6 import QtCore

class Dialog(QWidget, Ui_Dialog):
    def __init__(self):
        # llamamos al constructor
        super().__init__()
        # generamos la interfaz de la subventana
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        # señal para cerrar la subventana