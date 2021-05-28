import itertools
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del
# archivo genera_tablas
from generar_tabla import Mundial

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

"""
Para abrir los archivos del mundial. !Vamos la Tri Qatar 2022!
"""
openCsv = open('data/mundial2018.csv', 'r', encoding='utf-8')


for i in itertools.islice(openCsv, 1, None):
    texto_mundial = i.split("|")
    texto_final = texto_mundial[len(texto_mundial)-1].split("\n")
    texto_mundial[len(texto_mundial)-1] = texto_final[0]
    session.add(Mundial(numero=texto_mundial[0], fifaDisplayName=texto_mundial[1], country=texto_mundial[2],
                        lastname=texto_mundial[3], firstname=texto_mundial[4], shirt_name=texto_mundial[5], position=texto_mundial[6],
                        height=texto_mundial[7], caps=texto_mundial[8],  goals=texto_mundial[9]))


session.commit()
