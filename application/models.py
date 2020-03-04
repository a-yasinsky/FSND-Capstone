from sqlalchemy import Column, String, Integer
import json
from . import db

class Housing(db.Model):
  __tablename__ = 'housing'

  id = Column(Integer, primary_key=True)
  name = Column(String)
  description = Column(String)
  locality_id = db.Column(db.Integer, db.ForeignKey('localities.id'),
                nullable=False)
  category_id = db.Column(db.Integer, db.ForeignKey('categories.id'),
                nullable=False)
  photos = db.relationship('Photo', backref='housing', lazy=True)
  room_types = db.relationship('RoomType', backref='housing', lazy=True)

  def __init__(self, name, description, locality, category):
    self.name = name
    self.description = description
    self.locality_id = locality
    self.category_id = category

  def insert(self, photos, room_types):
      db.session.add(self)

      for link in photos:
          photo = Photo(link)
          self.photos.append(photo)
          db.session.add(photo)

      for room_type in room_types:
          r_type = RoomType(room_type['name'], room_type['price'])
          self.room_types.append(r_type)
          db.session.add(r_type)

      db.session.commit()

  def format(self):
    return {
      'id': self.id,
      'name': self.name,
      'description': self.description,
      'locality': self.locality.name,
      'category': self.category.name,
      'photos': [photo.link for photo in self.photos],
      'room_types': [r_t.name for r_t in self.room_types]
    }

class Category(db.Model):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    housing = db.relationship('Housing', backref='category', lazy=True)

    def __init__(self, name):
        self.name = name

class Photo(db.Model):
    __tablename__ = 'photos'

    id = Column(Integer, primary_key=True)
    link = Column(String)
    housing_id = Column(Integer, db.ForeignKey('housing.id'), nullable=False)

    def __init__(self, link):
        self.link = link

class Locality(db.Model):
    __tablename__ = 'localities'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    housing = db.relationship('Housing', backref='locality', lazy=True)

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
    housing_id = Column(Integer, db.ForeignKey('housing.id'), nullable=False)

    def __init__(self, name, price):
        self.name = name
        self.price = price
