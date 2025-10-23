##3. Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno 
#(comprendidas entre 0 y 10). A continuación, debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor. 

notas = []
media=0

numeroDeNotas= int(input("Dime cuántas notas quieres añadir"))
for i in range (numeroDeNotas):
    nota = float(input(f"Dime la {i+1} nota "))
    if nota>10 and nota<0:
        print("Introduce una nota válida")
    else:
        notas.append(nota)

print(f"Estas son todas las notas que has puesto {notas}")
for i in notas:
    media+=i

media=media/len(notas)
print(f"La media de todas las notas es {media}")