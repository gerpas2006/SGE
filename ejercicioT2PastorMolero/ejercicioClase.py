#Generame una lista de las edades de la clase de 2DAM y quiero que me hagas estas operaciones devolviendome todos los resultados con 2 decimales
#1. Calculame la media de edad de la clase
#2. Dime cuantos alumnos son mayores de 20 años
#3. Dime cual es la media de los alumnos mañores de 25 años
#4. Muestrame los alumnos que tengan una edad impar
#5. Dime cuantos alumnos hay con la edad que te diga el usuario

edadesClase = [25,23,18,19,24,19,26,21,26,27,30,31,23]
mediaAlumnos = []
alumnosEdadImpar = []
contador=0
mediaDeLaClase = round(sum(edadesClase)/len(edadesClase),2)

print(f"La media de edades de los alumnos de 2DAM es {mediaDeLaClase}")

for i in edadesClase:
    if i>20:
        contador+=1
print(f"Hay {contador} alumnos que son mayores de 20 años")

for i in edadesClase:
    if i>25:
        mediaAlumnos.append(i)
mediaAlumnos25 = round(sum(mediaAlumnos)/len(mediaAlumnos),2)
print(f"La media de edad de los alumnos mayores de 25 años es {mediaAlumnos25}")

for i in edadesClase:
    if i % 2 != 0:
        alumnosEdadImpar.append(i)
        
print(f"Estos son las edades impares que hay en la clase 2DAM {alumnosEdadImpar}")

edad = int(input("Dime que la edad que quieras saber que mas se repite en la clase 2DAM "))
print(f"La edad {edad} se repite {edadesClase.count(edad)} veces en la clase 2DAM")






