
def validar_coste_positivo(func):
        def wrapper(*args, **kwargs):
            coste = func(*args, **kwargs)
            if coste < 0:
                print("El coste no puede ser menor que 0")
            return coste
        return wrapper
class Servidor:

    def __init__(self,num_dias:int,coste_diario:float):
        self.num_dias = num_dias
        self.coste_diario = coste_diario

    @validar_coste_positivo
    def coste_anual(self):
        return self.coste_diario * self.num_dias
    
class MMO(Servidor):

    def __init__(self, num_dias:int, coste_diario:float,coste_base:float):
        super().__init__(num_dias, coste_diario)
        self.coste_base = coste_base
    
    def coste_anual(self):
        return super().coste_anual() + self.coste_base
    

class BattleRoyale(Servidor):

    def __init__(self, num_dias, coste_diario,cost_matchmaking:float):
        super().__init__(num_dias, coste_diario)
        self.coste_matchmaking = cost_matchmaking
    
    def coste_anual(self):
        return super().coste_anual() * self.coste_matchmaking

class Streaming(Servidor):

    def __init__(self, num_dias, coste_diario,coste_streaming:float,num_usuarios:float):
        super().__init__(num_dias, coste_diario)
        self.coste_streaming = coste_streaming
        self.num_usuarios = num_usuarios
    
    def coste_anual(self):
        return (super().coste_anual() * self.coste_streaming)*self.num_usuarios
    
class CentroDeServidores:

    def calcular_total_anual(self, listaServidores:list[Servidor]):
        suma = 0
        for i in listaServidores:
            suma += i.coste_anual()
        return suma
    def descuentoProveedor(self,descuento:float,cantSuperar:float):
        if self.calcular_total_anual> cantSuperar:
            return self.calcular_total_anual-((self.calcular_total_anual*descuento)/100)
    
    def totalServidorMMO(self, listaServidores:list[Servidor]):
        suma = 0
        for i in listaServidores:
            if isinstance(i, MMO):
                suma += i.coste_anual()
        return suma
    
class ServidorHibrido(MMO,BattleRoyale):

    def __init__(self, num_dias, coste_diario, coste_base, cost_matchmaking):
        MMO.__init__(self, num_dias, coste_diario, coste_base)
        BattleRoyale.__init__(self, num_dias, coste_diario, cost_matchmaking)
    
    def costeTotal(self):
        return MMO.coste_anual(self) + BattleRoyale.coste_anual(self) - Servidor.coste_anual(self)
    
class ServidorPremium(MMO):
    
    def __init__(self, num_dias, coste_diario, coste_base):
        super().__init__(num_dias, coste_diario, coste_base)


if __name__ == "__main__":
    servidor1 = Servidor(365, 10.5)
    print(f"Servidor básico - Coste anual: {servidor1.coste_anual()}€")
    
    mmo1 = MMO(365, 15.0, 5000.0)
    print(f"Servidor MMO - Coste anual: {mmo1.coste_anual()}€")
    
    battle1 = BattleRoyale(365, 12.0, 1.5)
    print(f"Servidor BattleRoyale - Coste anual: {battle1.coste_anual()}€")
    
    streaming1 = Streaming(365, 8.0, 2.0, 1000)
    print(f"Servidor Streaming - Coste anual: {streaming1.coste_anual()}€")
    
    premium1 = ServidorPremium(365, 20.0, 10000.0)
    print(f"Servidor Premium - Coste anual: {premium1.coste_anual()}€")
    
    print("\n--- Probando validador de coste negativo ---")
    servidor_negativo = Servidor(365, -10.0)
    print(f"Coste anual con valor negativo: {servidor_negativo.coste_anual()}")


