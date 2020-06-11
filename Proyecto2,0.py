import matplotlib.pyplot as plt
from sympy import *
import numpy as np

init_printing()

num = int(input("introduce el valor de los datos conocidos: "))
datos_x = []
datos_y = []

for e in range(0,num):
    x_c = float(input("introduce el valor para x_"+str(e)+" "))
    datos_x.append(x_c)
    fx = float(input("introduce el valor para f(x_"+str(e)+") "))
    datos_y.append(fx)
x_d = float(input("introduce el valor de x para calcular f(x): "))
x = symbols('x')
Polinomio = 0
l=[]

for i in datos_x:
    li=(np.prod([(x-j)/(i-j) for j in datos_x if i !=j]))
    l.append(li)
    
Polinomio=np.dot(datos_y, l)
Final=simplify(Polinomio)
pprint(Final)

dato= {x:x_d}
y_d=float(Final.evalf(subs=dato))
format("%.2f" %y_d)
datos_x.append(x_d) , datos_y.append(y_d)
datos_x.sort() , datos_y.sort()
print("x =", datos_x)
print("y =", datos_y)

plt.plot(datos_x,datos_y)
plt.xlabel('x')
plt.ylabel('y')
