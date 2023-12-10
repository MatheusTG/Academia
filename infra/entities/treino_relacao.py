from infra.configs.base import Base
from sqlalchemy import Column, String, Integer, ForeignKey

class TreinoRelacao(Base):
  __tablename__ = 'treino_relacao'

  treino_id = Column(Integer, ForeignKey('treino.treino_id'), primary_key=True)
  treino_diario_id = Column(Integer, ForeignKey('treino_diario.treino_diario_id'), primary_key=True)

  def __repr__(self):
    return (self.__tablename__)

