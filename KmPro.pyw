#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""siempre que se cambie el archivo resultados.ui cambiar tambien el nombre de la clase Ui_Dialog por pyresultados (tambien con pyqr)"""
from PyQt4 import QtCore, QtGui
import sys
import qrencode # apt-get install python-qrencode (para instalar librerias pyqr)
import ConfigParser
from datetime import *
from calculo import Ui_Form
from ayuda import Ui_Dialog
from resultados import pyresultados
from qr import pyqr
from error import Ui_error
from ventanaaceite import Ui_nuevoaceite

archivo = "logs.ini"
Config = ConfigParser.ConfigParser()
Config.read(archivo)

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Myform(QtGui.QMainWindow):
    res = 0
    costoxkmcombustible = 0
    costoxkmaceitesfiltros=0
    costoxkmlavado=0
    costoxkmneumaticos=0
    costoxkmseguro=0
    costoxkmimpuestos=0
    costoxkmgaraje=0
    kmdurantevidautil = 0
    amortizacion = 0
    mantenimiento = 0
    preciocompra = 0
    vidautil = 0
    valorresidual = 0
    kmxmes = 0
    costoxltcomb = 0
    kmxltcomb = 0
    costoxltaceite = 0
    intervaloaceite = 0
    litrosaceitetotales = 0
    costoxneum = 0
    kmxneum = 0
    costopatente = 0
    costorenta = 0
    costoitv = 0
    costofiltros = 0
    costoseguro=0
    costogaraje=0
    costolavado=0
    try:
        UltimoCosto = Config.get("UltimoCosto","valor")
    except:
        UltimoCosto = "No Hay Ultimo Costo"

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui=Ui_Form()
        self.ui.setupUi(self)
        readAceites = open("aceites.txt","r")
        for leerlinea in readAceites:
            self.ui.tipoaceite.addItem(str(leerlinea))
        readAceites.close()

    def resultadofinal(self):
        try:
            self.aceite = self.ui.tipoaceite.currentText()
            if self.ui.gas.isChecked():
                self.combustible = "Gas"
            elif self.ui.gasoil.isChecked():
                self.combustible = "Gasoil"
            elif self.ui.nafta.isChecked():
                self.combustible = "Nafta"
            else:
                self.combustible = "No selecciono"
            if self.ui.siseguro.isChecked():
                self.seguro = "Si"
                self.costoseguro=float(500)
            elif self.ui.noseguro.isChecked():
                self.seguro = "No"
                self.costoseguro=0.0
            else:
                self.seguro = "No"
                self.costoseguro=0.0
            if self.ui.sigaraje.isChecked():
                self.garaje = "Si"
                self.costogaraje=float(300)
            elif self.ui.nogaraje.isChecked():
                self.garaje = "No"
                self.costogaraje=0.0
            else:
                self.garaje = "No"
                self.costogaraje=0.0
            if self.ui.silavado.isChecked():
                self.lavado = "Si"
                self.costolavado=float(50)
            elif self.ui.nolavado.isChecked():
                self.lavado = "No"
                self.costolavado=0.0
            else:
                self.lavado = "No"
                self.costolavado=0.0
            if self.ui.preciocompra.text() == "":
                self.preciocompra=0.0
            else:
                self.preciocompra=float(self.ui.preciocompra.text())
            if self.ui.kmxmes.text() == "":
                self.kmxmes=0.0
            else:
                self.kmxmes=float(self.ui.kmxmes.text())
            if self.ui.vidautil.text() == "":
                self.vidautil=0.0
            else:
                self.vidautil=float(self.ui.vidautil.text())
            if self.ui.valorresidual.text() == "":
                self.valorresidual=0.0
            else:
                self.valorresidual=float(self.ui.valorresidual.text())
            if self.ui.costoxltcomb.text() == "":
               self.costoxltcomb=0.0
            else:
               self.costoxltcomb=float(self.ui.costoxltcomb.text())
            if self.ui.kmxltcomb.text() == "":
                self.kmxltcomb=0.0
            else:
                self.kmxltcomb=float(self.ui.kmxltcomb.text())
            if self.ui.costoxltaceite.text() == "":
                self.costoxltaceite=0.0
            else:
                self.costoxltaceite=float(self.ui.costoxltaceite.text())
            if self.ui.intervaloaceite.text() == "":
                self.intervaloaceite=0.0
            else:
                self.intervaloaceite=float(self.ui.intervaloaceite.text())
            if self.ui.costoxneum.text() == "":
                self.costoxneum=0.0
            else:
                self.costoxneum=float(self.ui.costoxneum.text())
            if self.ui.kmxneum.text() == "":
                self.kmxneum=0.0
            else:
                self.kmxneum=float(self.ui.kmxneum.text())
            if self.ui.costopatente.text() == "":
                self.costopatente=0.0
            else:
                self.costopatente=float(self.ui.costopatente.text())
            if self.ui.costorenta.text() == "":
                self.costorenta=0.0
            else:
                self.costorenta=float(self.ui.costorenta.text())
            if self.ui.costoitv.text() == "":
                self.costoitv=0.0
            else:
                self.costoitv=float(self.ui.costoitv.text())
            if self.ui.litrosaceitetotales.text() == "":
                self.litrosaceitetotales=0.0
            else:
                self.litrosaceitetotales=float(self.ui.litrosaceitetotales.text())
            if self.ui.costofiltros.text() == "":
                self.costofiltros=0.0
            else:
                self.costofiltros=float(self.ui.costofiltros.text())
            #Seteo de cada gasto
            costoxkmcombustible=float(self.costoxltcomb/self.kmxltcomb)
            costoxkmaceitesfiltros=float((self.costoxltaceite*self.litrosaceitetotales+self.costofiltros)/self.intervaloaceite)
            costoxkmlavado=float((self.costolavado*4)/self.kmxmes) #depende del costo del lugar.
            costoxkmneumaticos=float(self.costoxneum/self.kmxneum)
            costoxkmseguro=float(self.costoseguro/self.kmxmes) #depende del tipo de seguro.
            costoxkmimpuestos=float((self.costorenta+self.costopatente+self.costoitv)/(self.kmxmes*12))
            costoxkmgaraje=float(self.costogaraje/self.kmxmes) #depende del costo del lugar.
            kmdurantevidautil = float((self.kmxmes*12)*self.vidautil)
            amortizacion = float((self.preciocompra-self.valorresidual)/kmdurantevidautil)
            mantenimiento = amortizacion
            self.res = '{0:.3g}'.format(float(costoxkmcombustible+costoxkmaceitesfiltros+costoxkmlavado+costoxkmneumaticos+costoxkmseguro+costoxkmimpuestos+costoxkmgaraje+amortizacion+mantenimiento))

            archivo = "logs.ini"
            Config = ConfigParser.ConfigParser()
            Config.read(archivo)
            section = "UltimoCosto"
            writearchivo = open(archivo,"w")
            if self.UltimoCosto == "No Hay Ultimo Costo":
                Config.add_section(section)
                Config.set(section,'valor',self.res)
                Config.write(writearchivo)
                writearchivo.close()
            else:
                Config.remove_section(section)
                Config.add_section(section)
                Config.set(section,'valor',self.res)
                Config.write(writearchivo)
                writearchivo.close()

            results = claseresultados()
            results.exec_()

        except ValueError: #si se ingresan letras.
            openerror = claseerror()
            openerror.setError("No puede ingresar letras.")
            openerror.exec_()
        except ZeroDivisionError: #si se ingresan 0 o no se completan casillas.
            openerror = claseerror()
            openerror.setError("Porfavor, completar las casillas.")
            openerror.exec_()
        except: # no se pudo guardar el nuevo valor en config parser...
            openerror = claseerror()
            openerror.setError("Error al guardar archivos.(ConfigParser)")
            openerror.exec_()

    def reset(self):
        self.res = 0
        self.ui.preciocompra.setText("")
        self.ui.kmxmes.setText("")
        self.ui.vidautil.setText("")
        self.ui.valorresidual.setText("")
        self.ui.costoxltcomb.setText("")
        self.ui.kmxltcomb.setText("")
        self.ui.costoxltaceite.setText("")
        self.ui.intervaloaceite.setText("")
        self.ui.costoxneum.setText("")
        self.ui.kmxneum.setText("")
        self.ui.costopatente.setText("")
        self.ui.costorenta.setText("")
        self.ui.costoitv.setText("")
        self.ui.costofiltros.setText("")
        self.ui.litrosaceitetotales.setText("")
        self.ui.gas.setChecked(True)
        self.ui.nafta.setChecked(False)
        self.ui.gasoil.setChecked(False)
        self.ui.siseguro.setChecked(False)
        self.ui.noseguro.setChecked(False)
        self.ui.silavado.setChecked(False)
        self.ui.nolavado.setChecked(True)
        self.ui.sigaraje.setChecked(False)
        self.ui.nogaraje.setChecked(False)

    def agregaraceite(self):
        ventanaaceite = claseagregaraceite()
        ventanaaceite.exec_()
        self.ui.tipoaceite.addItem(str(ventanaaceite.getNuevo()))

    def ayuda(self):
        ventanaayuda = Dialog()
        ventanaayuda.exec_()

    def getcomb(self):
        return self.combustible

    def getaceite(self):
        return self.aceite

    def getseguro(self):
        return self.seguro

    def getgaraje(self):
        return self.garaje

    def getlavado(self):
        return self.lavado

    def getResultado(self):
        return self.res

    def getUltimoCosto(self):
        return self.UltimoCosto

    def salir(self):
        exit()

