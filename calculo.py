# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt4.ui'
#
# Created: Wed Aug 28 15:15:34 2013
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(607, 642)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Img/auto.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.preciocompra = QtGui.QLineEdit(Form)
        self.preciocompra.setGeometry(QtCore.QRect(260, 40, 113, 27))
        self.preciocompra.setStyleSheet(_fromUtf8("background:rgb(255, 170, 0)"))
        self.preciocompra.setText(_fromUtf8(""))
        self.preciocompra.setObjectName(_fromUtf8("preciocompra"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(90, 50, 121, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(130, 10, 319, 17))
        self.label_2.setStyleSheet(_fromUtf8("background:rgb(85, 170, 255)"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(90, 110, 141, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(90, 80, 161, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(20, 190, 171, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(20, 270, 101, 20))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(20, 540, 51, 17))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.vidautil = QtGui.QLineEdit(Form)
        self.vidautil.setGeometry(QtCore.QRect(260, 100, 113, 27))
        self.vidautil.setStyleSheet(_fromUtf8("background:rgb(255, 170, 0)"))
        self.vidautil.setText(_fromUtf8(""))
        self.vidautil.setObjectName(_fromUtf8("vidautil"))
        self.kmxmes = QtGui.QLineEdit(Form)
        self.kmxmes.setGeometry(QtCore.QRect(260, 70, 113, 27))
        self.kmxmes.setStyleSheet(_fromUtf8("background:rgb(255, 170, 0)"))
        self.kmxmes.setText(_fromUtf8(""))
        self.kmxmes.setObjectName(_fromUtf8("kmxmes"))
        self.label_8 = QtGui.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(280, 180, 101, 17))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.costoxltcomb = QtGui.QLineEdit(Form)
        self.costoxltcomb.setGeometry(QtCore.QRect(430, 170, 71, 27))
        self.costoxltcomb.setStyleSheet(_fromUtf8("background:rgb(255, 170, 0)"))
        self.costoxltcomb.setText(_fromUtf8(""))
        self.costoxltcomb.setObjectName(_fromUtf8("costoxltcomb"))
        self.label_9 = QtGui.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(250, 210, 171, 17))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.kmxltcomb = QtGui.QLineEdit(Form)
        self.kmxltcomb.setGeometry(QtCore.QRect(430, 200, 71, 27))
        self.kmxltcomb.setStyleSheet(_fromUtf8("background:rgb(255, 170, 0)"))
        self.kmxltcomb.setText(_fromUtf8(""))
        self.kmxltcomb.setObjectName(_fromUtf8("kmxltcomb"))
        self.label_10 = QtGui.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(290, 260, 111, 17))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(20, 590, 51, 17))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(210, 560, 51, 17))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.costoxltaceite = QtGui.QLineEdit(Form)
        self.costoxltaceite.setGeometry(QtCore.QRect(430, 250, 71, 27))
        self.costoxltaceite.setStyleSheet(_fromUtf8("background:rgb(255, 170, 0)"))
        self.costoxltaceite.setText(_fromUtf8(""))
        self.costoxltaceite.setObjectName(_fromUtf8("costoxltaceite"))
        self.label_13 = QtGui.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(10, 390, 161, 17))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_14 = QtGui.QLabel(Form)
        self.label_14.setGeometry(QtCore.QRect(290, 290, 141, 16))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.intervaloaceite = QtGui.QLineEdit(Form)
        self.intervaloaceite.setGeometry(QtCore.QRect(430, 280, 71, 27))
        self.intervaloaceite.setStyleSheet(_fromUtf8("background:rgb(255, 170, 0)"))
        self.intervaloaceite.setText(_fromUtf8(""))
        self.intervaloaceite.setObjectName(_fromUtf8("intervaloaceite"))
        self.costoxneum = QtGui.QLineEdit(Form)
        self.costoxneum.setGeometry(QtCore.QRect(170, 380, 61, 27))
        self.costoxneum.setStyleSheet(_fromUtf8("background:rgb(255, 170, 0)"))
        self.costoxneum.setText(_fromUtf8(""))
        self.costoxneum.setObjectName(_fromUtf8("costoxneum"))
        self.label_15 = QtGui.QLabel(Form)
        self.label_15.setGeometry(QtCore.QRect(60, 440, 141, 17))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(90, 590, 101, 24))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.sigaraje = QtGui.QCheckBox(self.layoutWidget)
        self.sigaraje.setObjectName(_fromUtf8("sigaraje"))
        self.horizontalLayout_2.addWidget(self.sigaraje)
        self.nogaraje = QtGui.QCheckBox(self.layoutWidget)
        self.nogaraje.setObjectName(_fromUtf8("nogaraje"))
        self.horizontalLayout_2.addWidget(self.nogaraje)
        self.label_16 = QtGui.QLabel(Form)
        self.label_16.setGeometry(QtCore.QRect(270, 390, 231, 17))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.kmxneum = QtGui.QLineEdit(Form)
        self.kmxneum.setGeometry(QtCore.QRect(510, 380, 61, 27))
        self.kmxneum.setStyleSheet(_fromUtf8("background:rgb(255, 170, 0)"))
        self.kmxneum.setText(_fromUtf8(""))
        self.kmxneum.setObjectName(_fromUtf8("kmxneum"))
        self.splitter_2 = QtGui.QSplitter(Form)
        self.splitter_2.setGeometry(QtCore.QRect(270, 540, 116, 66))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.nolavado = QtGui.QRadioButton(self.splitter_2)
        self.nolavado.setObjectName(_fromUtf8("nolavado"))
        self.silavado = QtGui.QRadioButton(self.splitter_2)
        self.silavado.setObjectName(_fromUtf8("silavado"))
        self.costopatente = QtGui.QLineEdit(Form)
        self.costopatente.setGeometry(QtCore.QRect(210, 430, 71, 27))
        self.costopatente.setStyleSheet(_fromUtf8("background:rgb(255, 170, 0)"))
        self.costopatente.setText(_fromUtf8(""))
        self.costopatente.setObjectName(_fromUtf8("costopatente"))
        self.label_17 = QtGui.QLabel(Form)
        self.label_17.setGeometry(QtCore.QRect(380, 50, 16, 17))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.label_20 = QtGui.QLabel(Form)
        self.label_20.setGeometry(QtCore.QRect(380, 110, 41, 17))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.label_21 = QtGui.QLabel(Form)
        self.label_21.setGeometry(QtCore.QRect(380, 80, 31, 17))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.label_22 = QtGui.QLabel(Form)
        self.label_22.setGeometry(QtCore.QRect(510, 180, 16, 17))
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.label_23 = QtGui.QLabel(Form)
        self.label_23.setGeometry(QtCore.QRect(510, 290, 21, 17))
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.label_24 = QtGui.QLabel(Form)
        self.label_24.setGeometry(QtCore.QRect(580, 390, 21, 17))
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.label_25 = QtGui.QLabel(Form)
        self.label_25.setGeometry(QtCore.QRect(510, 210, 21, 17))
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.label_26 = QtGui.QLabel(Form)
        self.label_26.setGeometry(QtCore.QRect(510, 260, 16, 17))
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.label_27 = QtGui.QLabel(Form)
        self.label_27.setGeometry(QtCore.QRect(290, 440, 16, 17))
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.label_28 = QtGui.QLabel(Form)
        self.label_28.setGeometry(QtCore.QRect(240, 390, 16, 17))
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.tipoaceite = QtGui.QComboBox(Form)
        self.tipoaceite.setGeometry(QtCore.QRect(120, 250, 131, 41))
        self.tipoaceite.setObjectName(_fromUtf8("tipoaceite"))
        self.splitter = QtGui.QSplitter(Form)
        self.splitter.setGeometry(QtCore.QRect(160, 170, 91, 66))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.gas = QtGui.QRadioButton(self.splitter)
        self.gas.setChecked(True)
        self.gas.setObjectName(_fromUtf8("gas"))
        self.gasoil = QtGui.QRadioButton(self.splitter)
        self.gasoil.setObjectName(_fromUtf8("gasoil"))
        self.nafta = QtGui.QRadioButton(self.splitter)
        self.nafta.setObjectName(_fromUtf8("nafta"))
        self.layoutWidget1 = QtGui.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(90, 540, 101, 24))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.siseguro = QtGui.QCheckBox(self.layoutWidget1)
        self.siseguro.setObjectName(_fromUtf8("siseguro"))
        self.horizontalLayout.addWidget(self.siseguro)
        self.noseguro = QtGui.QCheckBox(self.layoutWidget1)
        self.noseguro.setObjectName(_fromUtf8("noseguro"))
        self.horizontalLayout.addWidget(self.noseguro)
        self.layoutWidget2 = QtGui.QWidget(Form)
        self.layoutWidget2.setGeometry(QtCore.QRect(420, 540, 180, 90))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.calcular = QtGui.QPushButton(self.layoutWidget2)
        self.calcular.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Bookman L"))
        font.setBold(True)
        font.setWeight(75)
        self.calcular.setFont(font)
        self.calcular.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.calcular.setMouseTracking(False)
        self.calcular.setStyleSheet(_fromUtf8("background:rgb(0, 170, 0)"))
        self.calcular.setIconSize(QtCore.QSize(16, 16))
        self.calcular.setObjectName(_fromUtf8("calcular"))
        self.verticalLayout.addWidget(self.calcular)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.ayuda = QtGui.QPushButton(self.layoutWidget2)
        self.ayuda.setObjectName(_fromUtf8("ayuda"))
        self.horizontalLayout_3.addWidget(self.ayuda)
        self.pushButton = QtGui.QPushButton(self.layoutWidget2)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.label_18 = QtGui.QLabel(Form)
        self.label_18.setGeometry(QtCore.QRect(350, 410, 221, 111))
        self.label_18.setText(_fromUtf8(""))
        self.label_18.setPixmap(QtGui.QPixmap(_fromUtf8("Img/auto.png")))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.label_32 = QtGui.QLabel(Form)
        self.label_32.setGeometry(QtCore.QRect(60, 470, 121, 17))
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.costorenta = QtGui.QLineEdit(Form)
        self.costorenta.setGeometry(QtCore.QRect(210, 460, 71, 27))
        self.costorenta.setStyleSheet(_fromUtf8("background:rgb(255, 170, 0)"))
        self.costorenta.setText(_fromUtf8(""))
        self.costorenta.setObjectName(_fromUtf8("costorenta"))
        self.label_33 = QtGui.QLabel(Form)
        self.label_33.setGeometry(QtCore.QRect(290, 470, 16, 17))
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.label_30 = QtGui.QLabel(Form)
        self.label_30.setGeometry(QtCore.QRect(90, 140, 141, 20))
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.valorresidual = QtGui.QLineEdit(Form)
        self.valorresidual.setGeometry(QtCore.QRect(260, 130, 111, 31))
        self.valorresidual.setStyleSheet(_fromUtf8("background:rgb(255, 170, 0)"))
        self.valorresidual.setText(_fromUtf8(""))
        self.valorresidual.setObjectName(_fromUtf8("valorresidual"))
        self.label_31 = QtGui.QLabel(Form)
        self.label_31.setGeometry(QtCore.QRect(380, 140, 16, 17))
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(520, 10, 71, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_34 = QtGui.QLabel(Form)
        self.label_34.setGeometry(QtCore.QRect(290, 500, 16, 17))
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.costoitv = QtGui.QLineEdit(Form)
        self.costoitv.setGeometry(QtCore.QRect(210, 490, 71, 27))
        self.costoitv.setStyleSheet(_fromUtf8("background:rgb(255, 170, 0)"))
        self.costoitv.setText(_fromUtf8(""))
        self.costoitv.setObjectName(_fromUtf8("costoitv"))
        self.label_35 = QtGui.QLabel(Form)
        self.label_35.setGeometry(QtCore.QRect(60, 500, 121, 17))
        self.label_35.setObjectName(_fromUtf8("label_35"))
        self.label_29 = QtGui.QLabel(Form)
        self.label_29.setGeometry(QtCore.QRect(570, 320, 21, 17))
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.label_19 = QtGui.QLabel(Form)
        self.label_19.setGeometry(QtCore.QRect(290, 320, 191, 16))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.litrosaceitetotales = QtGui.QLineEdit(Form)
        self.litrosaceitetotales.setGeometry(QtCore.QRect(490, 310, 71, 27))
        self.litrosaceitetotales.setStyleSheet(_fromUtf8("background:rgb(255, 170, 0)"))
        self.litrosaceitetotales.setText(_fromUtf8(""))
        self.litrosaceitetotales.setObjectName(_fromUtf8("litrosaceitetotales"))
        self.label_36 = QtGui.QLabel(Form)
        self.label_36.setGeometry(QtCore.QRect(10, 330, 131, 17))
        self.label_36.setObjectName(_fromUtf8("label_36"))
        self.label_37 = QtGui.QLabel(Form)
        self.label_37.setGeometry(QtCore.QRect(10, 350, 181, 17))
        self.label_37.setObjectName(_fromUtf8("label_37"))
        self.costofiltros = QtGui.QLineEdit(Form)
        self.costofiltros.setGeometry(QtCore.QRect(150, 320, 61, 27))
        self.costofiltros.setStyleSheet(_fromUtf8("background:rgb(255, 170, 0)"))
        self.costofiltros.setText(_fromUtf8(""))
        self.costofiltros.setObjectName(_fromUtf8("costofiltros"))
        self.label_38 = QtGui.QLabel(Form)
        self.label_38.setGeometry(QtCore.QRect(220, 330, 16, 17))
        self.label_38.setObjectName(_fromUtf8("label_38"))
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(250, 250, 31, 41))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.calcular, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.resultadofinal)
        QtCore.QObject.connect(self.ayuda, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.ayuda)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.salir)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.reset)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.agregaraceite)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.preciocompra, self.kmxmes)
        Form.setTabOrder(self.kmxmes, self.vidautil)
        Form.setTabOrder(self.vidautil, self.valorresidual)
        Form.setTabOrder(self.valorresidual, self.gas)
        Form.setTabOrder(self.gas, self.gasoil)
        Form.setTabOrder(self.gasoil, self.nafta)
        Form.setTabOrder(self.nafta, self.costoxltcomb)
        Form.setTabOrder(self.costoxltcomb, self.kmxltcomb)
        Form.setTabOrder(self.kmxltcomb, self.tipoaceite)
        Form.setTabOrder(self.tipoaceite, self.costoxltaceite)
        Form.setTabOrder(self.costoxltaceite, self.intervaloaceite)
        Form.setTabOrder(self.intervaloaceite, self.litrosaceitetotales)
        Form.setTabOrder(self.litrosaceitetotales, self.costofiltros)
        Form.setTabOrder(self.costofiltros, self.costoxneum)
        Form.setTabOrder(self.costoxneum, self.kmxneum)
        Form.setTabOrder(self.kmxneum, self.costopatente)
        Form.setTabOrder(self.costopatente, self.costorenta)
        Form.setTabOrder(self.costorenta, self.costoitv)
        Form.setTabOrder(self.costoitv, self.siseguro)
        Form.setTabOrder(self.siseguro, self.noseguro)
        Form.setTabOrder(self.noseguro, self.sigaraje)
        Form.setTabOrder(self.sigaraje, self.nogaraje)
        Form.setTabOrder(self.nogaraje, self.nolavado)
        Form.setTabOrder(self.nolavado, self.silavado)
        Form.setTabOrder(self.silavado, self.ayuda)
        Form.setTabOrder(self.ayuda, self.pushButton_2)
        Form.setTabOrder(self.pushButton_2, self.pushButton)
        Form.setTabOrder(self.pushButton, self.calcular)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "KmPro (Taxis/Remis)", None))
        self.label.setText(_translate("Form", "Precio de compra:", None))
        self.label_2.setText(_translate("Form", "Calculo del coste por kilometro de un automovil", None))
        self.label_3.setText(_translate("Form", "Vida util del vehiculo:", None))
        self.label_4.setText(_translate("Form", "Km por mes estimados:", None))
        self.label_5.setText(_translate("Form", "Tipo de combustible:", None))
        self.label_6.setText(_translate("Form", "Tipo de Aceite:", None))
        self.label_7.setText(_translate("Form", "Seguro:", None))
        self.label_8.setText(_translate("Form", "Costo por litro:", None))
        self.label_9.setText(_translate("Form", "Cuantos km rinde el litro:", None))
        self.label_10.setText(_translate("Form", "Precio por litro:", None))
        self.label_11.setText(_translate("Form", "Garaje:", None))
        self.label_12.setText(_translate("Form", "Lavado:", None))
        self.label_13.setText(_translate("Form", "Costo de 5 neumáticos:", None))
        self.label_14.setText(_translate("Form", "Intervalo de cambio:", None))
        self.label_15.setText(_translate("Form", "Costo anual patente:", None))
        self.sigaraje.setText(_translate("Form", "Sí", None))
        self.nogaraje.setText(_translate("Form", "No", None))
        self.label_16.setText(_translate("Form", "Duración del juego de neumáticos:", None))
        self.nolavado.setText(_translate("Form", "Manual", None))
        self.silavado.setText(_translate("Form", "Pago", None))
        self.label_17.setText(_translate("Form", "$", None))
        self.label_20.setText(_translate("Form", "Años", None))
        self.label_21.setText(_translate("Form", "Km", None))
        self.label_22.setText(_translate("Form", "$", None))
        self.label_23.setText(_translate("Form", "Km", None))
        self.label_24.setText(_translate("Form", "Km", None))
        self.label_25.setText(_translate("Form", "Km", None))
        self.label_26.setText(_translate("Form", "$", None))
        self.label_27.setText(_translate("Form", "$", None))
        self.label_28.setText(_translate("Form", "$", None))
        self.gas.setText(_translate("Form", "Gas", None))
        self.gasoil.setText(_translate("Form", "Gasoil", None))
        self.nafta.setText(_translate("Form", "Nafta", None))
        self.siseguro.setText(_translate("Form", "Sí", None))
        self.noseguro.setText(_translate("Form", "No", None))
        self.calcular.setText(_translate("Form", "Calcular costo", None))
        self.ayuda.setText(_translate("Form", "Ayuda", None))
        self.pushButton.setText(_translate("Form", "Salir", None))
        self.label_32.setText(_translate("Form", "Costo anual renta:", None))
        self.label_33.setText(_translate("Form", "$", None))
        self.label_30.setText(_translate("Form", "Valor Residual:", None))
        self.label_31.setText(_translate("Form", "$", None))
        self.pushButton_2.setText(_translate("Form", "Resetear", None))
        self.label_34.setText(_translate("Form", "$", None))
        self.label_35.setText(_translate("Form", "Costo anual ITV:", None))
        self.label_29.setText(_translate("Form", "Lt", None))
        self.label_19.setText(_translate("Form", "Litros de aceite del vehiculo:", None))
        self.label_36.setText(_translate("Form", "Costo total Filtros:", None))
        self.label_37.setText(_translate("Form", "(aceite,aire y combustible)", None))
        self.label_38.setText(_translate("Form", "$", None))
        self.pushButton_3.setText(_translate("Form", "+", None))

