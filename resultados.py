# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resultados.ui'
#
# Created: Thu Aug 22 18:35:11 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class pyresultados(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(398, 330)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("auto.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(270, 240, 98, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 20, 271, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.varresultados = QtGui.QLineEdit(Dialog)
        self.varresultados.setEnabled(False)
        self.varresultados.setGeometry(QtCore.QRect(80, 40, 231, 31))
        self.varresultados.setObjectName(_fromUtf8("varresultados"))
        self.vartipocomb = QtGui.QLineEdit(Dialog)
        self.vartipocomb.setEnabled(False)
        self.vartipocomb.setGeometry(QtCore.QRect(170, 80, 113, 27))
        self.vartipocomb.setObjectName(_fromUtf8("vartipocomb"))
        self.vartipoaceite = QtGui.QLineEdit(Dialog)
        self.vartipoaceite.setEnabled(False)
        self.vartipoaceite.setGeometry(QtCore.QRect(170, 120, 113, 27))
        self.vartipoaceite.setObjectName(_fromUtf8("vartipoaceite"))
        self.varseguro = QtGui.QLineEdit(Dialog)
        self.varseguro.setEnabled(False)
        self.varseguro.setGeometry(QtCore.QRect(170, 160, 41, 27))
        self.varseguro.setObjectName(_fromUtf8("varseguro"))
        self.vargaraje = QtGui.QLineEdit(Dialog)
        self.vargaraje.setEnabled(False)
        self.vargaraje.setGeometry(QtCore.QRect(170, 240, 41, 27))
        self.vargaraje.setObjectName(_fromUtf8("vargaraje"))
        self.varlavado = QtGui.QLineEdit(Dialog)
        self.varlavado.setEnabled(False)
        self.varlavado.setGeometry(QtCore.QRect(170, 200, 41, 27))
        self.varlavado.setObjectName(_fromUtf8("varlavado"))
        self.layoutWidget = QtGui.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 80, 143, 191))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtGui.QLabel(self.layoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout.addWidget(self.label_6)
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 200, 98, 27))
        self.pushButton_2.setStyleSheet(_fromUtf8("background:rgb(255, 255, 0)"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(20, 280, 191, 41))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.varultima = QtGui.QLineEdit(Dialog)
        self.varultima.setEnabled(False)
        self.varultima.setGeometry(QtCore.QRect(220, 290, 151, 31))
        self.varultima.setObjectName(_fromUtf8("varultima"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.accept)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.funcionqr)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Resultados", None))
        self.pushButton.setText(_translate("Dialog", "Ok", None))
        self.label.setText(_translate("Dialog", "El Costo por Km de su Automovil es de:", None))
        self.label_2.setText(_translate("Dialog", "Tipo de Combustible:", None))
        self.label_3.setText(_translate("Dialog", "Tipo de aceite:", None))
        self.label_4.setText(_translate("Dialog", "Seguro:", None))
        self.label_5.setText(_translate("Dialog", "Lavado pago:", None))
        self.label_6.setText(_translate("Dialog", "Garaje pago:", None))
        self.pushButton_2.setText(_translate("Dialog", "Ver Code Qr", None))
        self.label_7.setText(_translate("Dialog", "El costo por km de la ultima \n"
"vez que ingreso fue de:", None))

