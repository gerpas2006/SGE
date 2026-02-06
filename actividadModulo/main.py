from model.calorias import Calorias
from model.yogur import Yogur


def main():
    print("=== CONTADOR DE CALORÍAS DE YOGURES ===\n")

    yogures:list[Yogur] = []
    tamanios:list[float] = []

    cant = int(input("Cuantos yogures quieres añadir: "))
    for i in range (cant):
        marca = input(f"Dime la marca del {i+1} yogur: ")
        sabor = input(f"Dime el sabor del {i+1} yogur: ")
        trocitos = input("Tiene trocitos el yogur? s/n: ")
        if trocitos == 's':
            trocitos = True
        else:
            trocitos = False
        desnatado = input("El yogur es desnatado? s/n: ")
        if desnatado == 's':
            desnatado = True
        else:
            desnatado = False
        tamanio = float(input("Que tamaño tiene el yogur: "))
        y = Yogur(marca,sabor,trocitos,desnatado)
        print(f"El yogur {i+1} tiene {round(Calorias.calcularCalorias(y,tamanio),2)} kcal\n")
        yogures.append(y)
        tamanios.append(tamanio)

    print(f"La suma de todos los yogures es de {Calorias.sumarCalorias(yogures,tamanios)} kcal")


if __name__ == "__main__":
    main()