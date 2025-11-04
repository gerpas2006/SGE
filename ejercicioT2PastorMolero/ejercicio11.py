#11. Escriba un programa que permita crear dos listas de palabras y que, a continuación, escriba las siguientes listas (en las que no debe haber repeticiones): 
#Lista de palabras que aparecen en las dos listas. 
#Lista de palabras que aparecen en la primera lista, pero no en la segunda. 
#Lista de palabras que aparecen en la segunda lista, pero no en la primera. 
#Lista de palabras que aparecen en ambas listas.


listPalabras1 = []
listPalabras2 = []
repetir = []

numeroDePalabras = int(input("Dime cuántas palabras quieres añadir en las listas "))

for i in range (numeroDePalabras):
    agregar = str(input("Dime el valor que quieres añadir "))
    listPalabras1.append(agregar)

for i in range (numeroDePalabras):
    agregar = str(input("Dime el valor que quieres añadir "))
    listPalabras2.append

for i in listPalabras1:
    for j in listPalabras2:
        if j == i:
            repetir.append(i)

print(f"{repetir}")
        

