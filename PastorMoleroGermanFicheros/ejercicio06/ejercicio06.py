# 6. Crea un programa que lea de un fichero y tenga las siguientes funcionalidades en un menú:
# La palabra de mayor longitud. 
# Las veces que aparece una palabra. 
# Lea una línea aleatoria del fichero. 
# Dos funcionalidades más inventadas por tí. 

palabrasLargas = ['']
fichero = open('ejercicio06/fichero.txt', 'r')

for i in fichero:
    if(len(i) > str(palabrasLargas[0])):
        palabrasLargas.append(i)

print(palabrasLargas)