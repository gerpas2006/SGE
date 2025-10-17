lista = [1,2,3,4,5,6,7,8,9]
lista2 = [1,3,4,6,7,9,2,5,8]

print("Voy a explicar funcionalidades en listas en Python")
print("1. Para añadir un dato a las lista utilizamos la funcion append()")
print(f"Esta es la lista que tenemos ahora {lista}")
anadir = int(input("Dime el número que quieres añadir "))
lista.append(anadir)
print(f"Asi queda la lista despúes de ejecutar la función append() {lista}")
print("\n2. Para añadir un dato en una posicion concreta se utiliza la función insert()")
print(f"Esta es la lista que tenemos ahora {lista}")
posicion = int(input("Dime la posicion en la que quieres añadir el numero "))
anadir = int(input("Dime el número que quieres añadir "))
posicion-=1
lista.insert(posicion,anadir)
print(f"Esta es la lista que tenemos ahora despues de añadir el dato {lista}")
print("\n3. Para repetir las lista el numero de veces que quieras se utiliza el operador *")
numeroDeRepes = int(input("Dime el número de veces que quieres repetir la lista "))
print(lista*numeroDeRepes)
print("\n4. Para combinar dos listas hay dos maneras de hacerlo la primera es mediante el operador + o +=: esta lo que hace es que conserva la lista original"
" \ny la otra es con la función extend() que esta modifica la lista")
lista += lista2
print(f"Asi quedaria la lista si la combinamos con el operador +: {lista} solo en este momento ya que esta conserva la lista original")
lista.extend(lista2)
print(f"Y asi quedaria la lista si la combinamos con la funcion extend(): {lista} ahora la lista esta formada con las dos lista para siempre ya que modifica la lista original")
print("\n5. Para modificar una lista se utiliza el indice de la lista")
print(f"\nEsta es la lista que vamos a modificar {lista2}")
modificarPorIndice = int(input("\nDime el indice del numero que quieres modificar "))
modificarPorIndice-=1
nuevoValor = int(input("Dime el nuevo valor "))
lista2[modificarPorIndice] = nuevoValor
print(f"Asi queda la lista después de modificarlo mediante el índice {lista2}")
print("\n6. Para eliminar un valor se puede hacer de muchas maneras" \
"\n1. Mediante el indice\n2. Mediante el valor\n3. Mediante su rango\n4. Mediante su índice (con extracción):")
print(f"Esta es la lista {lista2}")
delPorIndice = int(input("1. Dime el indice del valor que quieres eliminar "))
delPorIndice-=1
del lista2[delPorIndice]
print(f"Asi queda la lista {lista2}")

