# Para abrir un fichero se utiliza esta linea
fichero = open('temps.txt', 'r')
print("Todo el fichero")
print(fichero.read())

# Para ver de linea en linea el fichero
fichero.seek(0)
linea1= fichero.readline()
print("Primera línea del fichero")
print(linea1)
# Para ir leyendo línea a línea
print("Para leer de línea e línea")
fichero.seek(0)
for linea in fichero:
    print(linea,end='')


# Para mostrar el fichero en forma de lista
fichero.seek(0)
lineas = fichero.readlines()
print("\nContenido del fichero leído con readLines():")
for linea in lineas:
    print(linea, end='')
fichero.close()



