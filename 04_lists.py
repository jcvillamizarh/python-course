numbers = []
for element in range(1, 11):
  numbers.append(element)

print(numbers)

numbers_v2 = [element for element in range(1, 11)]
print(numbers_v2)

pairs = []

for i in range(1, 11):
  if i % 2 == 0:
    pairs.append(i * 2)

print(pairs)

pairs_v2 = [i for i in range(1, 11) if i % 2 == 0]
print(pairs_v2)