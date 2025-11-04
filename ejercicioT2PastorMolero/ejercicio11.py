#11. Escriba un programa que permita crear dos listas de palabras y que, a continuación, escriba las siguientes listas (en las que no debe haber repeticiones): 
#Lista de palabras que aparecen en las dos listas. 
#Lista de palabras que aparecen en la primera lista, pero no en la segunda. 
#Lista de palabras que aparecen en la segunda lista, pero no en la primera. 
#Lista de palabras que aparecen en ambas listas.


listPalabras1 = []
listPalabras2 = []
repetir = []
noRepetidosLista1 = []
noRepetidosLista2 = []
todas = []

numeroDePalabras = int(input("Dime cuántas palabras quieres añadir en las listas "))

for i in range (numeroDePalabras):
    agregar = str(input("Dime el valor que quieres añadir "))
    listPalabras1.append(agregar)

for i in range (numeroDePalabras):
    agregar = str(input("Dime el valor que quieres añadir "))
    listPalabras2.append(agregar)

for i in listPalabras1:
    for j in listPalabras2:
        if j == i:
            repetir.append(j)

print(f"Estas son las plabras que se repiten en las dos listas {repetir}")

for i in listPalabras1:
    if i not in listPalabras2:
        noRepetidosLista1.append(i) 

print(f"Estos son los valores que no se repiten de la lista 1 {noRepetidosLista1}")

for i in listPalabras2:
    if i not in listPalabras1:
        noRepetidosLista2.append(i) 
        
print(f"Estos son los valores que no se repiten de la lista 1 {noRepetidosLista2}")

for i in listPalabras1:
    if i not in todas:
        todas.append(i)

for j in listPalabras2:
    if j not in todas:
        todas.append(j)

print(f"Estos son los valores de las dos listas sin repeticiones {todas}")









        

