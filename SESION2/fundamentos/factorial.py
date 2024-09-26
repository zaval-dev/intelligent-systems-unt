def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

def calcular(a, b=5, c=6):
    return a+b+c

# print('El factorial de 3 es:', factorial(4))
suma = calcular(4)
print('La suma es:', suma)