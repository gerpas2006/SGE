# 2. Escriba un programa que pida tres números enteros distintos y que escriba 
# una lista que empiece por el más pequeño y termine en el más grande.
#No leemos dentro de una funcion a no ser que me lo digan


def ordenarDeMenorAMayor(listaPedidios):
    return sorted(listaPedidios)

def anadirNumeroPedidos(numeroAPedir):
    for i in range(0,numeroAPedir):
        numeroPedido =int(input("Dime el número "))
        listaPedidios.append(numeroPedido)


listaPedidios = []
numeroAPedir = 4


anadirNumeroPedidos(numeroAPedir)
print(ordenarDeMenorAMayor(listaPedidios))

# Mi compañero lo ha hecho sin utilizar for y ha metido las dos funciones en una para al final solo mostrar la funcion que contiene el resultado final