import sys
from PyQt5 import uic, QtWidgets
import matplotlib.pyplot as plt
from sympy import *
import numpy as np
import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from Segunda  import Ui_Segunda

qtCreatorFile = "ProjectF.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

datos_x = []
datos_y = []
LAGRANGE = []
Puerta = False

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
	
	def __init__(self):
		QtWidgets.QMainWindow.__init__(self)
		Ui_MainWindow.__init__(self)
		self.setupUi(self)
		self.Next.clicked.connect(self.Guardar)
		self.Next.clicked.connect(self.DigDatX.clear)
		self.Next.clicked.connect(self.DigDatY.clear)
		self.Calcular.clicked.connect(self.Lagrange)
		self.Lista.stateChanged.connect(self.ListaData)
		self.Polinomio.stateChanged.connect(self.VerPol)       
		self.Grafica_2.clicked.connect(self.Plot)
		self.Import.clicked.connect(self.Obtener)
		self.Limpiar.clicked.connect(self.New)
		self.Limpiar.clicked.connect(self.Mos_Evaluacion.clear)
		self.Limpiar.clicked.connect(self.Mos_Polinomio.clear)
		self.Limpiar.clicked.connect(self.ListDat.clear)
		self.Limpiar.clicked.connect(self.Poliexp.clear)
		self.Limpiar.clicked.connect(self.DigDatY_2.clear)

	def Obtener(self):
         global Puerta
         Puerta = True
         filePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open file")
         if filePath != "" :
            self.datos = pd.ExcelFile(str(filePath))
            self.ComboH.addItems(list(self.datos.sheet_names))
            self.df = self.datos.parse(self.ComboH.currentText())
            self.ComboX.addItems(list(self.df.columns.values))
            self.ComboY.addItems(list(self.df.columns.values))
         global datos_x
         global datos_y
         datos_x = list(self.df["x"][:])
         datos_y = list(self.df["y"][:])

	def Plot(self):
         if Puerta == False :
            global datos_x
            global datos_y
            plt.plot(datos_x , datos_y)
            plt.show()
         else:
            self.df = self.datos.parse(self.ComboH.currentText())
            datos_x = self.df["x"]
            datos_y = self.df["y"]
            plt.plot(datos_x , datos_y)
            plt.show()

	def Guardar(self):
		try:
			X = float (self.DigDatX.toPlainText())
			y = float (self.DigDatY.toPlainText())
		except ValueError:
			self.ventana = QtWidgets.QMainWindow()
			self.ui=Ui_Segunda()
			self.ui.setupUi(self.ventana)
			self.ventana.show()			
		else:
			datos_x.append(X)
			datos_y.append(y)
	
	def ListaData(self):
		Matriz = []
		Matriz.append(datos_x),Matriz.append(datos_y)
		MatrizF = np.array(Matriz)
		ListaF = str(MatrizF)
		self.ListDat.setText(ListaF)
		
	def Lagrange(self):
         x = symbols('x')
         Polinomio = 0
         l=[]
         x_d = float (self.DigDatY_2.toPlainText())
         for i in datos_x:
            li=(np.prod([(x-j)/(i-j) for j in datos_x if i !=j]))
            l.append(li)	
         Polinomio=np.dot(datos_y, l)
         F=simplify(Polinomio)
         print("Polinomio simplificado =" , F)
         Final=str(F)
         LAGRANGE.append(Polinomio)
         self.Mos_Polinomio.setText(Final)
         dato= {x:x_d}
         y_d=float(F.evalf(subs=dato))
         Y_Fin=str(y_d)
         self.Mos_Evaluacion.setText(Y_Fin)
         format("%.2f" %y_d)
         datos_x.append(x_d) , datos_y.append(y_d)
         datos_x.sort() , datos_y.sort()
         print("x =", datos_x)
         print("y =", datos_y)

	def VerPol(self):
		Pol=str(LAGRANGE)
		self.Poliexp.setText(Pol)

	def New(self):
		global LAGRANGE
		global datos_x
		global datos_y
		LAGRANGE = []
		datos_x = []
		datos_y = []

if __name__ == "__main__":
	app =  QtWidgets.QApplication(sys.argv)
	window = MyApp()
	window.show()
	sys.exit(app.exec_())
