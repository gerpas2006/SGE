# 1. Escriba un programa que pida un número. Después pregunte cuántos números se van a 
# introducir, pida esos números, y escriba cuántos de esos números era mayor que el anterior

def numeroMayores(numeroPedido,listaAnadido):
    for i in listaAnadido:
        if i > numeroPedido:
            listaNumeroMayores.append(i)
    return listaNumeroMayores

def anadirNumero(listaAnadido,numeroAPedir):
    for i in range(numeroAPedir):
        numeroAnadir = int(input("Dime el número "))
        listaAnadido.append(numeroAnadir)


numeroPedido= int(input("Dime un número "))
numeroAPedir = int(input("Cuántos número quieres introducir "))
listaNumeroMayores = []
listaAnadido = []


anadirNumero(listaAnadido,numeroAPedir)
print(f"Estos son los números más grandes que el pedido al principio {numeroMayores(numeroPedido,listaAnadido)}")

# Mi compañero lo que a hecho ha sido añadir el numero pedido en la lista y después lo ha comparado