from infra.configs.base import Base
from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, Table
from sqlalchemy.orm import relationship

class TreinoDiario(Base):
  __tablename__ = 'treino_diario'

  treino_diario_id = Column(Integer, primary_key=True)
  cardio = Column(Boolean)
  grupo_muscular_id = relationship('GrupoMuscular', backref='grupo_muscular', lazy='subquery')

  def __repr__(self):
    return f''' 
      treino_diario_id {self.treino_diario_id}
      Cardio {self.cardio}
    '''


association_table = Table(
    "grupo_treino_diario",
    Base.metadata,
    Column('grupo_treino_diario_id', Integer, primary_key=True),
    Column("treino_diario_id", ForeignKey("treino_diario.treino_diario_id")),
    Column("grupo_muscular_id", ForeignKey("grupo_muscular.grupo_muscular_id")),
)