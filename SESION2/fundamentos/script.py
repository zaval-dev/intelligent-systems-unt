def mostrar_mensaje(mensaje):
    print(mensaje)

# mostrar_mensaje('Hola mundo')

def leer_numero(mensaje):
    while True:
        num = int(input(mensaje))
        if num > 0:
            return num
        
def reporte_divisores(n):
    print('Los divisores de', n, 'son: ')
    for i in range(1, n+1):
        if n % i == 0:
            print(i, end=" ")

def es_primo(n):
    cd = 0
    for i in range(1, n+1):
        if n % i == 0:
            cd+=1
    if cd == 2:
        return True
    return False

# n = leer_numero('Digita un número positivo: ')
# reporte_divisores(n)
# if(es_primo(n)):
#     print('El número', n, 'es primo.')
# else:
#     print('El número', n, 'no es primo.')