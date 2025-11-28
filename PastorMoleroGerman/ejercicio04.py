# # 4. Escriba un programa que pida un número y dibuje dos cuadrados de ese número de estrellas en
# # diagonal, como muestran los ejemplos siguientes:
# Escriba un número entero positivo: 3
# * * *
# * * *
# * * *
#         * * *
#         * * *
#         * * *
#  Escriba un número entero positivo: 4
# * * * *
# * * * *
# * * * *
# * * * *
#         * * * *
#         * * * *
#         * * * *
#         * * * *

def cuadrados(numero):
    for i in range(numero):
        print("* " * numero)
    for j in range(numero):
        print("  " * numero + "* " * numero)


numero = int(input("Introduca un número positivo"))

print(cuadrados(numero))

