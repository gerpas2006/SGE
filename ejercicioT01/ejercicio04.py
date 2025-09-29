numero1 = input("Dime el primer número ")
numero2 = input("Dime el segundo numero ")
if numero1>numero2:
    print(f"{numero1} es mayor que {numero2}")
elif numero2>numero1:
    print(f"{numero2} es mayor que {numero1}")
else:
    print("Los dos numeros son iguales")