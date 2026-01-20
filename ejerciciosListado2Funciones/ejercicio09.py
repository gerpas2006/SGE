class Droid:
    def __init__(self, nombre:str,velocidad:float,tiempo:float,danioRecibido:float,vida:float):
        self.nombre = nombre
        self.velocidad = velocidad
        self.tiempo = tiempo
        self.danioRecibido = danioRecibido
        self.vida = vida
    
    def distanciaRecorrida(self):
        pass
    
    def calcularVidaActual(self):
        pass

class ProtocoloDroid(Droid):
    def __init__(self, nombre, velocidad, tiempo, danioRecibido, vida):
        super().__init__(nombre, velocidad, tiempo, danioRecibido, vida)

    def distanciaRecorrida(self):
        return self.velocidad*self.tiempo
    
    def calcularVidaActual(self):
        return self.vida-self.danioRecibido
    
class AstromechDroid(Droid):
    def __init__(self, nombre, velocidad, tiempo, danioRecibido, vida):
        super().__init__(nombre, velocidad, tiempo, danioRecibido, vida)

    def distanciaRecorrida(self):
        return self.velocidad*self.tiempo
    
    def calcularVidaActual(self):
        return self.vida-self.danioRecibido
    
    