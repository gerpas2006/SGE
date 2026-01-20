import math
class Figura:
    
    def calcularArea():
        pass
    def calcularPerimetro():
        pass
    def calcularFactorEscala():
        pass

class Rectangulo(Figura):
    def calcularArea(base:float,altura:float):
        return round((base*altura),2)
    
    def calcularPerimetro(base:float,altura:float):
        return round((2*(base+altura)),2)
    
    def calcularFactorEscala():
        pass
        

class Circulo(Figura):
    
    def calcularArea(radio:float):
        return round((math.pi*radio**2),2)
    
    def calcularPerimetro(radio:float):
        return round((2*math.pi*radio),2)
    
    def calcularFactorEscala():
        pass
    

class Triangulo(Figura):
    
    def calcularArea(base:float,altura:float):
        return round(((base*altura)/2),2)
    
    def calcularPerimetro(longitudLadoUno:float,longitudLadoDos:float,longitudLadoTres:float):
        return round((longitudLadoUno+longitudLadoDos+longitudLadoTres),2)    
    
    def calcularFactorEscala():
        pass
    



