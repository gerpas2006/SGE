from modelo.alumno import Alumno
from modelo.profesor import Profesor


class Aula:
    def __init__(self,nombre:str,tutor:Profesor):
        self.nombre = nombre
        self.tutor = tutor
        self.alumnos : list[Alumno] = []
    
    def agregarAlumnos(self,alumno:Alumno):
        self.alumnos.append(alumno)
    
    def calcular_nota_media(self) -> float:
        if not self.alumnos:
            return 0.0
        
        suma_nota = sum(alumno.nota for alumno in self.alumnos)
        return suma_nota/len(self.alumnos)
    
    def __str__(self):
        return f"Nombre = {self.nombre}, Tutor = ´{self.tutor}"
    