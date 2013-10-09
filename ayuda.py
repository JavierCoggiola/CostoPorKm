# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ayuda.ui'
#
# Created: Tue Aug 20 19:28:23 2013
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Img/auto.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 381, 221))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(280, 250, 98, 27))
        self.pushButton.setStyleSheet(_fromUtf8("background:rgb(0, 170, 255)"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Ayuda KmPro", None))
        self.label.setText(_translate("Dialog", "\n"
"Vida util: tiempo de uso del auto (tiempo de vida).\n"
"\n"
"Valor residual: valor estimado para vender el vehiculo \n"
"                             luego de la vida ulil (Generalmente es el \n"
"                             40% del valor de compra).\n"
"\n"
"ITV: Inspeccion tecnica vehicular\n"
"\n"
" \n"
"\n"
"-Para calcular el coste presione el boton \'Calcular costo\'\n"
"-Para salir presione el boton \'salir\'\n"
"", None))
        self.pushButton.setText(_translate("Dialog", "Aceptar", None))

