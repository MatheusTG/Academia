from infra.configs.base import Base
from sqlalchemy import Column, String, Integer

class Plano(Base):
  __tablename__ = 'plano'

  plano_id = Column(Integer, primary_key=True)
  duracao= Column(String, nullable=False)
  preco = Column(String, nullable=False)
  nome=Column(String, nullable=False)

  def __repr__(self):
    return f''' 
      plano_id {self.plano_id}
      Duração {self.duracao}
      Preço {self.preco}
      Nome {self.nome}
    '''

