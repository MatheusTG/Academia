from infra.configs.base import Base
from sqlalchemy import Column, String, Integer

class Treinos(Base):
  __tablename__ = 'treinos'

  treino_id = Column(Integer, primary_key=True)
  frequencia = Column(Integer, nullable=False)
  objetivo = Column(String, nullable=False)

  def __repr__(self):
    return f'Treino (id_treino={self.treino_id}, frequencia={self.frequencia}, objetivo={self.objetivo})'

