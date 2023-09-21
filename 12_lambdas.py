'''
lambdas
def func(args) : retur_val
is equivalent to:
lambda args : return_:value
'''

def increment(x):
  return x + 1
result = increment(10)
print(result)

#lambda function

increment_v2 = lambda x: x + 1

result_2 = increment_v2(2)
print(result_2)

#lambda function 2

full_name = lambda name, last_name : f'Full name is {name.title()} {last_name.title()}'

text = full_name('juan', 'villamizar')
print(text)