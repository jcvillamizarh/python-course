# Función reduce()
# reduce(lambda )
import functools


def accum(counter, item):
  print('counter => ', counter)
  print('item=> ', item)
  return counter + item


numbers = [1, 2, 3, 4]
result = functools.reduce(accum, numbers)

#reduce con lambda
result_2 = functools.reduce(lambda counter, item: counter + item, numbers)

print(result)
print(result_2)
