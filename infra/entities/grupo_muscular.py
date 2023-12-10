from infra.configs.base import Base
from sqlalchemy import Column, String, Integer, ForeignKey

class GrupoMuscular(Base):
  __tablename__ = 'grupo_muscular'

  grupo_muscular_id = Column(Integer, primary_key=True)
  nome = Column(String, nullable=False)
  categoria = Column(String, nullable=False)

  def __repr__(self):
    return f''' 
      grupo_muscular_id {self.grupo_muscular_id}
      Nome do Músculo {self.nome}
      Categoria {self.categoria}
    '''