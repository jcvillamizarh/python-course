#Errores en Python

#Division por cero
#print(2 / 0)

# AssertionError

suma = lambda x, y: x + y

assert suma(2, 2) == 4

age = 10

# Lanzar una excepcion
if age < 18:
  raise Exception('Minors are not allowed')

