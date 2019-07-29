from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Photography(Base):

	__tablename__ = "Mygear"
	client_id = Column(Integer , primary_key = True )
	name = Column(String)
	budget = Column(Integer)
	Will_buy = Column(Boolean)	
	
	def __repr__(self):
		return ( "name : {}\n"
				 "budget : {}\n"
				 "Will_buy : {} ").format(
				 self.name , self.budget , self.Will_buy )



