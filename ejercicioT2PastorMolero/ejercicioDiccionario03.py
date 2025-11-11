# 4. Si tenemos un diccionario para un inventario de un frutero inteligente, por ejemplo, inventario =
# {"manzanas": 10, "naranjas": 5, "peras": 8}
# Crear los siguientes apartados:
# 1. Mostrar todas las claves y valores.
# 2. Aumentar manzanas en 5.
# 3. Eliminar peras.
# 4. Calcular el total de frutas.

inventario = {"manzanas": 10,
            "naranjas": 5, 
            "peras": 8}

repetir = True

while repetir:
    eleccion = int(input("0. Salir\n1. Mostrar Claves y valores\n2. Aumentar manzanas 5\n3. Eliminar las peras\n4. Total de frutas"))
    match eleccion:
        case 0:
            print("Saliendo....")
            repetir = False
        case 1:
            for clave,valor in inventario.items():
                print(f"Frutas: {clave}, Cant: {valor}")
        case 2:
            inventario["manzanas"] = 10+5
        case 3:
            del inventario["peras"]
        case 4:
            suma = 0
            for i in inventario.values():
                suma+=i
            print(f"La suma de todas las frutas es {suma}") 
        case _:
            print("Elige una opción correcta")