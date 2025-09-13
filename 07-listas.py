# lista

# creacion de una lista

numeros = [20, 5, 8, 9, 48]

# print(numeros[5])  # esto genera error
print(numeros[2])  # esto imprime el 8
numeros[3] = 100  # Cambiamos el elemento de la lista segun su indice

print(numeros)

# Metodos de las listas

# longitud de una lista, len()
print(len(numeros))

# append(): Agregar elementos al final de una lista

numeros.append(100)

print(numeros)

# extend:
listaA = [8, 10]
listaB = [56, 65]
listaA.extend(listaB)
print(listaA)

# insert :
list1 = [60, 20, 55]
list1.insert(2, 2000)
print(list1)

# remove
miLista = ['sol', 'luna', 'marte', 'luna', 'jupiter']
miLista.remove('luna')
print(miLista)

# pop: elimina el ultimo elemento
misPlanetas = ['tierra', 'saturno', 'marte', 'urano', 'jupiter']
# misPlanetas.pop()
devuelto = misPlanetas.pop(1)

print(misPlanetas)
print('---------------------')
print(devuelto)

# index: Devuelve el indice del primer elemento cuyo valor es igual al elemento pasado como argumento

numbers = [10, 20, 30, 40, 30]
# print(numbers.index(30))
# print(numbers)

# count:
veces = numbers.count(30)
print(veces)

nombres = ['Lina', 'Sebas', 'Roger', 'Andres', 'Andres', 'Ronald', 'Andres']

print(nombres.count('Andres'))

# sort: por defecto ordena en ascendente
nums = [54, 6, 8, 778, 10]
# nums.sort()
nums.sort(reverse=True)  # descendente
print(nums)

print(nums[0])

# copy

valores = [54, 6, 8, 778, 10]

newValores = valores.copy()

print(valores)
print(newValores)

# clear
estudiantes = ['Lina', 'Sebas', 'Roger',
               'Andres', 'Andres', 'Ronald', 'Andres']
print(estudiantes)
estudiantes.clear()
print(estudiantes)
