lista  = ["manzana","pera","uva","naranja","limón","melón","kiwi","fresa","mango"]
lista2 = ["limón","cereza","pera","kiwi","melocotón","uva","banano","ciruela","arándano"]
lista3 = ["sol","luna","estrella","nube","viento","lluvia","rayo","trueno","tormenta"]

repetir = True

print("Bienvenido a mi programa")
while repetir:
    print("******************************************************************")
    print("0. Salir")
    print("1. Añadir un dato al final de la lista")
    print("2. Añadir un dato en una posición concreta")
    print("3. Repetir la lista varias veces")
    print("4. Combinar dos listas (conservando o modificando la original)")
    print("5. Modificar un elemento por su índice")
    print("6. Eliminar por índice, por valor o por rango; vaciar la lista")
    print("7. Encontrar el índice de un elemento")
    print("8. Comprobar si un elemento está en la lista")
    print("9. Contar cuántas veces se repite un valor")
    print("10. Mostrar la lista ordenada sin modificarla")
    print("11. Mostrar la longitud de la lista")
    print("12. Iterar mostrando índices y valores")
    print("13. Iterar dos listas en paralelo mostrando pares")
    print("******************************************************************")

    eleccion = int(input("Dime lo que quieres hacer"))

    match eleccion:
        case 0:
            print("Saliendo....")
            print("Gracias por utilizar mi programa")
            repetir=False
        case 1:
            print("1. Para añadir un dato a las lista utilizamos la funcion append()")
            print(f"Esta es la lista que tenemos ahora {lista}")
            anadir = str(input("Dime la palabra que quieres añadir "))
            lista.append(anadir)
            print(f"Asi queda la lista despúes de ejecutar la función append() {lista}")

        case 2:
            print("2. Para añadir un dato en una posicion concreta se utiliza la función insert()")
            print(f"Esta es la lista que tenemos ahora {lista}")
            posicion = int(input("Dime la posicion en la que quieres añadir el numero "))
            anadir = str(input("Dime la palabra que quieres añadir "))
            posicion -= 1
            lista.insert(posicion,anadir)
            print(f"Esta es la lista que tenemos ahora despues de añadir el dato {lista}")

        case 3:
            print("3. Para repetir las lista el numero de veces que quieras se utiliza el operador *")
            numeroDeRepes = int(input("Dime el número de veces que quieres repetir la lista "))
            print(lista*numeroDeRepes)

        case 4:
            print("4. Para combinar dos listas hay dos maneras de hacerlo la primera es mediante el operador + o +=: esta lo que hace es que conserva la lista original"
                  " \ny la otra es con la función extend() que esta modifica la lista")
            print(f"Esta es la lista que tenemos ahora {lista}")
            lista += lista2
            print(f"Asi quedaria la lista si la combinamos con el operador +: {lista} solo en este momento ya que esta conserva la lista original")
            lista.extend(lista2)
            print(f"Y asi quedaria la lista si la combinamos con la funcion extend(): {lista} ahora la lista esta formada con las dos lista para siempre ya que modifica la lista original")

        case 5:
            print("5. Para modificar una lista se utiliza el indice de la lista")
            print(f"\nEsta es la lista que vamos a modificar {lista2}")
            modificarPorIndice = int(input("\nDime el indice del numero que quieres modificar "))
            modificarPorIndice -= 1
            nuevoValor = str(input("Dime el nuevo valor "))
            lista2[modificarPorIndice] = nuevoValor
            print(f"Asi queda la lista después de modificarlo mediante el índice {lista2}")

        case 6:
            print("6. Para eliminar un valor se puede hacer de muchas maneras"
                  "\n1. Mediante el indice\n2. Mediante el valor\n3. Mediante su rango")
            print(f"Esta es la lista {lista2}")
            delPorIndice = int(input("1. Dime el indice del valor que quieres eliminar "))
            delPorIndice -= 1
            del lista2[delPorIndice]
            print(f"Asi queda la lista {lista2}")
            delPorValor = str(input("2. Dime el valor que quieres eliminar "))
            lista2.remove(delPorValor)
            print(f"Asi queda la lista {lista2}")
            delPorRango1 = int(input("Dime desde que número quieres eliminar "))
            delPorRango2 = int(input("Dime hasta que número quieres eliminar "))
            lista2[delPorRango1:delPorRango2] = []
            print(f"Asi queda la lista {lista2}")
            print("Y para eliminar la lista entera se utiliza la función clear()")
            lista2.clear()

        case 7:
            print("7. Para encontrar un elemento se hace con la función index()")
            print(f"Esta es la lista {lista}")
            buscarValor = str(input("Dime el valor que quieres buscar "))
            print(f"Este es el indice del valor que has buscado {lista.index(buscarValor)}")

        case 8:
            print("8. Para saber si un elemento esta en la lista se utiliza la función in")
            print(f"Esta es la lista {lista}")
            saberSiEsta = str(input("Dime el elemento que quieres saber si esta o no "))
            if(saberSiEsta in lista):
                print(f"La palabra {saberSiEsta} si esta en la lista")
            else:
                print(f"La palabra {saberSiEsta} no esta en la lista")

        case 9:
            print(lista)
            print("9. Para saber cuántas veces se repite ese valor en la lista se utiliza la función .count()")
            contar = str(input("Dime el valor que quieres saber el número de veces que se repite "))
            print(f"Este es el número de veces que se repite el valor({contar} = {lista.count(contar)})")

        case 10:
            print("10. Para ordenar una lista se utiliza la función sorted() que esta solo la ordena y no la modifica, si la quieres modificar utilizas la función sort()")
            print(f"Lista ordenada {sorted(lista)}")
            lista.sort()

        case 11:
            print("11. Para saber la longitud de una lista se utiliza la función len()")
            print(f"Esta es la lista {lista}")
            print(f"La longitud de la lista es de {len(lista)}")

        case 12:
            print("12. Para iterar usando enumeracion se utiliza la función enumerate()")
            for i ,v in enumerate(lista):
                print(i,v)

        case 13:
            print("13. Para iterar sobre varias lista se utiliza la función zip()")
            for i, v in zip(lista, lista3):
                print(i,v)
        case _:
            print("Opción no válida.")