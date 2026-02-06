class Yogur:

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