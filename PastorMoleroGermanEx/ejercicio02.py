import random

tiempo = [
    ["Lunes","Martes","Miercoles","Jueves","Viernes","Sábado","Domingo"],
    [random.randint(1,60),random.randint(1,60),random.randint(1,60),random.randint(1,60),random.randint(1,60),random.randint(1,60),random.randint(1,60)]
]

repetir = True

while repetir:
    eleccion = int(input('''
            0. Salir
            1. Sumar una cant al Sábado y el Domingo
            2. Dias que no se ha jugado nada
            3. Mostrar lista
            4. Lista ordenada de menor a mayor
'''))
    
    match eleccion:
        case 0:
            print("Saliendo....")
            repetir = False
        case 1:
            horasExtrasSabado = int(input("Dime cuántas horas le quieres añafir al sábado"))
            

            horasExtrasDomigo = int(input("Dime cuántas horas le quieres añafir al domingo"))

            print(tiempo)
        case 2:
            diasNoJugado = []
            for i in tiempo[0]:
                for j in tiempo[1]:
                    if j == 0:
                        diasNoJugado.append(i)
            print(f"Estos son los dias que a habido examen {diasNoJugado}")
        case 3:
            for i,j in zip (tiempo[0],tiempo[1]):
                print(i,j)
        case 4:
            print(sorted(tiempo[0]))
            print(sorted(tiempo[1]))
        case _:
            print("Elige una opcion correcta")

    