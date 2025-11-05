# 17. Rellenar la lista con temperaturas generadas de forma aleatoria entre dos límites leídos por teclado. Pueden
# tener decimales.
# A partir de esa lista, el programa debe:
# Mostrar todas las temperaturas introducidas.
# Calcular y mostrar la temperatura media.
# Mostrar la temperatura máxima y mínima junto con el día en que ocurrieron.
# Ordena la lista de mayor a menor temperatura.
# Mostrar cuántos días tuvieron temperaturas por encima de la media.
# Crear una nueva lista solo con las temperaturas superiores a la media.
import random



temperaturas = [
    ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"],
    []
]

desde = float(input("Dime desde que temperatura quieres registrar "))
hasta = float(input("Dime hasta que temperatura quieres registrar "))

for i in range(len(temperaturas[0])):
    temperaturas[1].append(random.randint(desde,hasta))

for dias,tem in zip(temperaturas[0],temperaturas[1]):
    print(f"{dias}: {tem} grados")

media = round(sum(temperaturas[1])/len(temperaturas[1]),2)

print(f"La media de las temperaturas es {media}")

print(f"La temperatura más alta registrada a sido {max(temperaturas[1])} y la mínima a sido {min(temperaturas[1])}")
