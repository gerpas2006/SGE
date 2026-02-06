from gestion.aula import Aula
from modelo.alumno import Alumno
from modelo.profesor import Profesor


def main():
    profesor = Profesor("Ana García","Matemática")

    aula = Aula("1 Bachillarato",profesor)

    alumno1 = Alumno("Pedro",5)
    alumno2 = Alumno("Raúl",8)
    alumno3 = Alumno("Antonio",10)

    aula.agregarAlumnos(alumno1)
    aula.agregarAlumnos(alumno2)
    aula.agregarAlumnos(alumno3)

    print(aula)
    print(f"Nota media del aula es: {aula.calcular_nota_media():.2f}")

if __name__ == "__main__":
    main()