from sqlalchemy import Column, String, Integer, Date, Numeric, ForeignKey
from infra.configs.base import Base

class Cliente(Base):
    __tablename__ = 'cliente'

    cpf = Column(String, primary_key=True)
    nome = Column(String, nullable=False)
    sobrenome = Column(String, nullable=False)
    telefone = Column(String, nullable=False)
    datanac = Column(Date, nullable=False)
    peso = Column(Numeric, nullable=False)
    plano_id = Column(Integer, ForeignKey('plano.plano_id'))
    franquia_id = Column(Integer, ForeignKey('franquia.franquia_id'))
    treino_id = Column(Integer, ForeignKey('treino.treino_id'))

    def __repr__(self):
        return f"{self.__tablename__}({self.cpf})"
