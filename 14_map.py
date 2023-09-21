# Map Ejecuta una función específica para cada elemento
# en un iterable y el elemento de envía a la función como un
# parámetro

numbers = [1, 2, 3, 4]
numbers_v2 = []

for i in numbers:
  numbers_v2.append(i * 2)

print(numbers)
print(numbers_v2)

#uso de lambdas y map

numbers_v3 = list(map(lambda i: i * 2, numbers))
print(numbers_v3)

numbers_1 = [1, 2, 3, 4]
numbers_2 = [5, 6, 7, 5]

result = list(map(lambda x, y: x + y, numbers_1, numbers_2))

print(result)
