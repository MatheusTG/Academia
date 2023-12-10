from infra.configs.base import Base
from sqlalchemy import Column, String, Integer, ForeignKey

class Exercicio(Base):
  __tablename__ = 'exercicio'

  exercicio_id = Column(Integer, primary_key=True)
  nome = Column(String, nullable=False)
  grupo_muscular_id = Column(Integer, ForeignKey('grupo_muscular.grupo_muscular_id'))

  def __repr__(self):
    return f''' 
      exercicio_id {self.exercicio_id}
      Nome do Exercício {self.nome}
      grupo_muscular_id {self.grupo_muscular_id}
    '''