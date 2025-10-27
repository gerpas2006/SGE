#4. Escriba un programa que permita crear una lista de palabras. Para ello, el programa tiene que pedir 
#un número y luego solicitar ese número de palabras para crear la lista.
#Por último, el programa tiene que escribir la lista. 

palabras =[]

numeroDePalabras= int(input("Dime cuantas palabras quieres añadir "))
for i in range(numeroDePalabras):
    agregarPalabra = str(input(f"Dime la {i+1} palabra que quieres añadir "))
    palabras.append(agregarPalabra)
print(f"Estas son todas las palabras {palabras}")