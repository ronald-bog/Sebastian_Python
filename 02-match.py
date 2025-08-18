# match
opcion = 'Andres'
opcionConv = opcion.lower()

match opcionConv:
    case 'andres':
        print('Elegiste la opcion A')
    case 'beto':
        print('Elegiste la opcion B')
    case 'carlos':
        print('Elegiste la opcion C')
    case 'danilo':
        print('Elegiste la opcion D')
    case _:
        print('Opcion no valida')


opcion = 10

match opcion:
    case 1:
        print('Uno')
    case 2:
        print('Dos')
    case 3:
        print('Tres')
    case _:
        print('Numero no Reconocido')


# Metodos de los string
