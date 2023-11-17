# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)
import recursos_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(615, 435)
        MainWindow.setMinimumSize(QSize(615, 435))
        MainWindow.setMaximumSize(QSize(800, 435))
        icon = QIcon()
        icon.addFile(u":/iconos/imagenes/calculadora.jpg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QPushButton {\n"
"  border-radius: 10px;\n"
"  background: #B2BEB5;\n"
"  padding: 20px;\n"
"  margin: 2px;\n"
"}")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Arial Rounded MT Std"])
        font.setPointSize(36)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"QLabel {\n"
"	border-radius: 10px;\n"
"    background: #89CFF0;\n"
"	margin:2px;\n"
"	border: 2px solid black;\n"
"}")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 4)

        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMaximumSize(QSize(130, 70))
        font1 = QFont()
        font1.setFamilies([u"Arial Rounded MT Std Extra Bold"])
        font1.setPointSize(18)
        font1.setBold(True)
        self.pushButton_6.setFont(font1)
        self.pushButton_6.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pushButton_6, 2, 2, 1, 1)

        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMaximumSize(QSize(130, 70))
        self.pushButton_7.setFont(font1)
        self.pushButton_7.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pushButton_7, 3, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMaximumSize(QSize(130, 70))
        self.pushButton_5.setFont(font1)
        self.pushButton_5.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pushButton_5, 2, 1, 1, 1)

        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMaximumSize(QSize(130, 70))
        self.pushButton_4.setFont(font1)
        self.pushButton_4.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pushButton_4, 2, 0, 1, 1)

        self.pushButton_punto = QPushButton(self.centralwidget)
        self.pushButton_punto.setObjectName(u"pushButton_punto")
        self.pushButton_punto.setMaximumSize(QSize(130, 70))
        self.pushButton_punto.setFont(font1)
        self.pushButton_punto.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pushButton_punto, 4, 0, 1, 1)

        self.pushButton_divison = QPushButton(self.centralwidget)
        self.pushButton_divison.setObjectName(u"pushButton_divison")
        self.pushButton_divison.setMaximumSize(QSize(130, 70))
        self.pushButton_divison.setFont(font1)
        self.pushButton_divison.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pushButton_divison, 1, 3, 1, 1)

        self.pushButton_1 = QPushButton(self.centralwidget)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setMaximumSize(QSize(130, 70))
        self.pushButton_1.setFont(font1)
        self.pushButton_1.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pushButton_1, 1, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMaximumSize(QSize(130, 70))
        self.pushButton_3.setFont(font1)
        self.pushButton_3.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pushButton_3, 1, 2, 1, 1)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMaximumSize(QSize(130, 70))
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)

        self.pushButton_multi = QPushButton(self.centralwidget)
        self.pushButton_multi.setObjectName(u"pushButton_multi")
        self.pushButton_multi.setMaximumSize(QSize(130, 70))
        self.pushButton_multi.setFont(font1)
        self.pushButton_multi.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pushButton_multi, 2, 3, 1, 1)

        self.pushButton_suma = QPushButton(self.centralwidget)
        self.pushButton_suma.setObjectName(u"pushButton_suma")
        self.pushButton_suma.setMaximumSize(QSize(130, 70))
        self.pushButton_suma.setFont(font1)
        self.pushButton_suma.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pushButton_suma, 4, 3, 1, 1)

        self.pushButton_resta = QPushButton(self.centralwidget)
        self.pushButton_resta.setObjectName(u"pushButton_resta")
        self.pushButton_resta.setMaximumSize(QSize(130, 70))
        self.pushButton_resta.setFont(font1)
        self.pushButton_resta.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pushButton_resta, 3, 3, 1, 1)

        self.pushButton_igual = QPushButton(self.centralwidget)
        self.pushButton_igual.setObjectName(u"pushButton_igual")
        self.pushButton_igual.setMaximumSize(QSize(130, 70))
        self.pushButton_igual.setFont(font1)
        self.pushButton_igual.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pushButton_igual, 4, 2, 1, 1)

        self.pushButton_0 = QPushButton(self.centralwidget)
        self.pushButton_0.setObjectName(u"pushButton_0")
        self.pushButton_0.setMaximumSize(QSize(130, 70))
        self.pushButton_0.setFont(font1)
        self.pushButton_0.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pushButton_0, 4, 1, 1, 1)

        self.pushButton_9 = QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMaximumSize(QSize(130, 70))
        self.pushButton_9.setFont(font1)
        self.pushButton_9.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pushButton_9, 3, 2, 1, 1)

        self.pushButton_8 = QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMaximumSize(QSize(130, 70))
        self.pushButton_8.setFont(font1)
        self.pushButton_8.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pushButton_8, 3, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 615, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Calculadora", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushButton_punto.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.pushButton_divison.setText(QCoreApplication.translate("MainWindow", u"\u00f7", None))
        self.pushButton_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButton_multi.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.pushButton_suma.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.pushButton_resta.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pushButton_igual.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.pushButton_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
    # retranslateUi

