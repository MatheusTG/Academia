from infra.configs.base import Base
from sqlalchemy import Column, Integer

class Financeiro(Base):
  __tablename__ = 'financeiro'
  
  financeiro_id = Column(Integer, primary_key=True)
  ganho_ultimo_mes = Column(Integer, nullable=False)
  gasto_ultimo_mes = Column(Integer, nullable=False)
  
  def __repr__(self):
    return f''' 
      financeiro_id {self.financeiro_id}
      Ganho Último Mês {self.ganho_ultimo_mes}
      Gasto Último Mês {self.gasto_ultimo_mes}
    '''