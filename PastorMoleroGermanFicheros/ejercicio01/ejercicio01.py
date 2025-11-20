# 1. Escribe un programa que cuente cuántas líneas NO vacías contiene un fichero 
# 'entrada.txt' que tenga varias líneas de prueba. 


f = open('ejercicio01/entrada.txt', 'r')
contador=0

for linea in f:
    if linea.strip() == '':
        contador+=1
f.close()

print(f'Hay {contador} líneas vacias')
