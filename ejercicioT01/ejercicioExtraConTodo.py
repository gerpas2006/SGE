#Un cajero automático permite al usuario realizar varias operaciones. El programa debe:

#Comenzar con un saldo inicial de 1000 euros.
#Mostrar un menú de opciones en un bucle:
#Consultar saldo 
#Depositar dinero
#Retirar dinero
#Salir
#Usar un bucle para repetir el menú hasta que el usuario elija “Salir”.
#Usar match/case para ejecutar la operación seleccionada.
#Usar condiciones para evitar retirar más dinero del que hay disponible.


saldo = 100
eleccion = None
while eleccion!=0:
    print("0. Salir\n1. Consultar saldo\n2. Depositar dinero.\n3. Retirar dinero\n4. Hacer varios ingresos")
    eleccion = int(input("Dime que quieres hacer "))
    match eleccion:
        case 0:
            print("Saliendo....")
        case 1:
            print(f"Ahora mismo en la cuenta tienes {saldo}€")
        case 2:
            depositar = float(input("Cuanto dinero quieres depositar "))
            if depositar>0:
                 saldo+=depositar
                 print("Dinero depositado correctamente")
            elif depositar<0:
                 print("No puedes introducir un numnero negativo")
        case 3:
            retirar = float(input("Dime cuanto dinero quieres retirar "))
            if retirar>saldo:
                print("No puedes retirar dinero que no tienes")
            elif retirar<0:
                print("No puedes retirar dinero negativo")
            else:
                saldo-=retirar
                print(f"Aquie tienes sus {retirar}€")
        case 4:
            numDepositos= int(input("Cuantos depositos quieres hacer "))
            for i in range (0,int(numDepositos)):   
                depositar= float(input(f"Cuanto quieres depositar en la {i + 1 } vez"))
                if depositar<0:
                    print("No puedes depositar números negativos")
                elif depositar>0:
                    saldo+=depositar
            print("Todo el dinero ha sido depositado correctamente")
            
        case _ :
            print("Elige una opción correcta")
