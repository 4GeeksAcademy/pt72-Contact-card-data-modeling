import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()
# starwars
    # user
    # favorites
    # characters
    # planets
# instagram
    # user
    # followers
    # post
    # media
    # comment
    # likes
# contact card
    # user/agenda
    # contact
    # inner circle
    
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(550), nullable=False)

    contacts = relationship('Contact', back_populates="user")
    favorites = relationship('Favorites', back_populates="user")

class Contact(Base):
    __tablename__ = 'contact'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(550), nullable=False)
    address = Column(String(250))
    phone = Column(String(250))

    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    def to_dict(self):
        return {}
    
class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    contact_id = Column(Integer, ForeignKey('contact.id'))
    contact = relationship(Contact)


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
