# Modules

# Sistema operativo
import sys

print(sys.path)

import re

text = 'Mi numero es 311 1232 123123, el codigo del pais es 57, mu numero de la suerte es el 7'
# Expresión regular para buscar número en más de una ocasión
result = re.findall('[0-9]+', text)
print(result)

#Manejo de fechas
import time

timestamp = time.time()
localTime = time.localtime()
formattedDate = time.asctime(localTime)
print(formattedDate)

#Colecciones
import collections
numbers = [1,2,1,2,2,2,3,4,4,5,6,7]
counter = collections.Counter(numbers)
print(counter)

