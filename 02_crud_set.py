# CRUD en SET
'''
add(): Añade un elemento.

update(): Añade cualquier tipo de objeto iterable como: listas, tuplas.

discard(): Elimina un elemento y si ya existe no lanza ningún error.

remove(): Elimina un elemento y si este no existe lanza el error “keyError”.

pop(): Nos devuelve un elemento aleatorio y lo elimina y si el conjunto está vacío lanza el error “key error”.

clear(): Elimina todo el contenido del conjunto.
'''

set_countries = {'col', 'mex', 'bol'}

size = len(set_countries)
print(size)

print('col' in set_countries)
print('pe' in set_countries)

# add
set_countries.add('pe')
print(set_countries)

# Update
set_countries.update({'ar', 'ecua', 'pe'})
print(set_countries)

# remove
set_countries.remove('ar')
print(set_countries)

# discard
set_countries.discard('arg')
print(set_countries)

# clear
set_countries.clear()
print(set_countries)
