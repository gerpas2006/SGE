# 3. Escriba un programa que pregunte cuántos números se van a introducir, pida esos números, y muestre
# un mensaje cada vez que un número no sea mayor que el anterior


def mayor(numeroAPedir, listaNumero):
    for i in range(numeroAPedir):
        anadir = int(input("Dime el número"))
        listaNumero.append(anadir)
        if listaNumero[i] > listaNumero[i-1]:
            print("Este número es mayor que el anterior")

listaNumero = []

numeroAPedir = int(input("Dime cuántos números quieres añadir"))


print(mayor(numeroAPedir, listaNumero))