class yogur:

    caloria:float = 120.0
    
    def __init__(self,marca:str,sabor:str,trocitos:bool,desnatado:bool):
        self._marca = marca
        self._sabor = sabor
        self._trocitos = trocitos
        self._desnatado = desnatado
    
    @property
    def marca(self):
        return self._marca
    
    @marca.setter
    def marca(self, value:str):
        self._marca = value
    
    @property
    def sabor(self):
        return self._sabor
    
    @sabor.setter
    def sabor(self, value:str):
        self._sabor = value
    
    @property
    def trocitos(self):
        return self._trocitos
    
    @trocitos.setter
    def trocitos(self, value:bool):
        self._trocitos = value
    
    @property
    def desnatado(self):
        return self._desnatado
    
    @desnatado.setter
    def desnatado(self, value:bool):
        self._desnatado = value

class calorias:

    def calcularCalorias(yogur:yogur,tamanio:float)->float:
        totalCalorias = (tamanio / 100.0) * yogur.caloria
        if yogur.desnatado:
            totalCalorias = totalCalorias - totalCalorias * 0.3           
        return totalCalorias
    
    def sumarCalorias(yogures:list[yogur], tamanio:list[float])->float:
        suma = 0
        for i in range(0,len(yogures)):
            suma += calorias.calcularCalorias(yogures[i], tamanio[i])
        return suma
    
    def calcularCaloriasDesnatados(yogures:list[yogur], tamanio:float)->float:
        resultado = 0
        for i in yogures:
            if i.desnatado:
                resultado += calorias.calcularCalorias(i, tamanio)
        return resultado

class principal:
    print("=== CONTADOR DE CALORÍAS DE YOGURES ===\n")

    yogures:list[yogur] = []
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
        y = yogur(marca,sabor,trocitos,desnatado)
        print(f"El yogur {i+1} tiene {round(calorias.calcularCalorias(y,tamanio),2)} kcal\n")
        yogures.append(y)
        tamanios.append(tamanio)

    print(f"La suma de todos los yogures es de {calorias.sumarCalorias(yogures,tamanios)} kcal")