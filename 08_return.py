# Function with return

def sum_with_range(min, max):
  sum = 0
  for x in range(min, max):
    sum += x
  return sum  

sum_with_range(1, 10)

result_2 = sum_with_range(1, 5)
print(result_2)

