import matplotlib.pyplot as plt
import numpy as np
import math

def runge_kutta_4_edo_2(f, x, u, v, h, n):
    '''
    Función que implementa el método de Runge-Kutta de orden 4 para resolver una EDO
    '''
    r = []
    t = []
    for i in range(n):

        k11 = v
        k12 = f(x, u, v)
        k21 = v + (h/2)*k12
        k22 = f(x+(h/2), u+(h/2)*k11, v+(h/2)*k12)
        k31 = v + (h/2)*k22
        k32 = f(x+(h/2), u+(h/2)*k21, v+(h/2)*k22)
        k41 = v + h*k32
        k42 = f(x+h, u+h*k31, v+h*k32)

        u = u + h * (((1/6) * k11) + ((1/3) * k21) + ((1/3) * k31) + ((1/6) * k41))
        v = v + h * (((1/6) * k12) + ((1/3) * k22) + ((1/3) * k32) + ((1/6) * k42))
        x = x + h
        r.append(x)
        t.append(u)
    return r, t

def f(x, u, v): #la c sale de lo de Tchebyshev que corresponde con la n
    '''
    Aquí se define la EDO
    '''
    return (3*x*v - (n*(n+2))*u)/(1-x**2)



# DATOS



c = int(input("Introduce el valor de c: ")) #La c corresponde con Tchebyshev
# Rango de x
x_inicial = -1
x_final = 1
# Datos iniciales
x = -0.999
u = (-1)**c  #recodar que la u es la y
sumatorio = 0
for m in range(0, math.floor(c/2)):
    sumatorio += (-1)**m * (math.factorial(c-m-1))/(np.math.factorial(m)*np.math.factorial(c-2*m-1))*(-2)**(c-2*m-1)
v = sumatorio
# Número de subintervalos que nos permite calcular el valor de h (paso)
n = 100
h = (x_final - x_inicial)/n

r, t = runge_kutta_4_edo_2(f, x, u, v, h, n)
#print('w_100: {:.7f}'.format(t[-1]))

# Gráfica
plt.plot(r, t)
plt.xlabel('x')
plt.ylabel('u(x)')
plt.grid(True)
plt.savefig('para_c_2')
