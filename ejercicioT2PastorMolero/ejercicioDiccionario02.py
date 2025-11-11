# 3. Crear un diccionario que tenga como claves el dni de un estudiante y como valor la nota media de su
# expediente. La nota media se generará de manera aleatoria entre 1 y 10.
# Escribir el código necesario en un menú para hacer los siguiente:
# a) Mostrar los datos.
# b) Modificar la nota.
# c) Añadir un nuevo estudiante.
# d) Crear un nuevo diccionario (no modificar el original) solo con los estudiantes que tienen nota media
# mayor a un valor dado por teclado (por ejemplo, para comprobar que pueden entrar en un ciclo según esa
# nota de corte).
import random


alumnos = {
    '12345j' : random.randint(1,10),
    '12345s' : random.randint(1,10),
    '12345q' : random.randint(1,10),
    '12345w' : random.randint(1,10),
    '12345e' : random.randint(1,10),
}

repetir = True

while repetir:
    eleccion = int(input("0. Salir\n1. Mostrar los datos\n2. Modificar la nota\n3. Añadir un nuevo alumno\n4. Alumnos que pueden entrar en el grado 2 DAM\n"))
    match eleccion:
        case 0:
            print("Saliendo....")
            repetir = False
        
        case 1:
            for dni,nota in alumnos.items():
                print(f"Dni: {dni} , Nota Media: {nota}")
        case 2:
            dni = str(input("Dime el dni del alumno"))
            nuevaNotaMedia = float(input("Dime la nueva nota media"))
            alumnos[dni] = nuevaNotaMedia
            for dni,nota in alumnos.items():
                print(f"Dni: {dni} , Nota Media: {nota}")
        case 3:
            dni = str(input("Dime el dni del nuevo alumno"))
            alumnos[dni] = random.randint(1,10)
            for dni,nota in alumnos.items():
                print(f"Dni: {dni} , Nota Media: {nota}")
        case 4:
            alumnosMejorNota = {}
            notaAlta = float(input("Dime la nota media para saber quines entran en el grado superior de DAM"))
            for dni,nota in alumnos.items():
                if nota>=notaAlta:
                    alumnosMejorNota[dni] = nota
            print("Estos son los alumnos que entran en el grado de DAM ")
            for i,j in alumnosMejorNota.items():
                print(f"Dni: {i} , Nota Media: {j}")


