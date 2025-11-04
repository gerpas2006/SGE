#7. Escriba un programa que permita crear una lista de palabras y que, a continuación, 
#pida una palabra y elimine esa palabra de la lista. 

palabras = ["Pedro", "Raúl","Antonio"]

print(f"Esta es la lista de palabras {palabras}")
eliminar = str(input("Dime que la palabra de la lista quieres eliminar"))

for i in palabras:
    if i == eliminar:
        palabras.remove(eliminar)
if eliminar not in palabras:
        print("No se a encontrado la palabra")

print(f"Asi queda la lista {palabras}")