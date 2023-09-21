# Function with arguments and parameters by default
# And returning multiple results

def find_volume(length=1, width = 1, depth = 1):
  return length * width * depth, width, 'hola'

result, width, text = find_volume(width=2)
print(result)
print(width)
print(text)