objetivo = int(input("Introduce un número: ")) 
list = [] 
suma=0 
while suma != objetivo: 
        num= int(input("Dame un número ")) 
        suma+=num 
        if suma>objetivo: 
            print("La suma de los numeros que has puesto se pasan ya del objetivo.Te voy a restar el último numero que has puesto") 
            suma-=num 
        else:
            list.append(num) 


print(f"Estos han sido todos los número que has dicho {list}")