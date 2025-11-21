# 4. Crea un programa que lea un fichero llamado 'texto.txt' y genere 'numerado.txt' con todas las líneas 
# precedidas de su número. 

numero = 1
texto = open('ejercicio04/texto.txt', 'r')
numerado = open('ejercicio04/numerado.txt', 'w')

for i in texto:
    numerado.write(f"{numero}. {i}")
    numero += 1

texto.close()
numerado.close()