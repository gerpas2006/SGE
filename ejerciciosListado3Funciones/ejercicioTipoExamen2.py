class Beverage:
    def __init__(self,nombre:str,cost:float):
        self.nombre = nombre
        self._cost = cost
    @property
    def getCost(self):
        return self._cost
    
    @getCost.setter
    def cost(self,cost:float):
        self._cost = cost

class PremiumIngredients(Beverage):
    def __init__(self, nombre:str, cost:float, listaIngrediente:list):
        super().__init__(nombre, cost)
        self.listaIngrediente = listaIngrediente

    @staticmethod
    def get_available_extras() -> tuple:
        extras = ("Caramelo","Chocolate","Canela","Nata")
        return extras

class CafeService(Beverage):
    def __init__(self, nombre:str, cost:float,temperatura:tuple,puntos:int):
        super().__init__(nombre, cost)
        self.temperaturas = temperatura
        self.puntos = puntos
    
    @staticmethod
    def get_service_hours():
        horario = "Horario: 7:00 - 22:00"
        return horario
    
class SpecialCoffee(PremiumIngredients,CafeService):
    totalOreders = 0

    def __init__(self, nombre, cost, listaIngrediente,temperatura:tuple,puntos:int):
        PremiumIngredients.__init__(self,nombre, cost, listaIngrediente)
        CafeService.__init__(self,nombre,cost,temperatura,puntos)

    @classmethod
    def show_statistics(self)->int:
        return self.totalOrders
    
    @classmethod
    def aumentarTotal(self):
        self.totalOreders += 1
    
    def __str__(self):
        return super().__str__() + f",Nombre: {self.nombre}, Coste: {self.cost}, Extras: {self.listaIngrediente} Temperaturas: {self.temperaturas}, Puntos: {self.puntos}"


class Principal:

    cafe1 = SpecialCoffee("Caramel Latte",2.45,["Chocolate","Caramelo"],("Caliente"),2)
    cafe1.aumentarTotal()
    cafe2 = SpecialCoffee("Caramel Latte",2.45,["Chocolate","Caramelo"],("Caliente"),2)
    cafe2.aumentarTotal()
    cafe3 = SpecialCoffee("Caramel Latte",2.45,["Chocolate","Caramelo"],("Caliente"),2)
    cafe3.aumentarTotal()

    print(f"Hay {SpecialCoffee.show_statistics()} cafes")
        



