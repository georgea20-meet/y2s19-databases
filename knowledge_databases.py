from knowledge_model import Base, Photography

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(name,budget,Will_buy):
	x = Photography(name = name , budget = budget, Will_buy = Will_buy)
	session.add(x)
	session.commit()

add_article("Elie",2000 ,True)

def query_all_articles():
	photographer = session.query(Photography).first()
	return photographer

print(query_all_articles())

def query_article_by_name(name):
	photographer = session.query(Photography).filter_by(name = name).first()
	return photographer 

query_article_by_name("Elie")

def delete_article_by_name(name):
	session.query(Photography).filter_by(name = name ).delete()
	session.commit()

delete_article_by_name("Elie")

def delete_all_articles(name):
	pass

def edit_article_rating():
	pass
