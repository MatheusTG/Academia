from infra.configs.base import Base
from sqlalchemy import Column, String, Integer, ForeignKey

class Franquia(Base):
  __tablename__ = 'franquia'
  
  franquia_id = Column(Integer, primary_key=True)
  cidade_id = Column(Integer, ForeignKey('cidade.cidade_id'))
  proprietario = Column(String, nullable=False)
  telefone = Column(String, nullable=False)
  bairro = Column(String, nullable=False)
  rua = Column(String, nullable=False)
  numero = Column(Integer, nullable=False)
  financeiro_id = Column(Integer, ForeignKey('financeiro.financeiro_id'))
  
  def __repr__(self):
    return (self.__tablename__)