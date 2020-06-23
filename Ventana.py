import sys
from PyQt5 import uic, QtWidgets
import matplotlib.pyplot as plt
from sympy import *
import numpy as np

qtCreatorFile = "Ventana.ui"

datos_x = []
datos_y = []

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.Calcular.clicked.connect(self.Lagrange)
        self.Next.clicked.connect(self.Guardar)
        self.Next.clicked.connect(self.DigDatX.clear)
        self.Next.clicked.connect(self.DigDatY.clear)
 
    def Guardar(self):
        X = float (self.DigDatX.toPlainText())
        datos_x.append(X)
        y = float (self.DigDatY.toPlainText())
        datos_y.append(y)
        
        
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

    

if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())