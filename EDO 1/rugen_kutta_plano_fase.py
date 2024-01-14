from cmath import sin
import matplotlib.pyplot as plt
import numpy as np
import math 


def runge_kutta_4_plano(f1, f2, t, x, y, h, n):
    '''
    Función que implementa el método de Runge-Kutta de orden 4 para resolver un sistema de EDOs de primer orden
    '''
    u = []
    v = []
    for i in range(n):
        k11 = f1(t, x, y)
        k12 = f2(t, x, y)
        k21 = f1(t + (h/2), x + ((h/2) * k11), y + ((h/2) * k12))
        k22 = f2(t + (h/2), x + ((h/2) * k11), y + ((h/2) * k12))
        k31 = f1(t + (h/2), x + ((h/2) * k21), y + ((h/2) * k22))
        k32 = f2(t + (h/2), x + ((h/2) * k21), y + ((h/2) * k22))
        k41 = f1(t + h, x + (h * k31), y + (h * k32))
        k42 = f2(t + h, x + (h * k31), y + (h * k32))

        t = t + h 
        x = x + (h/6) * (k11 + (2 * k21) + (2 * k31) + k41)
        y = y + (h/6) * (k12 + (2 * k22) + (2 * k32) + k42)
        u.append(x)
        v.append(y)
    return u, v

def f1(t, x, y):
    '''
    Aquí se define la primera EDO de orden 1 del sistema
    '''
    #return y
    return - y + x*(1 - x**2 - y**2)

def f2(t, x, y):
    '''
    Aquí se define la segunda EDO de orden 1 del sistema
    '''
    return  x + y*(1 - x**2 - y**2)

def generar_datos_iniciales(n):
    '''
    Función que genera n datos iniciales aleatorios entre -2 y 2
    '''
    datos_iniciales = []
    for _ in range(n):
        x0 = np.random.uniform(-2, 2)
        y0 = np.random.uniform(-2, 2)
        datos_iniciales.append((x0, y0))

    return datos_iniciales

def plot_plano_fases(f1, f2, t, datos, h, n):
    '''
    Función que grafica el plano de fases
    '''
    for x0, y0 in datos:
        # Aplicamos el método de Runge-Kutta de orden 4 para resolver el sistema de EDOs de primer orden
        u, v = runge_kutta_4_plano(f1, f2, t, x0, y0, h, n)
        # Graficamos
        plt.plot(u, v)

    plt.xlim(-2, 2)
    plt.ylim(-2, 2)

    plt.xlabel('x(t)')
    plt.ylabel('y(t)')
    plt.title('Plano de Fases')
    plt.grid(True)
    plt.show()

# DATOS
# -----
k = 1
c = 0
# Rango de t (tiempo)
t_inicial = 0 # Normalmente siempre arranca en 0
t_final = 15
# Datos iniciales
t = 0
x = 0.5 # Primera EDO1 del sistema
y = 0 # Segunda EDO1 del sistema

# Número de subintervalos que nos permite calcular el valor de h (paso)
n = 200
h = (t_final - t_inicial)/n

# Generar 20 soluciones con datos iniciales aleatorios
datos_iniciales = generar_datos_iniciales(20)

# Graficar el plano de fases con las 20 soluciones
plot_plano_fases(f1, f2, t, datos_iniciales, h, n)