from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QButtonGroup, QProgressBar
from PySide6.QtCore import qDebug, QTimer
from PySide6.QtGui import *
from PySide6 import QtCore
from interfaces.ui_mainwindow import Ui_MainWindow
from interfaces.ui_pbmain import Ui_Dialog
import sys
import re

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.c=0
        #PRUEBA2
        #self.actionSalir.triggered.connect(self.close)
        # creamos la subventana pero no la mostramos
        #self.subventana = Subventana()
        # señal para abrir la subventana enviándole el texto del campo
        #self.pushButton_0.clicked.connect(self.btn_click_0)
        self.btn_grp = QButtonGroup()
        self.btn_grp.setExclusive(True)
        self.btn_grp.addButton(self.pushButton_0)
        self.btn_grp.addButton(self.pushButton_1)
        self.btn_grp.addButton(self.pushButton_2)
        self.btn_grp.addButton(self.pushButton_3)
        self.btn_grp.addButton(self.pushButton_4)
        self.btn_grp.addButton(self.pushButton_5)
        self.btn_grp.addButton(self.pushButton_6)
        self.btn_grp.addButton(self.pushButton_7)
        self.btn_grp.addButton(self.pushButton_8)
        self.btn_grp.addButton(self.pushButton_9)
        self.btn_grp.addButton(self.pushButton_punto)
        self.btn_grp.addButton(self.pushButton_igual)
        self.btn_grp.addButton(self.pushButton_divison)
        self.btn_grp.addButton(self.pushButton_multi)
        self.btn_grp.addButton(self.pushButton_resta)
        self.btn_grp.addButton(self.pushButton_suma)
        self.btn_grp.buttonClicked.connect(self.on_click)

        #ProgressBar
        self.subdialog = Dialog()
        self.subdialog.progressBar.setValue(0)
    def on_click(self, value):
        strlabel=self.label.text()


        if strlabel=="0": #Validación primer caracter
            if validacion_operacionesdif(value.text()):
                self.label.setText(value.text())

        elif value.text()=="=": #RESULTADO FINAL

            #Mostrar ProgressBar
            self.timer= QTimer()
            self.timer.setInterval(1000)
            self.subdialog.show()

            #QTimer
            self.c=0
            self.subdialog.progressBar.reset()
            self.subdialog.progressBar.setValue(0)
            self.timer.start()
            self.timer.timeout.connect(self.counter)

            resultado=self.label.text().replace('x', '*')
            #Validación para que no sea una operación el último caracter
            if validacion_operacionesigual(resultado[-1]):
                resultado=resultado[:-1]
            #Validación para cambiar los puntos por 0
            if resultado[0]==".":
                resultado="0"+resultado
            if resultado[-1]==".":
                resultado=resultado+"0"
            auxres=""
            for i in range(len(resultado)):
                if resultado[i]==".":
                    if resultado[i-1]!="0" and resultado[i+1]!="0":
                        auxres +="0"+resultado[i]
                    else:
                        auxres +=resultado[i]
                else:
                    auxres +=resultado[i]
            #Enviar resultados
            print(auxres)
            self.label.setText(str(eval(auxres)))

        elif validacion_operacionesigual(value.text()): #No poner dos veces seguidas una operación
            auxlabel = self.label.text()+value.text()
            listacadena = list(auxlabel)
            #Comparar ultimo caracter con el penultimo
            if (listacadena[len(listacadena)-2] != listacadena[len(listacadena)-1]) and validacion_operacionesdif(listacadena[len(listacadena)-2]):
                self.label.setText(self.label.text()+listacadena[len(listacadena)-1])

        elif value.text()==".": #Validar que no tenga más de un punto
            auxlabel = self.label.text()+value.text()
            #Convertir cadena en arreglo separado por operaciones
            auxlist=re.split('x|/|-|\+', auxlabel)
            if(auxlist[len(auxlist)-1].count(".") <=1):
                self.label.setText(self.label.text()+value.text())

        elif value.text()=="0": #Condición para no escribir un 0 después de una operación
            if validacion_operacionesdif(self.label.text()[-1]):
                self.label.setText(self.label.text()+value.text())

        else:
            self.label.setText(self.label.text()+value.text())

    #Contador QTimer
    def counter(self):
        self.c +=1
        self.subdialog.progressBar.setValue(self.c)
        if self.c>=100:
            self.c=0
            self.timer.stop()
            self.subdialog.progressBar.setValue(0)
            self.subdialog.close()

def validacion_operacionesdif(cadena):
    if cadena!="x" and cadena!="-" and cadena!="+" and cadena!="/" and cadena!="=" and cadena!="*":
        return True
    else:
        return False

def validacion_operacionesigual(cadena):
    if cadena=="x" or cadena=="-" or cadena=="+" or cadena=="/" or cadena=="=" or cadena=="*":
        return True
    else:
        return False        

class Dialog(QWidget, Ui_Dialog):
    def __init__(self):
        # llamamos al constructor
        super().__init__()
        # generamos la interfaz de la subventana
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        # señal para cerrar la subventana
        #self.pushButton.clicked.connect(self.close)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())