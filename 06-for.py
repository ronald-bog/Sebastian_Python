''' FOR '''

'''
SINTAXIS:

for variable in secuencia(coleccion):
     bloque de codigo a repetir
'''

planeta = "Saturno y Jupiter"
lenguajesProgramacion = ['Python', 'Javascript', 'Java', 'C++']

for i in lenguajesProgramacion:
    print(i)

# range()

for numero in range(6):
    print(numero)

for num in range(2, 9):
    print(num)

for fulanito in range(3, 15, 4):
    print(fulanito)

for letra in range(0, 18, 2):
    print(planeta[letra])

# Control de flujo del bucle (loop)

# Break (break)

for x in range(5):
    if x == 5:
        break
    print(x)


# Continue (continue)

for z in range(9):
    if z == 5:
        continue
    print(z)
