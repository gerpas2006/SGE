contactos = "fichero.txt"

repetir = True

while repetir:
    eleccion = int(input('''
0. Salir
1. Crear Contacto
2. Leer Contactos
3. Actualizar Contactos
4. Borrar Contacto
'''))

    match eleccion:
        case 0:
            print("Saliendo.....")
            repetir = False

        case 1:
            nombre = input("Dime el nombre del nuevo contacto: ")
            apellido = input("Dime el apellido del nuevo contacto: ")
            telefono = input("Dime el teléfono del nuevo contacto: ")
            correo = input("Dime el correo del nuevo contacto: ")

            f = open('fichero.txt', 'a')
            f.write(f"\n{'='*80}\n")
            f.write(f"CONTACTO\n")
            f.write(f"{'='*80}\n")
            f.write(f"Nombre:    {nombre}\n")
            f.write(f"Apellido:  {apellido}\n")
            f.write(f"Teléfono:  {telefono}\n")
            f.write(f"Correo:    {correo}\n")
            f.close()

            print("Contacto añadido.\n")
            
        case 2:
            f = open(contactos, "r")
            print(f.read())
            f.close() 
            
        case 3:
            f = open(contactos, "r")
            contenido = f.read()
            f.close()
            
            nombre_buscar = input("Nombre del contacto a actualizar: ")
            
            if nombre_buscar in contenido:
                nuevo_nombre = input("Nuevo nombre: ")
                nuevo_apellido = input("Nuevo apellido: ")
                nuevo_telefono = input("Nuevo teléfono: ")
                nuevo_correo = input("Nuevo correo: ")
                
                contenido = contenido.replace(f"Nombre:    {nombre_buscar}", f"Nombre:    {nuevo_nombre}")
                
                f = open(contactos, "w")
                f.write(contenido)
                f.close()
                print("Contacto actualizado.\n")
            else:
                print("Contacto no encontrado.\n")
                
        case 4:
            f = open(contactos, "r")
            contenido = f.read()
            f.close()
            
            nombre_borrar = input("Nombre del contacto a borrar: ")
            
            if nombre_borrar in contenido:
                lineas = contenido.split('\n')
                nuevo = []
                i = 0
                while i < len(lineas):
                    if f"Nombre:    {nombre_borrar}" in lineas[i]:
                        i += 4
                    else:
                        nuevo.append(lineas[i])
                    i += 1
                
                f = open(contactos, "w")
                f.write('\n'.join(nuevo))
                f.close()
                print("Contacto borrado.\n")
            else:
                print("Contacto no encontrado.\n")
            
