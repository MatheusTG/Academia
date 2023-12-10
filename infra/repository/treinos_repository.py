from infra.configs.connection import DBConnectionHandler
from infra.entities.treino import Treino

class TreinosRepository:
  def select(self):
    with DBConnectionHandler() as db:
      data = db.session.query(Treino).all()
      return data
  
  def insert(self, treino_id, frequencia, objetivo):
    with DBConnectionHandler() as db:
      data_insert = Treino(treino_id=treino_id, frequencia=frequencia, objetivo=objetivo)
      db.session.add(data_insert)
      db.session.commit()

  # def delete(self, titulo):
  #   with DBConnectionHandler() as db:
  #     db.session.query(Treinos).filter(Treinos.titulo==titulo).delete()
  #     db.session.commit()

  # def update(self, titulo, ano):
  #   with DBConnectionHandler() as db:
  #     db.session.query(Treinos).filter(Treinos.titulo==titulo).update({'ano': ano})
  #     db.session.commit()