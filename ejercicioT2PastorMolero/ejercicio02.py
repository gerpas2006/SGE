#Creame una lista vacia y rellenala con todos los múltiplos de 3 que hay hasta el número que diga el usuario
multiplos3 = []
numero = int(input("Dime hasta qué número quieres que te diga los múltiplos de 3: "))

for i in range(numero + 1):
    if i % 3 == 0:
        multiplos3.append(i)

print("Estos son todos los múltiplos de 3 hasta", numero, ":")
print(multiplos3)
