import Chapter1 as ch1
import utilities as util
            
while True:
    option = util.enter_number([1,2,3,4,5,6])
    if option == 1:
        print('Esta es la opción 1:')
        ch1.main_file_2()
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