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

  def insert(self):
    db.session.add(self)
    db.session.commit()

  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def format(self):
    return {
      'id': self.id,
      'name': self.name,
      'description': self.description
    }
