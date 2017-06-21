import sys

# configuration to import modules
# dependency
# create database

# needed for mapper code
from sqlalchemy import Column, ForeignKey, Integer, String

# needed for class and configuration
from sqlalchemy.ext.declarative import declarative_base

# needed for foreign key relationships
from sqlalchemy.orm import relationship

# needed for configuration
from sqlalchemy import  create_engine


# setup for class code
# tells python that our classes are special classes
Base = declarative_base()

'''
-----------
|name| id |
-----------
'''
# inherits from Base clas
class Restaurant(Base):

    # instance variable
    __tablename__ = "restaurant"

    # max 80 chars and it has to contain a name
    name = Column(String(80), nullable=False)

    # id of this restaurant and is the primary key
    id = Column(Integer, primary_key=True)


'''
                                            Foreign Key
---------------------------------------------------------
|name| id | course | description | price | restaurant_id |
---------------------------------------------------------
'''
# inherits from Base

class Menuitem(Base):

    __tablename = "menu_item"

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)

    course = Column(String(250))
    description = Column(String(250))
    price = Column(String(8))
    # Foreign key the restaurant table and id column
    restaurant_id = Column(Integer, ForeignKey("restaurant.id"))

    # Restaurant has-a MenuItem
    restaurant = relationship(Restaurant)


#### end of file ####
engine = create_engine("sqlite//restaurantmenu.db")

Base.metadata.create_all(engine)