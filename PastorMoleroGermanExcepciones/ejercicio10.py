class IsEmpty(Exception):
    def __init__(self, mensaje = " La lista esta vacia"):
        super().__init__(mensaje)
class CantidadErronea(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)

class TipoPedido:
    def __init__(self,precioBase:float,cant:int,nombre:str):
        self.precioBase = precioBase
        self.cant = cant
    
    def calcularPrecioFinal(self)->float:
        return self.precioBase*self.cant

class Farmacia(TipoPedido):
    def __init__(self, precioBase:float, cant:int, nombre:str,descuento:float):
        super().__init__(precioBase, cant, nombre)
        self.descuento = descuento
    
    def calcularPrecioFinal(self):
        if self.descuento<0:
            raise CantidadErronea("El descuento no puede ser menor que 0")
        elif self.descuento>100:
            raise CantidadErronea("El descuento no puede ser mayor que 100")
        return super().calcularPrecioFinal()-((super().calcularPrecioFinal()*self.descuento)/100)
    
class Logistica(TipoPedido):
    def __init__(self, precioBase:float, cant:int,nombre:str,precioPorLlevarCasa:float):
        super().__init__(precioBase, cant, nombre)
        self.precioPorLlevarCasa = precioPorLlevarCasa
    
    def calcularPrecioFinal(self):
        if self.precioPorLlevarCasa<0:
            raise CantidadErronea("El precio por llevarlo a casa no puede ser menor que 0")
        return super().calcularPrecioFinal()+self.precioPorLlevarCasa
    
class GestionPedido:
    def __init__(self,listaPedidos:list[TipoPedido]):
        self.listaPedido = listaPedidos

    def cantDePedidoDeLogitica(self):
        resul = 0
        if not self.listaPedido:
            raise IsEmpty()
        for i in self.listaPedido:
            if isinstance(i,Logistica):
                resul+=1
        return resul
    
    def calcularPrecioTotal(self):
        resul = 0
        if not self.listaPedido:
            raise IsEmpty()
        for i in self.listaPedido:
            resul += i.calcularPrecioFinal()
        return resul

class Principal:

    listaPedidos:list[TipoPedido]= [
        Farmacia(25.6,5,"Farmacia",10),
        Logistica(89.5,4,"Logistica",2.3)
    ]

    gestionPedido:GestionPedido = GestionPedido(listaPedidos)

    print(Farmacia.calcularPrecioFinal())
    print(Logistica.calcularPrecioFinal())
    print(gestionPedido.calcularPrecioTotal())
    print(gestionPedido.cantDePedidoDeLogitica())

