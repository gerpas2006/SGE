# 5. Escriba un programa que pida dos números (m y n) y que escriba n segmentos de m estrellas
# separados por m espacios, como muestran los ejemplos siguientes:
# Escriba el tamaño del segmento: 4
# Escriba el número de segmentos: 3
# * * * *  * * * *  * * * *

def estrellas(m, n):
    print(("* " * m + "  ") * n)


m = int(input("Dime el tamaño del segmento"))
n = int(input("Dime el número de segmentos"))

estrellas(m, n)