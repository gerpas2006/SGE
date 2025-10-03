objetivo = int(input("Introduce un número: "))
list = []
suma=0
while suma != objetivo:
    num= int(input("Dame un número"))
    list.append(num)
    suma+=num
    if suma>objetivo:
        print("La suma de los numeros que has puesto se pasan ya del objetivo. Has perdidoooo!!!!")
        suma=objetivo

print(f"Estos han sido todos los número que has dicho {list}")

