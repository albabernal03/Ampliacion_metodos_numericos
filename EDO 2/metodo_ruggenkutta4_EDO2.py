import matplotlib.pyplot as plt
import numpy as np
import math 


def runge_kutta_4_2(f, x, u, v, c, h, n):
    '''
    Función que implementa el método de Runge-Kutta de orden 4 para resolver una EDO de orden 2
    '''
    r = []
    t = []
    for i in range(n):
        k11 = v
        k12 = f(x, u, v, c)
        k21 = v + (h/2) * k12
        k22 = f(x + (h/2), u + ((h/2) * k11), v + ((h/2) * k12), c)
        k31 = v + ((h/2) * k22)
        k32 = f(x + (h/2), u + ((h/2) * k21), v + ((h/2) * k22), c)
        k41 = v + (h * k32)
        k42 = f(x + h, u + (h * k31), v + (h * k32), c)

        x = x + h
        u = u + (h/6) * (k11 + (2 * k21) + (2 * k31) + k41)
        v = v + (h/6) * (k12 + (2 * k22) + (2 * k32) + k42)
        r.append(x)
        t.append(u)
    return r, t

def f(x, u, v, c):
    '''
    Aquí se define la EDO de orden 2
    '''
    return (-u**2 - (2/x)*v)


# DATOS
# -----
# Dato para polinomios de Tchebyshev: c, constante de la EDO
c = 0
# Rango de x
x_inicial = 0
x_final = 10
# Datos iniciales
x = 0.0000000000001
u = 1 # Recodar que la u es la y
v = 0 # Recodar que la v es la y'
# Número de subintervalos que nos permite calcular el valor de h (paso)
n = 100
h = (x_final - x_inicial)/n

# Aplicamos el método de Runge-Kutta de orden 4 para resolver la EDO de segundo orden
r, t = runge_kutta_4_2(f, x, u, v, c, h, n)


# Graficar la solución
# --------------------
plt.plot(r, t, label='Solución numérica')
plt.xlabel('x')
plt.ylabel('u(x)')

plt.legend()
plt.grid(True)
plt.show()