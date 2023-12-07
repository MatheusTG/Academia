from infra.configs.base import Base
from sqlalchemy import Column, String, Integer, ForeignKey

class GrupoTreino(Base):
  __tablename__ = 'grupo_treino'

  grupo_treino_id = Column(Integer, primary_key=True)
  treino_diario_id = Column(Integer, ForeignKey('treino_diario.treino_diario_id'))
  grupo_muscular_id = Column(Integer, ForeignKey('grupo_muscular.grupo_muscular_id'))

  def __repr__(self):
    return (self.__tablename__)
