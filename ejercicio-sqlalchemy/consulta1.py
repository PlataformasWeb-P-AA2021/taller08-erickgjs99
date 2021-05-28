from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ 

from generar_tabla import Mundial

engine = create_engine('sqlite:///taller8.db')

Session = sessionmaker(bind=engine)
session = Session()

# Crear un archivo que permita presentar todos los jugadores, ordenados por el número de goles.
goles_jugadores = session.query(Mundial).order_by(Mundial.goals).all()
print(goles_jugadores)
