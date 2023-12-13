from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from infra.configs.base import Base

class DBConnectionHandler:
  def __init__(self):
    self.__connection_string = 'postgresql://postgres:matheus0604@localhost:5432/academia'
    self.__engine = self.__create_database_engine()
    self.session = None 

  def __create_database_engine(self):
    engine = create_engine(self.__connection_string)
    if not database_exists(engine.url):
      create_database(engine.url)
      Base.metadata.create_all(engine)
    return engine

  def get_engine(self):
    return self.__engine
  
  def __enter__(self):
    session_make = sessionmaker(bind=self.__engine)
    self.session = session_make()
    return self

  def __exit__(self, exc_type, exc_val, exc_tb):
    self.session.close()
