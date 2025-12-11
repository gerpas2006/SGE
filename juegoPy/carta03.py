
def listaMasLarga(lista1,lista2):
    contadorLista1 = 0
    contadorLista2 = 0
    for i in lista1:
        contadorLista1+=1
    for i in lista2:
        contadorLista2+=1
    if contadorLista2>contadorLista1:
        print("La lista 2 es mas grande que la 1")
    elif contadorLista1>contadorLista2:
        print("La lista 1 es más grande que la lista 2")
    else:
        print("Las dos lista tienen el mismo tamaño")



lista1 = [1,2,3]
lista2 = [1,2,3]

listaMasLarga(lista1,lista2)