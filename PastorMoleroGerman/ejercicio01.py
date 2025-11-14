contactos = {
    '123456789': 'Mamá',
    '987654321': 'Luisito'
}

historico= {}

repetir = True

while repetir:
    eleccion = int(input('''
        0. Salir
        1. Modificar un contacto
        2. Buscar un contacto
        3. Número de veces de un nombre
        4. Mostrar el diccionario
        5. Borrar un elemento     
        6. Historial de borrado                                           
'''))
    
    match eleccion:
        case 0:
            print("Saliendo....")
            repetir=False
        case 1:
            clave = str(input("Dime el número del contacto que quieres modificar"))
            valor = str(input("Dime el nuevo nombre del numero que me has dicho"))
            contactos[clave] = valor
        case 2:
            clave = str(input("Dime el número de telefono que quieres saber si esta"))
            if clave in contactos:
                print("Si esta en la agenda")
            else:
                print("Ese telefono no esta en la agenda")
        case 3:
            contador = 0
            nombre = str(input("Dime que nombre quieres ver cuantas veces se repite"))

            for i in contactos.values():
                if i == nombre:
                    contador+=1
            print(f"El nombre {nombre} se repite {contador} veces")
        case 4:
            for clave,valor in contactos.items():
                print(f"Teléfono {clave}, Nombre {valor}")
        case 5:
            eliminar = str(input("Dime el telefono que quieres eliminar"))
            historico = {
                contactos.pop(eliminar)
            }
            
        case 6:
            print(f"Estos son los contactos que has eliminado")
            for i in historico:
                print(f"Nombre {i}")
        case _:
            print("Elige una opción correcta")