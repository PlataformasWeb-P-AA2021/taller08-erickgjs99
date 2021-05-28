#Importación sqlalchmy para trabajar
from ast import Str
from sqlalchemy import column, create_engine, false, null, true
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

# se importa información del archivo configuracion
from configuracion import cadena_base_datos

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Base = declarative_base()

class Mundial(Base):
    __tablename__ = 'mundial'
    cod = Column(Integer, primary_key = True)
    numero = Column(String, nullable = false)
    fifaDisplayName = Column(String, nullable=false)
    country = Column(String, nullable=false)
    lastname = Column(String, nullable=false)
    firstname = Column(String, nullable=false)
    shirt_name = Column(String, nullable=false)
    position = Column(String, nullable=false)
    height = Column(Integer, nullable = false)
    caps = Column(String, nullable = false)
    goals =Column(Integer, nullable = false)

    def __repr__(self):
        return "Mundial: numero: %s - fifaDisplayname: %s - country: %s - lastname: %s - firstname: %s - shirtname: %s - position: %s - height: %d - caps: %s - goals: %d" %(
                self.numero,
                self.fifaDisplayName,
                self.country,
                self.lastname,
                self.firstname,
                self.shirt_name,
                self.position,
                self.height,
                self.caps,
                self.goals
            )

Base.metadata.create_all(engine)