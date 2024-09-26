# Tipo de datos lista
# Es una secuencia de valores de distinto tipo
# Cada valor tiene una posicion que comienza con 0
# El índice del primer valor es 0, del segundo, 1 y así sucesivamente
# Comienza con [], los valores separados por comas

list = [12, 20, True, False, 'Juan', [29,45], 67.90]
print(list)

# Recorrido de la lista
for element in list:
    print(element)

# len(list) --> Devuelve el número de elementos de una lista
print('\n')
for i in range(len(list)):
    print(list[i])

# EL operador not in devuelve verdadero si el elemento no está en la lista
print('\n')
print(12 in list)
