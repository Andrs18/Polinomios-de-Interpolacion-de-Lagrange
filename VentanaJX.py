import sys
from PyQt5 import uic, QtWidgets
import matplotlib.pyplot as plt
from sympy import *
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
#from VentanaX  import Ui_Segunda

qtCreatorFile = "VentanaX.ui"
datos_x = []
datos_y = []
LAGRANGE = []

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
	
	def __init__(self):
		QtWidgets.QMainWindow.__init__(self)
		Ui_MainWindow.__init__(self)
		self.setupUi(self)
		self.Next.clicked.connect(self.Guardar)
		self.Next.clicked.connect(self.DigDatX.clear)
		self.Next.clicked.connect(self.DigDatY.clear)
		self.Calcular.clicked.connect(self.Lagrange)
		self.Lista.stateChanged.connect(self.ListaDat)
		self.Polinomio.stateChanged.connect(self.VerPol)
		self.Grafica_2.stateChanged.connect(self.plot)
		
	def Guardar(self):
		X = float (self.DigDatX.toPlainText())
		datos_x.append(X)
		y = float (self.DigDatY.toPlainText())
		datos_y.append(y)
	
	def ListaDat(self):
		Matriz = []
		Matriz.append(datos_x),Matriz.append(datos_y)
		MatrizF = np.array(Matriz)
		ListaF = str(MatrizF)
		self.ListDat.setText(ListaF)
		
	def plot(self):
		plt.plot(datos_x,datos_y)
		plt.show()
		
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
		Final=str(F)
		LAGRANGE.append(Polinomio)
		self.Mos_Polinomio.setText(Final)
		
		dato= {x:x_d}
		y_d=float(F.evalf(subs=dato))
		Y_Fin=str(y_d)
		ydef = Y_Fin
		self.Mos_Evaluacion.setText(Y_Fin)
		format("%.2f" %y_d)
		datos_x.append(x_d) , datos_y.append(y_d)
		datos_x.sort() , datos_y.sort()
		print("x =", datos_x)
		print("y =", datos_y)
	
	def VerPol(self):
		Pol=str(LAGRANGE)
		self.Poliexp.setText(Pol)

if __name__ == "__main__":
	app =  QtWidgets.QApplication(sys.argv)
	window = MyApp()
	window.show()
	sys.exit(app.exec_())
