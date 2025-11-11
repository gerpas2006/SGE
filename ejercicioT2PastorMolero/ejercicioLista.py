# Voy a alquilar una habitación de mi casa a modo de apartamento turístico y necesito un programa para gestionar lo
# recaudado. Se debe usar una lista como estructura principal para guardar los datos (si hace falta alguna tupla se puede
# usar). Como no hemos dado todavía objetos, lo haremos con una lista de flotantes, que será lo recaudado cada día que lo
# alquilo.
# El programa puede empezar creando una lista directamente con datos y luego poder hacer lo siguiente mediante un menú
# en la clase Principal y debe mostrar en la misma
# • Agregar una nueva recaudación.
# • Poner a cero una recaudación (se me ha ido el cliente sin pagar).
# • Imprimir toda la lista, es decir, mostrar todos los datos de todas las recaudaciones en bonito.
# • Buscar el día en que más he ganado y decir cuántos días he ganado esa cantidad.
# • Sumar una cantidad a un día como gasto extra.
# • Calcular cuánto he recaudado en todas las recaudaciones.
# • Ordenar la lista de mayor a menor.
# • Calcular la media diaria.
# • Calcular el porcentaje de días al mes (suponiendo 30 días) en que he tenido la habitación alquilada.
# • Dividir la lista en dos nuevas listas. Una de ellas debe ser la que tenga las 5 menores recaudaciones, la otra las restantes.

departamento = [123.6,124.4,125.45,126.12,127.24,129.99,129.99]
repetir = True

menoresRecaudacione = []
demasRecaudaciones = []


while repetir:
    eleccion = int(input("\n0. Salir \n1. Añadir una nueva recaudación \n2. Poner a cero una recaudación \n3. Imprimir todos los datos recaudados \n4. El dia que mas he recaudado " \
    "\n5. Sumar una cantidad a un dia en concreto \n6. Ordenar la lista de mayor a menor \n7. Calcular la media de cada dia \n8. Porcentaje de dias he tenido alquilada la habitacion\nDime que quieres hacer "))
    match eleccion:
        case 0:
            print("Saliendo....")
            repetir=False
        case 1:
            agregarRecaudacion = float(input("Dime en que día quieres añadir la recaudación"))
            departamento.append(agregarRecaudacion)
        case 2:
            indice = float(input("Dime el indice de la recaudacion que quieres poner a 0"))
            indice-=1
            departamento[indice] = 0
            print(departamento)
        case 3:
            for i in departamento:
                print(f"Recaudado = {i}")
        case 4:
            contador =0
            for i in departamento:
                if i == max(departamento):
                    contador+=1
            print(f"Ha habido {contador} dias que has ganado el dinero {max(departamento)}")
        case 5:
            indice = float(input("Dime el indice del dia que quieres cambiar"))
            indice -=1
            nuevoValor = float(input("Dime el nuevo valor"))
            departamento[indice] = nuevoValor
            print(departamento)
        case 6:
            print(f"La lista ordenada es {sorted(departamento)}")
        case 7:
            print(f"La suma de las recaudaciones es {sum(departamento)}")
                
        


