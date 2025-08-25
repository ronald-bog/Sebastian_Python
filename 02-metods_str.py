# Metodos de los Strings (str)

palabra = "Hola Mundo"

# Acceso a un carcater por medio del indice
print(palabra[5])

# Medir longitud (cantidad de elementos) de un string y otras colecciones
print(len(palabra))

# lower()
print(palabra.lower())

# upper()
print(palabra.upper())

# capitalize
nombre = 'sebastian'
print(nombre.capitalize())

# split
planeta = 'Saturno-Venus-Urano'
print(planeta.split())
print(planeta.split('-'))

# replace
saludo = 'hola Sebastian'
print(saludo.replace("Sebastian", "Andres"))
