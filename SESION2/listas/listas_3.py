# Slice list[first_index : final_index : increment]

lista= [12, 15, 16, 18, 99, 10, 44, 55, 66, 77, 88, 123999, 12345,1345]
lista_2 = lista[:]

# lista_2 = lista.copy()
del lista_2[0]

lista_3 = lista[3:7]

lista_4 = lista[5:]

print(lista, lista_2, lista_3, lista_4, sep='\n')

print('\n')

for i in range(-1, -len(lista)-1, -1):
    print(lista[i])