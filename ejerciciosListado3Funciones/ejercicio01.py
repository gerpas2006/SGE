class yogur:

    tamanio:float = 100.0
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
        totalCalorias = 0.0    
        if yogur.desnatado:
            totalCalorias = totalCalorias - totalCalorias * 0.3
        else:
            totalCalorias = (tamanio / 100.0) * yogur.caloria           
        return totalCalorias
    
    def sumarCalorias(yogures:list[yogur], tamanio:float)->float:
        suma = 0
        for i in yogures:
            suma += calorias.calcularCalorias(i, tamanio)
        return suma
    
    def calcularCaloriasDesnatados(yogures:list[yogur], tamanio:float)->float:
        resultado = 0
        for i in yogures:
            if i.desnatado:
                resultado += calorias.calcularCalorias(i, tamanio)
        return resultado

class principal:
    print("=== CONTADOR DE CALORÍAS DE YOGURES ===\n")

    marca = input("Marca del yogur: ")
    sabor = input("Sabor: ")
    trocitos = input("¿Tiene trocitos? (s/n): ").lower() == 's'
    desnatado = input("¿Es desnatado? (s/n): ").lower() == 's'
    tamanio = float(input("Tamaño en ml: "))

    yogur1 = yogur(marca, sabor, trocitos,desnatado)
    calorias_yogur1 = calorias.calcularCalorias(yogur1, tamanio)
    print(f"\nCalorías del yogur: {calorias_yogur1} kcal\n")

    print("--- Segundo yogur ---")
    marca2 = input("Marca del yogur: ")
    sabor2 = input("Sabor: ")
    trocitos2 = input("¿Tiene trocitos? (s/n): ").lower() == 's'
    desnatado2 = input("¿Es desnatado? (s/n): ").lower() == 's'
    tamanio2 = float(input("Tamaño en ml: "))

    yogur2 = yogur(marca2, sabor2, trocitos2, desnatado2)
    calorias_yogur2 = calorias.calcularCalorias(yogur2, tamanio2)
    print(f"\nCalorías del yogur: {calorias_yogur2} kcal\n")

    yogures = [yogur1, yogur2]
    total = calorias.sumarCalorias(yogures, 100)
    print(f"Calorías totales de los yogures (100ml c/u): {total} kcal")
    
    total_desnatados = calorias.calcularCaloriasDesnatados(yogures, 100)
    print(f"Calorías solo de yogures desnatados (100ml c/u): {total_desnatados} kcal")