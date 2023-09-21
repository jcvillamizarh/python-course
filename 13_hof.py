#Higher order functions

def increment(x) : 
  return x + 1

incremen_v2 =lambda x : x + 1

def higher_order_function(x, func) :
  return x + func(x)

h_o_f_2 = lambda x, func : x + func(x)

result = higher_order_function(2, increment)
# 2 + (2+1)
print(result)

result = h_o_f_2(2, incremen_v2)
print(result)