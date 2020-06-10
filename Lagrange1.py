import numpy as np 

def lagrange(x):
    L0 = ((np.poly1d([1,0]) - float(matriz[0,1])) / (float(matriz[0,0]) - float(matriz[0,1])))
    print("L0" , type(L0))
    L1 = ((np.poly1d([1,0]) - float(matriz[0,0])) / (float(matriz[0,1]) - float(matriz[0,0])))
    print("L1" , type(L1))
    px = (float(matriz[(1,0)]) * L0) + (float(matriz[(1,1)]) * L1)
    print("px" , type(px))
    return px


num = int(input("Número de datos conocidos: " ))
matriz = np.zeros((2,num))
for e in range(0,num):
    x = float(input("introduce el valor para x_"+str(e)+" "))
    matriz[0,e] = x
    fx = float(input("introduce el valor para f(x_"+str(e)+") "))
    matriz[1,e] = fx
x_des = float(input("introduce el valor de x para calcular f(x): "))
sol = lagrange(x)
#print(type(sol))
print("SOLUCION", sol(x_des))
#print(np.seterr('raise'))
#print("el valor de f(x) es aproximadamente: " , )
#print(matriz)