class Vehiculo:
    def __init__(self,marca:str,matricula:str,consumo:float):
        self.marca = marca
        self.matricula = matricula
        self.consumo = consumo
    
    def coste_recorrido(self,km:float)->float:
        return self.consumo*km

class Electrico(Vehiculo):
    def __init__(self, marca:str, matricula:str, consumo:float,costeAdicional:float):
        Vehiculo.__init__(self,marca, matricula, consumo)
        self.costeAdicional = costeAdicional
    
    def coste_recorrido(self, km:float)->float:
        return Vehiculo.coste_recorrido(self,km)+self.costeAdicional

class Autonomo(Vehiculo):
    def __init__(self, marca:str, matricula:str, consumo:float,costeSistema:float):
        Vehiculo.__init__(self,marca, matricula, consumo)
        self.costeSistema = costeSistema
    
    def coste_recorrido(self, km:float)->float:
        return Vehiculo.coste_recorrido(self,km)+self.costeSistema

class CocheInteligente(Electrico,Autonomo):
    def __init__(self, marca:str, matricula:str, consumo:float, costeAdicional:float,costeSistema:float):
        Electrico.__init__(self,marca,matricula,consumo,costeAdicional)
        Autonomo.__init__(self,marca,matricula,consumo,costeSistema)
    
    def coste_recorrido(self, km:float)->float:
        costeElectrico = Electrico.coste_recorrido(self,km)
        costeAutonomo = Autonomo.coste_recorrido(self,km)
        return costeAutonomo + costeElectrico


class Principal:


    vehiculo1 : Vehiculo = Electrico("Peugeot","ABC1234",120.12,20.23)
    vehiculo2 : Vehiculo = Autonomo("Renault","DEF5678",130.2,30.3)
    cocheInteligente = CocheInteligente("Citroen","QWE7568",23.1,12.3,24.1)

    print(f"El vehiculo electrico tiene un coste de {round(vehiculo1.coste_recorrido(120.12),2)} €")
    print(f"El vehiculo autonomo tiene un coste de {round(vehiculo2.coste_recorrido(124.2),2)} €")
    print(F"El coste del coche inteligente tiene un coste de {round(cocheInteligente.coste_recorrido(132.5),2)} €")
