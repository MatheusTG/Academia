from infra.configs.base import Base
from infra.configs.connection import DBConnectionHandler
import infra.entities

with DBConnectionHandler() as db:
  engine = db.get_engine()
  Base.metadata.create_all(engine)