#!/usr/bin/python3
""" State Module for HBNB project """
import models
from os import getenv
from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=True)
    cities = relationship('City', backref='state', cascade='all, delete-orphan')

    if getenv("HBNB_TYPE_STORAGE") != "db":

        @property
        def cities(self):
            city_lis=[]
            for city in (models.storage.all(City).values()):
                if city.state_id == self.id:
                    city_lis.append(city)

            return city_lis