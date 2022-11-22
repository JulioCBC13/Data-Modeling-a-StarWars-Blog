import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String , Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    usuario = relationship(Usuario)

class Personajes(Base):
    __tablename__ = 'personajes'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    person_class = Column(String(250))
    faccion = Column(String(250))
    raza = Column(String(250))
        
class Planetas(Base):
    __tablename__ = 'planetas'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    color = Column(String(250))
    temperatura = Column(Float)
    mooncount= Column(String(250))

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    vehicle_class = Column(String(250))
    model = Column(String(250))
    brand = Column(String(250))
    price = Column(Float(250))
    passenger = Column(Integer)

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    vehicles_favorites_id = Column(Integer, ForeignKey('vehicles.id'), nullable=True)
    vehicles_favorites = relationship(Vehicles)
    user_favorites_id = Column(Integer, ForeignKey('usuario.id'), nullable=True)
    user_favorites = relationship(Usuario)
    personajes_favorites_id = Column(Integer, ForeignKey('personajes.id'), nullable=True)
    personajes_favorites = relationship(Personajes)
    planetas_favorites_id = Column(Integer, ForeignKey('planetas.id'), nullable=True)
    planetas_favorites = relationship(Planetas)

 
    

    # def to_dict(self):
    #     return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
