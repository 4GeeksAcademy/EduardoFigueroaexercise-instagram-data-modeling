import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Follower(Base):
    __tablename__ = 'follower'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    user_from_id = Column(Integer, primary_key=True)
    user_to_id = Column(String(250), nullable=False)

    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    

class Usuario(Base):
    __tablename__ = 'usuarios'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    firstname = Column(String(250))
    lastname = Column(String(250), nullable=False)
    email = Column(String, unique=True)

    Follower = relationship("follower", backref= "usuario", lazy=True)
    Comment = relationship("comment", backref= "usuario", lazy=True)
    Post = relationship("post", backref= "usuario", lazy=True)


class Comment(Base):
    __tablename__ = 'comment'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    comment_id = Column(Integer, ForeignKey('comment.id'))

    


class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    post_id = Column(Integer, ForeignKey('post.id'))

   
class Media(Base):
    __tablename__ = 'media'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    type = Column(String(250), nullable=False)
    url= Column()
    post_id= Column()
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    comment_id = Column(Integer, ForeignKey('comment.id'))





    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
