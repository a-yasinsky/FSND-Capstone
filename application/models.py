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
  photos = db.relationship('Photo',
                            backref='housing',
                            cascade = "all, delete, delete-orphan",
                            lazy=True)
  room_types = db.relationship('RoomType',
                                backref='housing',
                                cascade = "all, delete, delete-orphan",
                                lazy=True)
  contacts = db.relationship('Contact',
                            backref='housing',
                            lazy=True,
                            uselist=False,
                            cascade = "all, delete, delete-orphan")

  def __init__(self, name, description, locality, category):
    self.name = name
    self.description = description
    self.locality_id = locality
    self.category_id = category

  def insert(self, photos, room_types, contacts):
      db.session.add(self)

      for link in photos:
          photo = Photo(link)
          self.photos.append(photo)
          db.session.add(photo)

      for room_type in room_types:
          r_type = RoomType(room_type['name'], room_type['price'])
          self.room_types.append(r_type)
          db.session.add(r_type)

      contacts_ins = Contact(**contacts)
      self.contacts = contacts_ins
      db.session.add(contacts_ins)

      db.session.commit()

  def update_photos(self, photos):
      to_remove = []
      detect_append = []
      for photo in self.photos:
          if photo.link not in photos:
              to_remove.append(photo)
          else:
              detect_append.append(photo.link)
      for photo in photos:
          if photo not in detect_append:
              new_photo = Photo(photo)
              self.photos.append(new_photo)
              db.session.add(new_photo)

      for removable_link in to_remove:
          self.photos.remove(removable_link)

  def create_mapper(self, room_types):
      return {rt['id']: rt for rt in room_types if 'id' in rt}

  def update_room_types(self, room_types):
      room_id_mapper = self.create_mapper(room_types)
      to_remove = []
      to_append  = []
      for room_type in self.room_types:
          if room_type.id in room_id_mapper:
              new_room_type = room_id_mapper[room_type.id]
              if "name" in new_room_type:
                room_type.name = new_room_type['name']
              if "price" in new_room_type:
                room_type.price = new_room_type['price']
              to_append.append(room_type.id)
          else:
              to_remove.append(room_type)

      for removable_link in to_remove:
          self.room_types.remove(removable_link)

      for room_type in room_types:
          if 'id' not in room_type and 'name' in room_type and 'price' in room_type:
              new_room_type = RoomType(room_type['name'], room_type['price'])
              self.room_types.append(new_room_type)
              db.session.add(new_room_type)


  def update(self, photos, room_types, contacts):
      self.update_photos(photos)
      self.update_room_types(room_types)
      if self.contacts:
          self.contacts.query.update(contacts)
      else:
          contacts_ins = Contact(**contacts)
          self.contacts = contacts_ins
          db.session.add(contacts_ins)
      db.session.commit()

  def delete(self):
      db.session.delete(self)
      db.session.commit()

  @classmethod
  def getSearchResults(self, search_term = ''):
      return Housing.query.filter(
        db.func.concat(Housing.name, ' ', Housing.description).ilike(
          '%' + search_term + '%'
        )
      ).all()

  def format(self):
    return {
      'id': self.id,
      'name': self.name,
      'description': self.description,
      'locality': self.locality.name,
      'category': self.category.name,
      'photos': [photo.link for photo in self.photos],
      'room_types': [r_t.format() for r_t in self.room_types],
      'contacts': self.contacts.format() if self.contacts else None
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
    housing_id = Column(Integer, db.ForeignKey('housing.id'), nullable=False)
    adress = Column(String)
    tel_number = Column(String)
    email = Column(String)
    instagram = Column(String)
    facebook = Column(String)

    def format(self):
        return {
            'adress': self.adress,
            'tel_number': self.tel_number,
            'email': self.email,
            'instagram': self.instagram,
            'facebook': self.facebook
        }

class RoomType(db.Model):
    __tablename__ = 'room_types'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    housing_id = Column(Integer, db.ForeignKey('housing.id'), nullable=False)

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price
        }
