from infra.configs.connection import DBConnectionHandler

class RepositoryTool:
  def __init__(self, table):
    self.table = table

  def select(self):
    with DBConnectionHandler() as db:
      data = db.session.query(self.table).all()
      return data
  
  def insert(self, **kwargs):
    with DBConnectionHandler() as db:
      data_insert = self.table(**kwargs)
      db.session.add(data_insert)
      db.session.commit()

  def delete(self, attribute, value):
    with DBConnectionHandler() as db:
      db.session.query(self.table).filter(attribute==value).delete()
      db.session.commit()

  def update(self, attribute, value, change:dict):
    with DBConnectionHandler() as db:
      db.session.query(self.table).filter(attribute==value).update(change)
      db.session.commit()