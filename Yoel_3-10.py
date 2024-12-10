
"""
Diseña la clase Escuela para hacer un programa en Python 3 que permita la gestión completa de varias escuelas.
Cada escuela se instanciará a partir de la clase Escuela, que contendrá la información de la escuela (nombre, localidad, responsable...), 
así como la información de los diferentes profesores y grupos de alumnos, utilizando las siguientes clases auxiliares:

Clase Escuela: Deberá tener métodos para añadir/eliminar alumnos y profesores.
Clase Profesor: Contendrá la información de los profesores (nombre, tipo de profesor: ciencias, letras o mixto).
Clase Alumno: Contendrá la información de los alumnos (nombre, curso, profesor responsable).
Las clases deben estar en ficheros independientes. Ejemplo: Python Importar clase desde otro archivo
Cada clase deberá tener sus métodos CRUD:
    Crear (constructor)
    Leer (Getters y toString)
    Actualizar (Setters)
    Eliminar (Si fuera necesario, en este caso eliminar de una lista)
"""

class Profesor:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def actualizar_datos(self, nombre=None, tipo=None):
        if nombre:
            self.nombre = nombre
        if tipo:
            self.tipo = tipo

class Alumno:
    def __init__(self, nombre, curso, profesor_responsable):
        self.nombre = nombre
        self.curso = curso
        self.profesor_responsable = profesor_responsable

    def actualizar_datos(self, nombre=None, curso=None, profesor_responsable=None):
        if nombre:
            self.nombre = nombre
        if curso:
            self.curso = curso
        if profesor_responsable:
            self.profesor_responsable = profesor_responsable

class Escuela:
    def __init__(self, nombre, localidad, responsable):
        self.nombre = nombre
        self.localidad = localidad
        self.responsable = responsable
        self.profesores = []  # Lista de objetos Profesor
        self.alumnos = []  # Lista de objetos Alumno

    # Métodos CRUD para profesores
    def agregar_profesor(self, nombre, tipo):
        nuevo_profesor = Profesor(nombre, tipo)
        self.profesores.append(nuevo_profesor)
        print(f"Profesor {nombre} añadido.")

    def eliminar_profesor(self, nombre):
        self.profesores = [p for p in self.profesores if p.nombre != nombre]
        print(f"Profesor {nombre} eliminado.")

    def actualizar_profesor(self, nombre, nuevo_nombre=None, nuevo_tipo=None):
        for profesor in self.profesores:
            if profesor.nombre == nombre:
                profesor.actualizar_datos(nuevo_nombre, nuevo_tipo)
                print(f"Profesor {nombre} actualizado.")
                return
        print(f"Profesor {nombre} no encontrado.")

    def listar_profesores(self):
        return [str(p) for p in self.profesores]


    def agregar_alumno(self, nombre, curso, profesor_responsable):
        nuevo_alumno = Alumno(nombre, curso, profesor_responsable)
        self.alumnos.append(nuevo_alumno)
        print(f"Alumno {nombre} añadido.")

    def eliminar_alumno(self, nombre):
        self.alumnos = [a for a in self.alumnos if a.nombre != nombre]
        print(f"Alumno {nombre} eliminado.")

    def actualizar_alumno(self, nombre, nuevo_nombre=None, nuevo_curso=None, nuevo_profesor_responsable=None):
        for alumno in self.alumnos:
            if alumno.nombre == nombre:
                alumno.actualizar_datos(nuevo_nombre, nuevo_curso, nuevo_profesor_responsable)
                print(f"Alumno {nombre} actualizado.")
                return
        print(f"Alumno {nombre} no encontrado.")

    def listar_alumnos(self):
        return [str(a) for a in self.alumnos]

# Ejemplo de uso
if __name__ == "__main__":
    # Crear la escuela
    escuela = Escuela("Escuela Central", "Madrid", "Juan Pérez")

    # Agregar profesores
    escuela.agregar_profesor("María López", "ciencias")
    escuela.agregar_profesor("Carlos García", "letras")

    # Agregar alumnos
    escuela.agregar_alumno("Ana Torres", "3A", "María López")
    escuela.agregar_alumno("Luis Fernández", "4B", "Carlos García")

    # Listar profesores y alumnos
    print("\nProfesores en la escuela:")
    print("\n".join(escuela.listar_profesores()))

    print("\nAlumnos en la escuela:")
    print("\n".join(escuela.listar_alumnos()))

    # Actualizar profesor y alumno
    escuela.actualizar_profesor("María López", nuevo_tipo="mixto")
    escuela.actualizar_alumno("Ana Torres", nuevo_curso="4A")

    # Eliminar profesor y alumno
    escuela.eliminar_profesor("Carlos García")
    escuela.eliminar_alumno("Luis Fernández")

    # Estado final de la escuela
    print("\nEstado final de la escuela:")
    print(escuela)
