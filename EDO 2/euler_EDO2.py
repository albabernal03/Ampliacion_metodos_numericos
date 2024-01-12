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
    '''mi m es la n de la ecuacion de Bessel'''
    #return ((np.exp(-2*x))/(1-x**2))-4*v-4*u
    #return 1-v-u

    #Besel:
    return ((1/x)*v)-((1-((m**2)/(x**2)))*u)

# Datos
m=0
x_inicial = 0
x_final = 20
x = 0.1
u = 0 #recodar que la u es la y
v = 1#es y'
n = 100
h = (x_final - x_inicial) / n

'''cuando queremos j0 dejamos las condicones como están, en cambio si queremos y0 las cambiamos de orden los valores de u y v'''






# Método de Euler de segundo orden 
r, t = euler2(f, x, u, v, h, n,m)



# Gráfica
plt.plot(r, t, label='Solución numérica')
plt.xlabel('x')
plt.ylabel('u(x)')
plt.title('Bessel')
plt.legend()
plt.grid(True)
plt.show()



