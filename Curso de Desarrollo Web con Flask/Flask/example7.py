import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#SE CREA EL DIRECTORIO DE NUESTRO ARCHIVO PARA LA BASE DE DATOS
directory = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

#SE CONFIGURA LA BASE DE DATOS Y SE ESTABLECE PARA CREAR EL ALRCHIVO .sqlite
app.config['SQLALCHEMY_DATABASE_URI'] =  'sqlite:///' + os.path.join(directory, 'data.sqlite')

#ESTEBLECEMOS QUE NO HABRÁ MODIFICACIONES EN NUESTRA BASE DE DATOS
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#SE CREA LA BASE DE DATOS POR MEDIO DE UNA INSTANCIA DE LA CLASE SQLAlchemy CON PARAMETRO
# NUESTRA APP
dataBase = SQLAlchemy(app)

#SE UTILIZA ESTE MÉTODO Migrate PARA QUE SE PUEDAN ENVIAR LAS ACTUALIZACIONES CORRESPONDIENTES DE LA TABLA
# A LA BASE DE DATOS SIN NECESIDAD DE REHACERLA
Migrate(app, dataBase)

#SE CREA NUESTRA TABLA CON LOS DATOS QUE TENDRAN EN SUS COLUMNAS
class Person(dataBase.Model):
    #SE ESTABLECE EL NOMBRE DE NUESTRA TABLA PERO NO ES NECESARIO YA
    #QUE EL  NOMBRE ESTABLECIDO EN LA class SERÍA EL DE NUESTRA TABLA
    __tablename__ = 'Persons'

    id = dataBase.Column(dataBase.Integer, primary_key = True)
    name = dataBase.Column(dataBase.Text)
    age = dataBase.Column(dataBase.Integer)
    country = dataBase.Column(dataBase.Text)

    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    def __repr__(self):
        text = "Person: {} is {} from {}".format(self.name, self.age, self.country)
        return text
