# Manejo de archivos

#Abrir archivo
#file = open('./text.txt')

#leer un archivo
#print(file.read())

#leer archivo linea a linea
#print(file.readline())

#leer un archivo con un for
#for line in file:
#  print(line)

#cerrar el archivo
#file.close()

# Abrir y cerrar automaticamente el archivo
with open('./text.txt') as file:
  for line in file:
    print(line)
