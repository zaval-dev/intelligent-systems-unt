def enter_number():
    list = [1,2,3,4,5,6]
    while True:
        try:
            number = int(input('Selecciona una opción(1/2/3/4/5/6): '))
            if number not in list:
                print('El número no está dentro de los parámetros, vuelve a intentar...')
                continue
            return number
        except:
            print('Digite un número ENTERO válido...')

while True:
    option = enter_number()
    if option == 1:
        print('Esta es la opción 1:')
    elif option == 2:
        print('Esta es la opción 2:')
    elif option == 3:
        print('Esta es la opción 3:')
    elif option == 4:
        print('Esta es la opción 4:')
    elif option == 5:
        print('Esta es la opción 5:')
    elif option == 6:
        print('Esta es la opción para salir:')
        break