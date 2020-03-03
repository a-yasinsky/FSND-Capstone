from sqlalchemy import Column, String, Integer
import json
from . import db

class Housing(db.Model):
  __tablename__ = 'housing'

  id = Column(Integer, primary_key=True)
  name = Column(String)
  description = Column(String)

  def __init__(self, name, description):
    self.name = name
    self.description = description

  def format(self):
    return {
      'id': self.id,
      'name': self.name,
      'description': self.description
    }

class Category(db.Model):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name

class Photo(db.Model):
    __tablename__ = 'photos'

    id = Column(Integer, primary_key=True)
    link = Column(String)

    def __init__(self, link):
        self.link = link

class Locality(db.Model):
    __tablename__ = 'localities'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name

class Contact(db.Model):
    __tablename__ = 'contacts'

    id = Column(Integer, primary_key=True)
    adress = Column(String)
    tel_number = Column(String)
    email = Column(String)
    instagram = Column(String)
    facebook = Column(String)

class RoomType(db.Model):
    __tablename__ = 'room_types'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
