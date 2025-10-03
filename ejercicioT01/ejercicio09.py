numeroDeVeces= int(input("Dime las veces que quieres repetir la palabra"))
palabra = str(input(f"Dime la palabra que quieres repetir {numeroDeVeces}"))
contador=0
while contador<numeroDeVeces:
    print(palabra)
    contador+=1