# Estoy dando clases de inglés para el B2 y me gustaría que me ayudarais a crear un diccionario para ver cómo se dicen palabras con significado “raro” españolas en inglés. 
# Se hará todo en el mismo archivo, no se crean clases. Por ejemplo, “Cabeza: (en el sur de España) amigo/colega”, aro: sí, de acuerdo. 
# Consideraremos que no se repiten palabras con el mismo nombre, es decir, que la palabra “take” no aparece dos veces en el diccionario y que, 
# si tiene varios significados, estos pueden ir en el mismo String “significado”, por ejemplo, for---->por, para, durante. Se debe utilizar un diccionario 
# que se puede instanciar con algunos elementos de inicio y un menú para cada uno de las siguientes funcionalidades: 

# • Agregar una nueva palabra por teclado. 
# • Imprimir el diccionario completo “en bonito”. 
# • Buscar una palabra por nombre y mostrar su significado evitando que salta un error si la palabra no se encuentra.  
# • Modificar una palabra, modificando únicamente el significado de esta por otro nuevo, leído por teclado. 
# • Pedir al usuario sus dos palabras favoritas con los significados y combinar este con el ya creado modificando el original. 
# • Borrar una palabra (ustedes decidís la mejor forma). 
# • Ordenar el diccionario por orden alfabético. 

palabras = {
    'cabeza' : 'amigo/colega',
    'aro': 'sí,de acuerdo'
}
repetir = True

while repetir:
    eleccion = int(input("Dime que quieres hacer\n0. Salir \n1.Agregar una palabra al diccionario\n2. Modificar una palabra del diccionario\n3. Buscar una palabra en el diccionario" \
    "\n4. Combinar dos palabras que tu quieras\n5. Borrar una palabra\n6. Ordenar el diccionario\n7 Imprimir el diccionario "))

    match eleccion:
        case 0:
            print("Saliendo......")
            print("Gracias por utilizar mi programa")
            repetir=False
        case 1:
            clave = str(input("Dime como quieres llamar a la palabra"))
            valor = str(input("Dime el significado que le quieres poner a esa palabra"))
            palabras[clave] = valor
        case 2:
            clave = str(input("Dime la palabra que quieres modificar"))
            valor = str(input("Dime el nuevo significado de esa palabra"))
            palabras[clave] = valor
        case 3:
            buscar = str(input("Dime el nombre de la palabra que quieres saber su significado"))
            print(palabras.get(buscar))
        case 4:
            print()
        case 5:
            clave = str(input("Dime la palabra que quieres borrar del diccionario"))
            del palabras[clave]
        case 6:
            print(sorted(palabras.items()))
        case 7:
            for clave,valor in palabras.items():
                print(f"Palabra: {clave} , Significado: {valor}")







