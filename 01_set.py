'''
Conjuntos - SET
 - Se pueden modificar
 - No tienen un orden
 - No permite duplicados
'''

set_countries = {'col', 'mex', 'bol'}
print(set_countries)
print(type(set_countries))

set_types = {1, 'hola', False, 12.12}
print(set_types)

set_from_string = set('hola')
print(set_from_string)

set_from_tuple = set(('abc', 'cbd', 'as', 'abc'))
print(set_from_tuple)

numbers = [1, 2, 3, 1, 2, 3, 4]
set_from_list = set(numbers)
print(set_from_list)
unique_numbers = list(set_from_list)
print(unique_numbers)