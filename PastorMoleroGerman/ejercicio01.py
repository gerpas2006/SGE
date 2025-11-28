# 1. Escriba un programa que pida un número. Después pregunte cuántos números se van a 
# introducir, pida esos números, y escriba cuántos de esos números era mayor que el anterior

def numeroMayores(numeroPedido,listaAnadido):
    for i in listaAnadido:
        if i > numeroPedido:
            lista.append(i)
    return lista

numeroPedido= int(input("Dime un número"))
numeroAPedir = int(input("Cuántos número quieres introducir"))
lista = []
listaAnadido = []

for i in range(numeroAPedir):
    numeroAnadir = int(input("Dime el número"))
    listaAnadido.append(numeroAnadir)


print(f"Estos son los números más grandes que el pedido al principio {numeroMayores(numeroPedido,listaAnadido)}")