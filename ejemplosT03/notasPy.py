#Nota del trimestre de Python
numCriterio = int(input("¿Cuántos criterios hay?"))
listaCriterios = []
listaNotas =[]
totalNotas = ()
for numeros in range(numCriterio):
    criterio = float(input("Dime el numero del criterio"))
    listaCriterios.append(criterio)

for i in listaCriterios:
    numNotas = int(input(f"Dime cuantas notas hay en el criterio {i}"))
    for j in range(numNotas):
        nota = float(input("Dime la nota"))
        listaNotas.append(nota)
        suma = sum(listaNotas)/len(listaNotas)
        



