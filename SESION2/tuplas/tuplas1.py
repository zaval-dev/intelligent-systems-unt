# Tupla_ ESta compuesta por elementos de disintito tipo
# ES una secuencia inmutable
# Se declara con ()

alumno = ('alu001', 'José Carlos', 'López Ravelio', 18, 65.8)
print(alumno)

for data in alumno:
    print(data)

print('\n')

for i in range(len(alumno)):
    print(alumno[i])

print(alumno.count(18))
print(alumno.index(18))

print('\n')

a, b, c = 1, 2, 3
w = 'unt', 'sistemas', 'Facultad de Ingeniería'
print(type(w))