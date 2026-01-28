# 4. Crear un programa de ayuda a operaciones con aleatorios, es decir, que tenga, al menos, 4 funciones que
# generen y hagan operaciones con números aleatorios, por ejemplo, tirar un dado pero también puede haber
# otras que calculen cosas con una serie de números de forma aleatoria, por ejemplo, decir cuántas veces ha
# salido un número en una serie de tiradas del dado, cuál es el porcentaje de que salga un número según esas
# tiradas (si de 10 veces ha salido el 6 dos veces en 100 tiradas saldría...).

import random
def tirar_dado():
    return random.randint(1, 6)

def tirar_dados(n):
    return [tirar_dado() for _ in range(n)]

def contar_apariciones(tiradas, numero):
    return tiradas.count(numero)

def porcentaje_apariciones(tiradas, numero):
    total_tiradas = len(tiradas)
    if total_tiradas == 0:
        return 0
    apariciones = contar_apariciones(tiradas, numero)
    return (apariciones / total_tiradas) * 100

num_tiradas = 10
tiradas = tirar_dados(num_tiradas)
numero_a_contar = 6
apariciones = contar_apariciones(tiradas, numero_a_contar)
porcentaje = porcentaje_apariciones(tiradas, numero_a_contar)
print(f"Tiradas: {tiradas}")
print(f"El número {numero_a_contar} ha salido {apariciones} veces.")
print(f"Porcentaje de apariciones del número {numero_a_contar}: {porcentaje}%")