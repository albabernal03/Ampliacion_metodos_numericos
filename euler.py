import matplotlib.pyplot as plt
import numpy as np


#EJERCIO APLICANDO EULER
def euler(f,x,y,h,n):
    u = []
    v = []
    for i in range(n):
        y = y + h*f(x,y)
        x = x + h
        u.append(x)
        v.append(y)
    return u,v

def f(x,y):
    '''Aqui añadimos la EDO'''
    #return (np.exp(x))/((1+np.exp(x))*y)
    #return (x*y)/(x**2 + y**2)
    return 9.8-0.05*y
    

def f_exacta(x):
    
    #return np.sqrt(2 * np.log(1 + np.exp(x)) + 0.746144)
    return 245-245*np.exp(-0.04*x)




def error(v, v_aprox):
    '''
    Devuelve el error absoluto
    '''
    return abs(v - v_aprox)

#DATOS
x_inicial=0
x_final=100

x = 0
y = 0
n = 2000
h = (x_final-x_inicial)/n
u,v = euler(f,x,y,h,n)

print('w_100', v[-1])

#solucion real en y(100)
print('y(100)=', f_exacta(100)) #es la ultima x del rango

#Error
#v_exacta = f_exacta(1)
#print('Error: ', error(v_exacta,v[-1]))

#Grafica
plt.plot(u,v,label='Euler')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
plt.savefig('graficagota2.png')

