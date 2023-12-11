from infra.configs.base import Base
from sqlalchemy import Column, String, Integer, ForeignKey

class SeriesRepeticoes(Base):
  __tablename__ = 'series_repeticoes'

  grupo_treino_id = Column(Integer, ForeignKey('grupo_treino_diario.grupo_treino_id'), primary_key=True)
  exercicio_id = Column(Integer, ForeignKey('exercicio.exercicio_id'), primary_key=True)
  series = Column(Integer, nullable=False)
  repeticoes = Column(Integer, nullable=False)

  def __repr__(self):
    return f''' 
      grupo_treino_id {self.grupo_treino_id}
      exercicio_id {self.exercicio_id}
      Series {self.series}
      Repetições {self.repeticoes}
    '''