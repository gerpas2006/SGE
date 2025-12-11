# Saber si la suma de la lista sale par o impar

def sumarPares(listaNumeros):
    sumaLista = sum(listaNumeros)
    if sumaLista%2 == 0:
        print("La suma de la lista sale par")
    else:
        print("La suma de la lista es impar")

listaNumeros = [1,2,3,4,5,6,7,8,9]

sumarPares(listaNumeros)

