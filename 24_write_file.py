# Escribir en archivos y permisos de lectura y escritura
# r+ lectura y escritura
# w+ permite leer pero sobreescribe el contenido del archivo
with open('./text.txt', 'r+') as file:
  for line in file:
    print(line)
  file.write('continua una nueva linea\n')
  file.write('nueva linea\n')
  file.write('nueva linea 2\n')