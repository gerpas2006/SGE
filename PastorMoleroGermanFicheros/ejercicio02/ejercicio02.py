# 2. Crea un programa que añada la fecha y hora actuales al 
# final de un fichero. 
from datetime import datetime

escribirFichero = open('ejercicio02/fecha.txt', 'a')

fechaActual = datetime.now()

escribirFichero.write(str(fechaActual) + '\n')

escribirFichero.close()

leerFichero = open('ejercicio02/fecha.txt', 'r')

print(leerFichero.read())

leerFichero.close()

