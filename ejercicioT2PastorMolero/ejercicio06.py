#6. Escriba un programa que permita crear una lista de palabras y que, a continuación, 
#pida dos palabras y sustituya la primera por la segunda en la lista. 

palabras  = ["Rojo","Azul","Blanco"]

print(f"Lista original {palabras}")

palabra_vieja = str(input("Palabra a sustituir "))
palabra_nueva = str(input("Nueva palabra "))

for i in range (len(palabras)):
    if palabras[i]==palabra_vieja:
        palabras[i]=palabra_nueva

print(f"Lista modificada {palabras}")
