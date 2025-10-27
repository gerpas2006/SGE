#5. Escriba un programa que permita crear una lista de palabras y que, a continuación, 
#pida una palabra y diga cuántas veces aparece esa palabra en la lista. 

palabras = []

numeroDePalabras= int(input("Dime cuantas palabras quieres añadir "))
for i in range(numeroDePalabras):
    agregarPalabra = str(input(f"Dime la {i+1} palabra que quieres añadir "))
    palabras.append(agregarPalabra)
print(f"Estas son todas las palabras {palabras}")

buscarPalabra = str(input("Dime la palabra que quieres saber cuántas veces se repite "))
print(f"La palabra {buscarPalabra} aparace {palabras.count(buscarPalabra)} veces")