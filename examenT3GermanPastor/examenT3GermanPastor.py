class Interaccion:
    def __init__(self,puntuacionMin:int,diasEnCuenta:int,puntuacionBase:float):
        self.puntuacionMinima = puntuacionMin
        self.diasEnCuenta = diasEnCuenta
        self.puntuacionBase = puntuacionBase

    
    def puntuaciuonInteraccion(self):
        return self.puntuacionBase

class Reaccion(Interaccion):
    def __init__(self, puntuacionMin, diasEnCuenta, puntuacionBase,like:bool):
        super().__init__(puntuacionMin, diasEnCuenta, puntuacionBase)
        self.like = like

    def puntuaciuonInteraccion(self)->float:
        resul = 0
        if self.like:
            resul = super().puntuaciuonInteraccion() + 1
        else:
            resul = super().puntuaciuonInteraccion() - 1
        return resul
    

class Visualizacion(Interaccion):
    def __init__(self, puntuacionMin, diasEnCuenta, puntuacionBase,numeroSegundos:float):
        super().__init__(puntuacionMin, diasEnCuenta, puntuacionBase)
        self.numeroSegundos = numeroSegundos

    def puntuaciuonInteraccion(self,cantDada)->float:
        resul = 0
        if self.numeroSegundos>3:
            resul = super().puntuaciuonInteraccion()*cantDada
        else:
            resul = super().puntuaciuonInteraccion
        return resul


class VideoCompartido(Reaccion,Visualizacion):
    def __init__(self, puntuacionMin:int, diasEnCuenta:int, puntuacionBase:float,numeroSegundos:float,like:bool,numCompartidos:int):
        Reaccion.__init__(puntuacionMin, diasEnCuenta, puntuacionBase, like)
        Visualizacion.__init__(puntuacionMin, diasEnCuenta, puntuacionBase,numeroSegundos)
        self.numCompartidos = numCompartidos

    def sumaReaccionVisualizacion()->float:
        return Reaccion.puntuaciuonInteraccion()+Interaccion.puntuaciuonInteraccion()
    
class PublicacionCaracterizada:
    def __init__(self,listaInterracion:list[Interaccion]):
        self.listaInteraccion = listaInterracion
    
    def totalInteracciones(self)->float:
        resul = 0
        for i in self.listaInteraccion:
            resul += i.puntuaciuonInteraccion()
        return resul
    
    # def cambiarPuntuacionMinima(self):
    #     return Interaccion

class Principal:

    print("Bienvenido a mi programa")

    puntuacionBase = 22.3
    cantDada = 2

    listaInteracciones:list[Interaccion] = [
        Reaccion(2,3,puntuacionBase,True),
        Visualizacion(3,5,puntuacionBase,5.5)
    ]

    # publicacionCaracterizada:PublicacionCaracterizada = PublicacionCaracterizada(listaInteracciones) 

    # videoCompartido:VideoCompartido= VideoCompartido(2,5,puntuacionBase,5,True,2)

    for i in listaInteracciones:
        if isinstance(i,Reaccion):
            print(f"La puntuacion de las Reacciones es de {i.puntuaciuonInteraccion()}")
        elif isinstance(i,Visualizacion):
            print(f"La puntuacion de las Visualizaciones es de {i.puntuaciuonInteraccion(cantDada)}")
    
    # print(f"La suma de todas las Visualizaciones y de las Reacciones es de {videoCompartido.sumaReaccionVisualizacion()}")

    # print(f"La suma de todas las interacciones es de {publicacionCaracterizada.totalInteracciones(cantDada)}")