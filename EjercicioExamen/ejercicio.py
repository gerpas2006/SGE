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

            with open('fichero.txt', 'a') as f:
                # Leer el archivo para contar contactos existentes
                with open('fichero.txt', 'r') as read_f:
                    contenido = read_f.read()
                
                f.write(f"\n{'='*80}\n")
                f.write(f"CONTACTO\n")
                f.write(f"{'='*80}\n")
                f.write(f"Nombre:    {nombre}\n")
                f.write(f"Apellido:  {apellido}\n")
                f.write(f"Teléfono:  {telefono}\n")
                f.write(f"Correo:    {correo}\n")

            print("Contacto añadido.\n")
        case 2:
            with open(contactos, "r") as f:
                print(f.read())
        case 3:
        
