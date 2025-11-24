# 3. Haz un programa que copie el contenido de un fichero 
# llamado 'origen.txt' en otro llamado 'copia.txt'. 
import shutil

origen = open('ejercicio03/origen.txt')
copia = open('ejercicio03/copia.txt', 'w')

for i in origen:
    copia.write(i)

origen.close()
copia.close()


