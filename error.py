# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'error.ui'
#
# Created: Wed Aug 28 13:44:25 2013
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

class Ui_error(object):
    def setupUi(self, error):
        error.setObjectName(_fromUtf8("error"))
        error.resize(400, 110)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Img/error.jpeg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        error.setWindowIcon(icon)
        self.label = QtGui.QLabel(error)
        self.label.setGeometry(QtCore.QRect(130, 20, 231, 51))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(error)
        self.label_2.setGeometry(QtCore.QRect(30, 10, 91, 91))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("Img/error.jpeg")))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton = QtGui.QPushButton(error)
        self.pushButton.setGeometry(QtCore.QRect(310, 70, 61, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(error)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), error.accept)
        QtCore.QMetaObject.connectSlotsByName(error)

    def retranslateUi(self, error):
        error.setWindowTitle(_translate("error", "Error", None))
        self.label.setText(_translate("error", "Error al realizar las cuentas. \n"
"Porfavor, rellenar todas las casillas", None))
        self.pushButton.setText(_translate("error", "Ok", None))

