# Manejo de errores

try:
  print(0 / 0)
except ZeroDivisionError as error:
  print(error)

try:
  assert 1 != 1, 'Uno no es igual que uno'
except AssertionError as error:
  print(error)

try:
  age = 10
  if age < 18:
    raise Exception('Minors are not allowed')
except Exception as error:
  print(error)

# validación en un solo bloque

try:
  print(0 / 0)
  assert 1 != 1, 'Uno no es igual que uno'
  age = 10
  if age < 18:
    raise Exception('Minors are not allowed')
except ZeroDivisionError as error:
  print(error)
except AssertionError as error:
  print(error)
except Exception as error:
  print(error)
