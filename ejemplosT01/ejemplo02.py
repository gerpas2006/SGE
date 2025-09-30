ano=int(input("Introsuce el año que quieres saber si es bisiesto "))
if (ano % 4 ==0 and ano % 100!=0) or ano % 400==0:
    print("Es bisiesto")
else:
    print("No es bisiesto")