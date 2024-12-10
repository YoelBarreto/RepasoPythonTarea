from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

Base = declarative_base()

class Profesor(Base):
    __tablename__ = 'profesores'

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    tipo = Column(String, nullable=False)

    alumnos = relationship("Alumno", back_populates="profesor_responsable")

    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def __repr__(self):
        return f"Profesor(id={self.id}, nombre='{self.nombre}', tipo='{self.tipo}')"


class Alumno(Base):
    __tablename__ = 'alumnos'

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    curso = Column(String, nullable=False)
    profesor_id = Column(Integer, ForeignKey('profesores.id'), nullable=True)

    profesor_responsable = relationship("Profesor", back_populates="alumnos")

    def __init__(self, nombre, curso, profesor_responsable=None):
        self.nombre = nombre
        self.curso = curso
        self.profesor_responsable = profesor_responsable

    def __repr__(self):
        return (f"Alumno(id={self.id}, nombre='{self.nombre}', curso='{self.curso}', "
                f"profesor_responsable='{self.profesor_responsable.nombre if self.profesor_responsable else None}')")


class Escuela(Base):
    __tablename__ = 'escuelas'

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    localidad = Column(String, nullable=False)
    responsable = Column(String, nullable=False)

    def __init__(self, nombre, localidad, responsable):
        self.nombre = nombre
        self.localidad = localidad
        self.responsable = responsable

    def __repr__(self):
        return f"Escuela(id={self.id}, nombre='{self.nombre}', localidad='{self.localidad}', responsable='{self.responsable}')"


engine = create_engine('sqlite:///escuela.db', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

if __name__ == "__main__":
    profesor1 = Profesor(nombre="María López", tipo="ciencias")
    profesor2 = Profesor(nombre="Carlos García", tipo="letras")

    alumno1 = Alumno(nombre="Ana Torres", curso="3A", profesor_responsable=profesor1)
    alumno2 = Alumno(nombre="Luis Fernández", curso="4B", profesor_responsable=profesor2)

    session.add(profesor1)
    session.add(profesor2)
    session.add(alumno1)
    session.add(alumno2)
    session.commit()

    print("\nProfesores en la base de datos:")
    for profesor in session.query(Profesor).all():
        print(profesor)

    print("\nAlumnos en la base de datos:")
    for alumno in session.query(Alumno).all():
        print(alumno)

    alumno_a_actualizar = session.query(Alumno).filter_by(nombre="Ana Torres").first()
    if alumno_a_actualizar:
        alumno_a_actualizar.curso = "4A"
        session.commit()
        print(f"\nAlumno actualizado: {alumno_a_actualizar}")

    profesor_a_eliminar = session.query(Profesor).filter_by(nombre="Carlos García").first()
    if profesor_a_eliminar:
        session.delete(profesor_a_eliminar)
        session.commit()
        print(f"\nProfesor eliminado: {profesor_a_eliminar}")

    print("\nEstado final de la base de datos:")
    print("Profesores:")
    for profesor in session.query(Profesor).all():
        print(profesor)

    print("\nAlumnos:")
    for alumno in session.query(Alumno).all():
        print(alumno)
