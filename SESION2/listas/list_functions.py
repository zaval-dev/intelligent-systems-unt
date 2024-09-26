def lee_numero(mensaje):
    while True:
        n = int(input(mensaje))
        if n>0:
            return n
        
def leerLista(n):
    lista = []
    for i in range(n):
        valor = float(input('Ingrese número: '))
        lista.append(valor)
    return lista

def promedio(lista):
    suma = 0
    for elemento in lista:
        suma+=elemento
    return suma/len(lista)

n = lee_numero('Número de elementos de la lista: ')
lista = leerLista(n)
print('El promedio de elementos de la lista es:', promedio(lista))