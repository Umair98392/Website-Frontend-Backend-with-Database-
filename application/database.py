# Import the SQLAlchemy parts
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Create a database URL for SQLAlchemy
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:12345678@localhost/db"
#In this example, we are "connecting" to a Postgres database


# The engine is responsible for connecting to the database and managing connections.
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# For Creating Database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#we create an instance of the SessionLocal class, this instance will be the actual database session.

Base = declarative_base()
#This function is used to create a base class for your ORM classes (also known as model classes 
# (base class for creating table in db)). 
