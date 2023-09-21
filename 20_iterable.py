# Iterable : es un objeto que contiene un número de valores contables
# Un iterador es un objeto sobre el que puede iterar, 

my_iter = iter(range(1, 4))

print(my_iter)
#Iterar uno a uno
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
