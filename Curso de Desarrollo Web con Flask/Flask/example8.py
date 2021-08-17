import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

directory = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(directory, 'pets.sqlite')
app.config['SQLACHEMY_TRACK_MODIFICATIONS'] = False

dataBase = SQLAlchemy(app)

Migrate(app, dataBase)

class Pet(dataBase.Model):
    __tablename__  = 'Pets'
    id = dataBase.Column(dataBase.Integer, primary_key = True)
    name = dataBase.Column(dataBase.Text)
    toys = dataBase.relationship('Toy', backref='pet', lazy='dynamic')
    owners = dataBase.relationship('Owner', backref='pet', uselist=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        text  = "Pet: name {}".format(self.name)
        return text

    def show_toy(self):
        for toy in self.toys:
            print(toys.name)

class Toy(dataBase.Model):
    __tablename__ = 'Toys'
    id = dataBase.Column(dataBase.Integer, primary_key=True)
    name = dataBase.Column(dataBase.Text)
    id_pet = dataBase.Column(dataBase.Integer, dataBase.ForeignKey('Pets.id'))

    def __init__(self, name, id_pet):
        self.name = name
        self.id_pet = id_pet

class Owner(dataBase.Model):
    __tablename__ = 'Owners'
    id = dataBase.Column(dataBase.Integer, primary_key=True)
    name = dataBase.Column(dataBase.Text)
    id_pet = dataBase.Column(dataBase.Integer, dataBase.ForeignKey('Pets.id'))

    def __init__(self, name, id_pet):
        self.name  = name
        self.id_pet = id_pet
