# Github: sebastianblancolopez@gmail.com

# if - elif -else

color = 'lila'
if color == 'Rojo':
    print("El color es Rojo")
elif color == 'Verde':
    print("El color es Verde")
elif color == 'Amarillo':
    print("El color es Amarillo")
else:
    print("Es otro color")

# Expresion ternaria (if-else)

if 5 > 4:
    print('El 5 es mayor')
else:
    print('El 5 no es mayor')

print('El 5 es mayor' if 5 > 4 else 'El 5 no es mayor')

# js: 5 > 4 ? 'El 5 es mayor':'El 5 no es mayor'

# caso especial

planeta = "Tierra"
if planeta == "Tierra":
    print('Es planeta es la tierra')
if planeta == "marte":
    print('Es planeta es la marte')
elif planeta == "Jupiter":
    print('Es planeta es la Jupiter')
else:
    print('Es planeta es la Venus')

# if anidado

miVariable = 'framework'  # 'lenguaje'
dato = 'React'

if miVariable == "lenguaje":
    if dato == "Python":
        print('El lenguaje es Python')
    else:
        print('No corresponde')
elif miVariable == 'framework':
    if dato == "React":
        print('El frame es React')
    else:
        print('No corresponde')
