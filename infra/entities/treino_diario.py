from xmlrpc.client import Boolean, boolean
from infra.configs.base import Base
from sqlalchemy import Column, String, Integer, ForeignKey, Boolean

class TreinoDiario(Base):
  __tablename__ = 'treino_diario'

  treino_diario_id = Column(Integer, primary_key=True)
  cardio = Column(Boolean)

  def __repr__(self):
    return f''' 
      treino_diario_id {self.treino_diario_id}
      Cardio {self.cardio}
    '''