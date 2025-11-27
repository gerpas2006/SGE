# 2. Escriba un programa que pida tres números enteros distintos y que escriba 
# una lista que empiece por el más pequeño y termine en el más grande.


listaPedidios = []
numeroAPedir = 3
for i in range(0,numeroAPedir):
    numeroPedido =int(input("Dime el número"))
    listaPedidios.append(numeroPedido)

def ordenarDeMenorAMayor(listaPedidios):
    return sorted(listaPedidios)

print(ordenarDeMenorAMayor(listaPedidios))