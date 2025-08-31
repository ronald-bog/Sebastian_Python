'''
#! Agosto 29 2025

1. Escribe un programa que lea 5 números enteros e imprima cuántos de ellos son positivos.

contador = 0

for i in range(5):
    numero = int(input('introduce un número entero:' ))
    if numero > 0:
        contador += 1


2.  Escribe un programa que sume todos los números pares del 1 al 10 e imprima el resultado.


suma_pares = 0
for i in range (11):
    if numero %2 == 0
       suma_pares += numero
print('la suma de los números pares del 1 al 10 es', suma_pares)


3. Escribe un programa que elija un número secreto entre 1 y 5. El usuario debe intentar adivinarlo. Si acierta, mostrar "¡Correcto!"; si no, "Sigue intentando".
?
import random

numero_secreto = random.randint(1, 5)
intento = int(input("Adivina el número secreto entre 1 y 5: "))

if intento == numero_secreto:
    print("¡Correcto!")
else:
    print("Sigue intentando")

