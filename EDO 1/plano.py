from cmath import sin
import matplotlib.pyplot as plt
import numpy as np

def runge_kutta_4_sistemas(f1, f2, t, u, v, h, n):
    '''
    Función que implementa el método de Runge-Kutta de orden 4 para resolver un sistema de EDOs de primer orden
    '''
    u_vals = []
    v_vals = []
    for i in range(n):
        k11 = f1(t, u, v)
        k12 = f2(t, u, v)
        k21 = f1(t + (h/2), u + ((h/2) * k11), v + ((h/2) * k12))
        k22 = f2(t + (h/2), u + ((h/2) * k11), v + ((h/2) * k12))
        k31 = f1(t + (h/2), u + ((h/2) * k21), v + ((h/2) * k22))
        k32 = f2(t + (h/2), u + ((h/2) * k21), v + ((h/2) * k22))
        k41 = f1(t + h, u + (h * k31), v + (h * k32))
        k42 = f2(t + h, u + (h * k31), v + (h * k32))

        t = t + h 
        u = u + (h/6) * (k11 + (2 * k21) + (2 * k31) + k41)
        v = v + (h/6) * (k12 + (2 * k22) + (2 * k32) + k42)
        u_vals.append(u)
        v_vals.append(v)
    return u_vals, v_vals

def f1(t, u, v):
    '''
    Aquí se define la primera EDO de orden 1 del sistema (para posición)
    '''
    return v

def f2(t, u, v):
    '''
    Aquí se define la segunda EDO de orden 1 del sistema (para velocidad)
    '''
    c = 0.0  # Ajusta este valor según tus necesidades
    k = 1.0  # Ajusta este valor según tus necesidades
    return (-c*v) - (k*np.sin(u))

def generar_datos_iniciales(n):
    '''
    Función que genera n datos iniciales aleatorios entre -2 y 2
    '''
    datos_iniciales = []
    for _ in range(n):
        u0 = np.random.uniform(-2, 2)
        v0 = np.random.uniform(-2, 2)
        datos_iniciales.append((u0, v0))

    return datos_iniciales

def plot_plano_fases(f1, f2, t, datos, h, n):
    '''
    Función que grafica el plano de fases
    '''
    for u0, v0 in datos:
        # Aplicamos el método de Runge-Kutta de orden 4 para resolver el sistema de EDOs de primer orden
        u_vals, v_vals = runge_kutta_4_sistemas(f1, f2, t, u0, v0, h, n)
        # Graficamos
        plt.plot(u_vals, v_vals)

    plt.xlabel('Posición (u)')
    plt.ylabel('Velocidad (v)')
    plt.title('Plano de Fases del Péndulo Simple')
    plt.grid(True)
    plt.show()

# DATOS
# -----
# Rango de t (tiempo)
t_inicial = 0
t_final = 20
# Número de subintervalos que nos permite calcular el valor de h (paso)
n = 1000
h = (t_final - t_inicial)/n

# Generar 20 soluciones con datos iniciales aleatorios
datos_iniciales = generar_datos_iniciales(20)

# Graficar el plano de fases con las 20 soluciones
plot_plano_fases(f1, f2, t_inicial, datos_iniciales, h, n)