class claseresultados(QtGui.QDialog):
    """abre ventana resultados"""
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.dia=pyresultados()
        self.dia.setupUi(self)
        self.dia.varresultados.setText(str(myapp.getResultado())+"$")
        self.dia.vartipocomb.setText(str(myapp.getcomb()))
        self.dia.vartipoaceite.setText(str(myapp.getaceite()))
        self.dia.varseguro.setText(str(myapp.getseguro()))
        self.dia.vargaraje.setText(str(myapp.getgaraje()))
        self.dia.varlavado.setText(str(myapp.getlavado()))
        self.dia.varultima.setText(str(myapp.getUltimoCosto())+"$")

    def funcionqr(self):
        texto = "Costo por Km del automovil: "+str(myapp.getResultado())+" $\nTipo de combustible: "+str(myapp.getcomb())+"\nTipo de aceite: "+str(myapp.getaceite())+"\nSeguro: "+str(myapp.getseguro())+"\nLavado pago: "+str(myapp.getlavado())+"\nGaraje pago: "+str(myapp.getgaraje())
        imagen = qrencode.encode_scaled(texto, 300, version=3, level=3, hint=3, case_sensitive=True)[2]
        imagen.save('./Img/InfoAuto.png')
        self.hide()
        openqr = claseqr()
        openqr.exec_()

