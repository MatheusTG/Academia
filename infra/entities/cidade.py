from infra.configs.base import Base
from sqlalchemy import Column, String, Integer

class Cidade(Base):
  __tablename__ = 'cidade'
  
  cidade_id = Column(Integer, primary_key=True)
  nome = Column(String, nullable=False)
  estado = Column(String, nullable=False)
  populacao = Column(String, nullable=False)
  
  def __repr__(self):
    return f''' 
      cidade_id {self.cidade_id}
      Nome da Cidade {self.nome}
      População {self.populacao}
      Estado {self.estado}
    '''