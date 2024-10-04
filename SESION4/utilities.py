def enter_number(domain_list, input_message='Selecciona una opción: ', except_message='Digite un número ENTERO válido...'):
    while True:
        try:
            number = int(input(input_message))
            if domain_list:
                if number not in domain_list:
                    print('El número no está dentro de los parámetros, vuelve a intentar...')
                    continue
            return number
        except ValueError:
            print(except_message)