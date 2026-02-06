from model.yogur import Yogur


class Calorias:

    def calcularCalorias(yogur:Yogur,tamanio:float)->float:
        totalCalorias = (tamanio / 100.0) * yogur.caloria
        if yogur.desnatado:
            totalCalorias = totalCalorias - totalCalorias * 0.3           
        return totalCalorias
    
    def sumarCalorias(yogures:list[Yogur], tamanio:list[float])->float:
        suma = 0
        for i in range(0,len(yogures)):
            suma += Calorias.calcularCalorias(yogures[i], tamanio[i])
        return suma
    
    def calcularCaloriasDesnatados(yogures:list[Yogur], tamanio:float)->float:
        resultado = 0
        for i in yogures:
            if i.desnatado:
                resultado += Calorias.calcularCalorias(i, tamanio)
        return resultado
