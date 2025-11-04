# 13. Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen
# posiciones múltiplos de 3, y muestre por pantalla la lista resultante.

abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


for i in abecedario:
    if abecedario.index(i) % 3 == 0:
        abecedario.remove(i)

print(f"Esta es la lista quitandole los valores que estan en una posicion multiplo de 3 {abecedario}")