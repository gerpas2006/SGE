# . Dada la tupla temperaturas = (21, 24, 19, 30, 25, 28). Crear el código necesario para:
# 1. Mostrar el valor máximo y mínimo.
# 2. Calcular la temperatura media.
# 3. Convertir la tupla en lista, añadir una nueva temperatura y volver a convertir a tupla.
# 4. Comprobar si 30 está presente

temperaturas = (21, 24, 19, 30, 25, 28)
repetir = True

while repetir:
    eleccion = int(input("\n0. Salir\n1. Temperaturaa max y min\n2. Temperatura media\n3. Añadir nueva temperatura\n4. El 30 esta  presente?\n"))
    match eleccion:
        case 0:
            print("Saliendo...")
            repetir=False
        case 1:
            print(f"La temperatura maxima regiustrada es {max(temperaturas)} y la minima es {min(temperaturas)}")
        case 2:
            media = sum(temperaturas)/len(temperaturas)
            print(f"La temperatura media es {media}")
        case 3:
            agregar = float(input("Dime la nueva temperatura que quieres agregar"))
            listaTupla = list(temperaturas)
            listaTupla.append(agregar)
            temperaturas = tuple(listaTupla)
            print(temperaturas)
        case 4:
            if 30 in temperaturas:
                print("El 30 si esta presente en las temperaturas registradas")
            else:
                print("El 30 no esta presente en las temperaturas registradas")
        case _:
            print("Elige una opcion correcta")
            
