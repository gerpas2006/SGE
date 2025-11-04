#12. Escriba un programa que permita crear una lista de palabras y que, a continuación, ordene la lista por
#orden alfabético.

listPalabras = []

numero = int(input("Dime cuántas palabras quieres añadir "))

for i in range (numero):
    palabra = str(input("Dime la primera palabra "))
    listPalabras.append(palabra)

print(f"Esta es la lista ordenada alfabeticamente {sorted(listPalabras)}")