# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanaaceite.ui'
#
# Created: Wed Aug 28 08:44:12 2013
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

class Ui_nuevoaceite(object):
    def setupUi(self, nuevoaceite):
        nuevoaceite.setObjectName(_fromUtf8("nuevoaceite"))
        nuevoaceite.resize(319, 56)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Img/auto.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        nuevoaceite.setWindowIcon(icon)
        self.varagregaraceite = QtGui.QLineEdit(nuevoaceite)
        self.varagregaraceite.setGeometry(QtCore.QRect(10, 10, 211, 31))
        self.varagregaraceite.setObjectName(_fromUtf8("varagregaraceite"))
        self.pushButton = QtGui.QPushButton(nuevoaceite)
        self.pushButton.setGeometry(QtCore.QRect(230, 10, 81, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(nuevoaceite)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), nuevoaceite.accept)
        QtCore.QMetaObject.connectSlotsByName(nuevoaceite)

    def retranslateUi(self, nuevoaceite):
        nuevoaceite.setWindowTitle(_translate("nuevoaceite", "Agregar Aceite", None))
        self.pushButton.setText(_translate("nuevoaceite", "Agregar", None))

