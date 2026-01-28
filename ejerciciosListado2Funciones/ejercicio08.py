import math
class Figura:
    def __init__(self,nombre:str):
        self.nombre = nombre
    
    def calcularArea(self):
        pass

    def calcularPerimetro(self):
        pass

class Triangulo(Figura):
    def __init__(self, nombre:str,altura:float,base:float):
        super().__init__(nombre)
        self.altura = altura
        self.base = base

    def __str__(self):
        return f"Figura (Nombre: {self.nombre}, Altura: {self.altura}, Base: {self.base})"

    def calcularArea(self):
        return (self.base*self.altura)/2
    
    def calcularPerimetro(self):
        return self.base*3

class Circulo(Figura):

    def __init__(self, nombre:str,radio:float):
        super().__init__(nombre)
        self.radio = radio
    
    def calcularArea(self):
        return math.pi*self.radio**2
    
    def calcularPerimetro(self):
        return 2*math.pi*self.radio

class Rectangulo(Figura):

    def __init__(self, nombre:str,altura:float,base:float):
        super().__init__(nombre)
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return self.base*self.altura
    
    def calcularPerimetro(self):
        return 2 * (self.base+self.altura)

figuras: list[Figura] = [
    Triangulo('Triangulo',5,4),
    Triangulo('Triangulo1',8,2),
    Triangulo('Triangulo2',4,6),
    Circulo('Círculo',2.5),
    Rectangulo('Rectangulo',5,4)
]

suma = 0.0
perimetro = 0.0
triangulo = None
area = 0.0


for i in figuras:
    print(f"Nombre: {i.nombre} Área {round(i.calcularArea(),2)} Perímetro {round(i.calcularPerimetro(),2)}")
    suma += i.calcularArea()
    perimetro += i.calcularPerimetro()
    if isinstance(i,Triangulo):
        if (area<i.calcularArea()):
            area = i.calcularArea()
            triangulo = i
        

print(f"La suma de todas las áreas es {round(suma,2)} y la suma de todos los perimetros es {round(perimetro,2)} y el triangulo con mayor área es {triangulo}")


