##
# @file dialogpb.py
#
# @brief Muestra una barra de progreso en un dialog
#
# @section description_dialogpb Descripción
# Muestra una barra de progreso tomandando en cuenta dos variables
# - Tiempo
# - Tiempo maximo
#
# @section libraries_dialogpb Libraries/Modules
# - PySide6
#   -QCore
#
# @section notes_dialogpb Notas
# - Se hacen varias operaciones para llenar la Progress Bar
#
# @section todo_sensors TODO
# - None.
#
# @section author_sensors Autore(s)
# - Creado por Santiago Carrillo on 22/11/2023.
#
# Copyright (c) 2023 Santiago Carrillo.  All rights reserved.

# Imports
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from interfaces.ui_pbmain import Ui_Dialog
from PySide6.QtCore import QTimer
from PySide6 import QtCore
import sys

class Dialog(QWidget, Ui_Dialog):
    def __init__(self):

        #Variables
        self.c=0
        self.flag10=False
        self.limite=0
        self.tm=0

        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)

        self.progressBar.setValue(0)
        
    #Función de dialogo para mostrar la progress bar
    def mostrarDialogo(self, resultado, tmaximo):
        self.show()
        self.progressBar.setValue(0)
        #Limitar los segundos a 10
        if resultado>=tmaximo:
            resultado=tmaximo-1
            self.flag10=True

        self.limite=resultado*1000
        self.progressBar.setMaximum(self.limite)
        self.tm=tmaximo

        #Mostrar ProgressBar
        self.timer= QTimer()
        self.timer.setInterval(1) #Intervalos de un segundo (1/1000 de segundo)
        self.show()

        #QTimer
        self.c=0
        self.progressBar.reset()
        self.progressBar.setValue(0)
        self.timer.start()
        self.timer.timeout.connect(self.counter)

    #Contador QTimer
    def counter(self):
        self.c +=1
        self.progressBar.setValue(self.c)
        if self.c>self.limite:
            #Condición para saber si pasaron más de 10 segundos marque un error
            if self.flag10:
                self.flag10 = False
                QMessageBox.warning(self, " Error", "Pasaron más de "+str(self.tm)+" segundos")

            self.cerrarDialogoPB()
    

    #Cierra el Dialogo con el Progress Bar
    def cerrarDialogoPB(self):
        if self.isVisible():
            self.c=0
            self.timer.stop()
            self.progressBar.setValue(0)
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Dialog()
    window.show()
    sys.exit(app.exec_())