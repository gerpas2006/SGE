import random;
numAleatorio=int(random.randint(0,10))
numElegido=int(0)
contador=int(1)
while numElegido==numAleatorio or contador<=3:
    numElegido=int(input("Dime el numero que crees que ha salido "))
    if numAleatorio==numElegido:
        print("Has adivinado el numero")
        break
    contador+=1
print(f"El número generado era el {numAleatorio}")


