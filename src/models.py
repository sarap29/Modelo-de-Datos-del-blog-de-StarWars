import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er


Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name_user = Column(String(20))
    apellidos_user = Column(String(40))
    email_user = Column(String(50))
    contraseña_user = Column(String(50))

class Planetas(Base):
    __tablename__ = 'planetas'
    id = Column(Integer, primary_key=True)
    name_planeta = Column(String(20))
    diameter_planeta = Column(Float)
    gravity_planeta = Column(String(20))
    surface_water_planeta = Column(Integer)

class Personajes(Base):
    __tablename__ = 'personajes'
    id = Column(Integer, primary_key=True)
    name_personaje = Column(String(20))
    height_personaje = Column(Float)
    mass_personaje = Column(Float)
    gender_personaje = Column(String(10))
    created_date_time = Column(DateTime)

class Vehiculos(Base):
    __tablename__ = 'vehiculos'
    id = Column(Integer, primary_key=True)
    name_vehiculo = Column(String(50))
    model_vehiculo = Column(String(50))
    passenger_vehiculo = Column(Integer)

class PlanetasFavoritos(Base):
    __tablename__ = 'planetas_favoritos'
    id = Column(Integer, primary_key=True)
    id_del_usuario = Column(Integer, ForeignKey('user.id')) #almacena el ID del usuario que ha marcado un planeta como favorito.
    user = relationship(User) 
    id_del_planeta = Column (Integer, ForeignKey('planetas.id')) #almacena el ID del planeta que ha sido marcado como favorito.
    planetas = relationship(Planetas)

class PersonajesFavoritos(Base):
    __tablename__ = 'personajes_favoritos'
    id = Column(Integer, primary_key=True)
    id_del_usuario = Column(Integer, ForeignKey('user.id')) 
    user = relationship(User) 
    id_del_personaje = Column (Integer, ForeignKey('personajes.id')) #almacena el ID del personaje que ha sido marcado como favorito.
    personajes = relationship(Personajes)

class VehiculosFavoritos(Base):
    __tablename__ = 'vehiculos_favoritos'
    id = Column(Integer, primary_key=True)
    id_del_usuario = Column(Integer, ForeignKey('user.id')) 
    user = relationship(User) 
    id_del_vehiculo = Column (Integer, ForeignKey('vehiculos.id')) #almacena el ID del vehiculo que ha sido marcado como favorito.
    vehiculos = relationship(Vehiculos)




    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

