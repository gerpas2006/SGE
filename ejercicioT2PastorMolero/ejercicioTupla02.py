# 2. Dada la tupla productos = ("pan", "leche", "huevos", "queso")
# 1. Mostrar el primer y último elemento.
# 2. Contar cuántas veces aparece un producto (elige uno).
# 3. Convertir a lista, modificar un elemento y volver a tupla.
# 4. Añadir un nuevo producto (tupla concatenada).


productos = ("pan", "leche", "huevos", "queso")
repetir = True

while repetir:
    eleccion = int(input("0. Salir\n1. Mostrar el primer y ultimo producto\n2. Contar cúantas veces sale el producto que me digas\n3. Modificar un producto\n4. Añadir un nuevo producto"))
    match eleccion:
        case 0:
            print("Saliendo....")
            repetir=False
        case 1:
            print(f"El primer producto que esta en la tupla es {productos[0]} y el último es {productos[-1]}")
        case 2:
            contador = 0
            buscar = str(input("Dime que palabra quieres buscar")) 
            for i in productos:
                if i == buscar:
                    contador+=1
            print(f"El producto {buscar} esta {contador} veces")
        case 3:
            indice = int(input("Dime el indice del producto"))
            indice -=1
            nuevoProducto = str(input("Dime el nuevo producto"))
            listaProducto = list(productos)
            listaProducto[indice] = nuevoProducto
            productos = tuple(listaProducto)
            print(productos)
        case 4:
            nuevaLista = []
            agregar = str(input("Dime el nuevo producto"))
            nuevaLista.append(agregar)
            nuevaTupla = tuple(nuevaLista)
            print(nuevaTupla+productos)
        case _:
            print("Elige una opción correcta")

