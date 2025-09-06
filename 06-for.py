''' FOR '''

'''
SINTAXIS:

for variable in secuencia(coleccion):
     bloque de codigo a repetir
'''

planeta = "Saturno y Jupiter"
lenguajesProgramacion = ['Python', 'Javascript', 'Java', 'C++']

""" for i in planeta:
    print(i)

# range()

for numero in range(6):
    print(numero)

for num in range(39, 54):
    print(num)

for fulanito in range(31, 55, 5): # 31 36 41 46 51
    print(fulanito) """

for letra in range(0, 18, 2):
    print(planeta[letra])

# Control de flujo del bucle (loop)

# Break (break)

for x in range(5):
    if x == 3:
        break
    print(x)


# Continue (continue)

for z in range(9):
    if z == 5:
        continue
    print(z)


# ENUMERATE: obtiene index y elem de una coleccion

saludo = "Hello"
for index, element in enumerate(saludo):
    print(f'El indice es: {index} y el elemento es: {element}')

saludo2 = "Hello"
for idx, e in enumerate(saludo2):
    print(f'El indice es: {idx} y el elemento es: {e}')

saludo3 = "Hello"  # Ejemplo cambiando el orden logico del indice
for idx, e in enumerate(saludo3):
    print(f'El item: {idx + 1} es el elemento: {e}')

# ZIP: Nos permite obtener el elemento de dos colecciones

ciudad = "Medellin"
estrella = "Sirio"

for e1, e2 in zip(estrella, ciudad):
    print(e1, e2)

# REVERSE(reversed): Itera en orden inverso

galaxia = "Andromeda"

for l in reversed(galaxia):
    print(l)


# SORTED: Devuelve el iterable ordenado

desordenado = "ypand"

for letra in sorted(desordenado):
    print(letra)
