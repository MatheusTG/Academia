# from infra.configs.base import Base
# from sqlalchemy import Column, String, Integer, ForeignKey

# class GrupoTreinoDiario(Base):
#   __tablename__ = 'grupo_treino_diario'

#   grupo_treino_id = Column(Integer, primary_key=True)
#   treino_diario_id = Column(Integer, ForeignKey('treino_diario.treino_diario_id'))
#   grupo_muscular_id = Column(Integer, ForeignKey('grupo_muscular.grupo_muscular_id'))

#   def __repr__(self):
#     return f''' 
#       grupo_treino_id {self.grupo_treino_id}
#       treino_diario_id {self.treino_diario_id}
#       grupo_muscular_id {self.grupo_muscular_id}
#     '''
