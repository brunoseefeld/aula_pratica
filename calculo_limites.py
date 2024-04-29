
#comando para ter as funções que calculam os limites
import limites


#importando mais funções para comparar o tempo dos dois métodos

import math

import time


#testamos com a seguinte função
def f(x):
        y=(x-9)/((x**0.5)-3)
        return y

tolerance=0.00001

x_0=float(input())

limite=limites.Lim(f,x_0,tolerance)

print(f'O limite quando x tende a {x_0} de {f.__name__} é {limite}')


#Iremos encontrar a raíz da seguinte função:
def f_root(x):
        return x**2-9


print("Digite um chute inicial para encontrar a raiz quadrada de 9")

x_initial=float(input())



raiz=limites.Newton(f_root,x_initial, tolerance)



print(f'A raiz quadrada de 9 é {raiz}')



    