class Dialog(QtGui.QDialog):
    """abre ventana de ayuda"""
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self,parent)
        self.dia=Ui_Dialog()
        self.dia.setupUi(self)

class claseqr(QtGui.QDialog):
    """abre ventana de codigo qr"""
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self,parent)
        self.dia=pyqr()
        self.dia.setupUi(self)

    def accept(self):
        self.hide()
        results = claseresultados()
        results.exec_()

class claseagregaraceite(QtGui.QDialog):
    """abre ventana para agregar tipo de aceite"""
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self,parent)
        self.dia=Ui_nuevoaceite()
        self.dia.setupUi(self)

    def accept(self):
        writeaceites= open("aceites.txt","a")
        writeaceites.write(str(self.dia.varagregaraceite.text()+"\n"))
        writeaceites.close()
        self.varagregaraceite = str(self.dia.varagregaraceite.text())
        self.hide()

    def getNuevo(self):
        return self.varagregaraceite

class claseerror(QtGui.QDialog):
    """abre ventana que informa errores"""
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self,parent)
        self.dia=Ui_error()
        self.dia.setupUi(self)

    def setError(self, errorMostrar):
        self.dia.label.setText("Error al realizar las cuentas.\n"+errorMostrar)

if __name__=="__main__":
    app=QtGui.QApplication(sys.argv)
    myapp = Myform()
    myapp.show()
    sys.exit(app.exec_())
