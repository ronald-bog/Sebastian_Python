# Truthy y Falsy
''' Concepto que especifica como se evalua un valor o estructura dentro de un contexto Booleano '''

# Valores Truthy, todo lo que no esta especificado aqui es por ende un Truthy.
print(bool(0))
print(bool(""))
print(bool(False))
print(bool([]))
print(bool({}))
print(bool(None))
print(bool(()))
print(bool(set()))

if "palabra":
    print('el IF es True')
