
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from interfaces.ui_pbmain import Ui_Dialog
from PySide6.QtCore import QTimer
from PySide6 import QtCore
import sys

class Dialog(QWidget, Ui_Dialog):
    def __init__(self):

        #Variables
        self.c=19
        self.flag10=False
        self.limite=0

        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)

        self.progressBar.setValue(0)

        #Establecer tiempo aquí! (El tiempo tiene que ser un int)
        self.mostrarDialogo(resultado=10)

    #Función de dialogo para mostrar la progress bar
    def mostrarDialogo(self, resultado):

        #Limitar los segundos a 10
        if resultado>=10:
            resultado=9
            self.flag10=True

        self.limite=resultado*20
        self.progressBar.setMaximum(self.limite)

        #Mostrar ProgressBar
        self.timer= QTimer()
        self.timer.setInterval(50) #Intervalos de un segundo (1/20 de segundo)
        self.show()

        #QTimer
        self.c=19
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
                self.dialogoError()

            self.cerrarDialogoPB()
    
    #Muestra ventana de error
    def dialogoError(self):
        QMessageBox.warning(
        self, " Error", "Pasaron más de 10 segundos")

    #Cierra el Dialogo con el Progress Bar
    def cerrarDialogoPB(self):
        if self.isVisible():
            self.c=19
            self.timer.stop()
            self.progressBar.setValue(0)
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Dialog()
    window.show()
    sys.exit(app.exec_())