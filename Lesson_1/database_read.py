# [MRE] python script to read the database
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from database_setup import Base, Restaurant, MenuItem

# [MRE] the create_engine function lets our program know
# which database engine we want to communicate
engine = create_engine('sqlite:///restaurantmenu.db')

#lets bind the engine to the Base class. This command
#just makes the connections between our class definition
# and the correspondig tables within database.
Base.metadata.bind = engine
#Create a sessionmaker object, this establishes a link
#between our code executions and the engine 
DBSession = sessionmaker(bind = engine)
# in orden to CRUD on our database, sqlAlchemy use an 
#interface named a session. this one instance of this
#sesion. bat the things a not send to database until commit
session = DBSession()

items = session.query(Restaurant).all()
itemRest = session.query(MenuItem).all()
for itemR in items:
    print "Restaurant:", itemR.name
    for item in itemRest:
        print item.name , item.price
    print "\n"

