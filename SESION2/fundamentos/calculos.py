from math import pi
from script import *

def calculos(r):
    ac = pi*r**2
    lc = 2*pi*r
    return ac, lc

r = leer_numero('Valor del radio: ')
x,y = calculos(r)

print('El area del circulo es: ', x.__round__(2))
print('La longitud de la circunferencia: ', y.__round__(2))