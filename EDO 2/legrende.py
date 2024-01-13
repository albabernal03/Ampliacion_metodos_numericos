import matplotlib.pyplot as plt
import numpy as np

def euler2(f, x, u, v, h, n, m):
    r = []
    t = []
    for i in range(n):
        x = x + h
        u = u + h * v
        v = v + h * f(x, u, v, m)
        r.append(x)
        t.append(u)
    return r, t

def f(x, u, v,m): #la m sale de la ecuacion de Bessel
    '''Aqui definimos la EDO de segundo orden (se despeja la y'')'''
    return (2*x)/(1-x**2) * v - (m*(m+1))/(1-x**2) * u

# Datos
x_inicial = 0
x_final = 0.95
x = 0
u0 = 0 #recodar que la u es la y!!!!
v0 = 1 #es y' !!!!
n = 100
h = (x_final - x_inicial) / n
m=0 #para la ecuacion de Legrende

# Método de Euler de segundo orden 
r0, t0 = euler2(f, x, u0, v0, h, n,m)

# Gráfica
plt.plot(r0, t0, label='Solución numérica')
plt.xlabel('x')
plt.ylabel('u(x)')
plt.title('Legrende')
plt.legend()
plt.grid(True)
plt.show()
