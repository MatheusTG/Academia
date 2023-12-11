from infra.configs.base import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

class Treino(Base):
  __tablename__ = 'treino'

  treino_id = Column(Integer, primary_key=True)
  frequencia = Column(Integer, nullable=False)
  objetivo = Column(String, nullable=False)
  # treino_diario = relationship('TreinoDiario', backref='treino_diario', lazy='subquery')

  def __repr__(self):
    return f''' 
      treino_id {self.treino_id}
      Frequência {self.frequencia}
      Objetivo {self.objetivo}
    '''