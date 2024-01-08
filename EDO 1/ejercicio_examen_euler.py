
import matplotlib.pyplot as plt
import numpy as np


def euler(f, x, y, h, n):
    '''
    Función que implementa el método de Euler para resolver una EDO
    '''
    u = []
    v = []
    for i in range(n):
        y = y + h * f(x, y)
        x = x + h
        u.append(x)
        v.append(y)
    return u, v

def f(x, y):
    '''
    Aquí se define la EDO despejando y'
    '''
    return y - x**2 + 1

'''def f_exacta1(x):
    
    return (x + 1)**2 - (1/2)*np.exp(x)'''

'''def f_exacta2(x):
   
    return (x + 1)**2 - np.exp(x)'''

'''def f_exacta3(x):
   
    return (x + 1)**2 - 2*np.exp(x)'''

def error(v, v_aprox):
    '''
    Devuelve el error absoluto
    '''
    return abs(v - v_aprox)


# DATOS
# -----
# Rango de x
x_inicial = 0
x_final = 1/2
# Datos iniciales (me da n 3 datos iniciales donde x siempre es igual, pero y varía)
x = 0
y0 = 1/2
#y1 = 0
#y2 = -1
# Número de subintervalos que nos permite calcular el valor de h (paso)
n = 2000
h = (x_final - x_inicial)/n

# Aplicamos el método de Euler 3 veces (una para cada dato inicial) y obtenemos las soluciones numéricas
u0, v0 = euler(f, x, y0, h, n)
#u1, v1 = euler(f, x, y1, h, n)
#u2, v2 = euler(f, x, y2, h, n)

# Obtenemos las soluciones exactas
x_real = np.linspace(x_inicial, x_final, n)
y_real1 = f_exacta1(x_real)
y_real2 = f_exacta2(x_real)
y_real3 = f_exacta3(x_real)

# Imprimimos la última y del bucle con 7 decimales 

print('w_100: {:.7f}'.format(v0[-1]))

#Solucion real en y(1/2)

print('y(1/2): {:.7f}'.format(f_exacta1(1/2)) )

#Error absoluto
v_e=f_exacta1(1/2)
print('Error: {:.7f}'.format(error(v_e, v0[-1])))


# Graficar la solución
# --------------------
# Dibujamos las soluciones numéricas
plt.plot(u0, v0)
plt.plot(u1, v1)
plt.plot(u2, v2)
# Dibujamos las soluciones exactas
plt.plot(x_real, y_real1)
plt.plot(x_real, y_real2)
plt.plot(x_real, y_real3)

plt.grid(True)
plt.show()