class Alumno:
    def __init__(self,nombre:str,nota:float):
        self.nombre = nombre
        self.nota = nota

    def __str__(self):
        return f"Alumno(nombre = {self.nombre}, nota = {self.nota})"