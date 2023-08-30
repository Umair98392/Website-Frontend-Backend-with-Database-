#SQLAchhemy model  is used for handle request in a tables of a databse.
#SQLAlchemy models define attributes using '=' and pass the type as a parameter to Column, 
#like in: name = Column(String)
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

#importing base class to inherit
from .database import Base

#SQLAlchemy models are Python classes that define the structure and behavior of your 
#database tables in an object-oriented manner. which allows you to work with databases 
#using Python objects and code rather than writing raw SQL queries.

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")
