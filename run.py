from infra.repository.treinos_repository import TreinosRepository
from infra.configs.base import Base
from infra.configs.connection import DBConnectionHandler

repo = TreinosRepository()

# repo.insert(1, 3, 'Ganhar massa')
# repo.insert(2, 4, 'Perder peso')

data = repo.select()
  
print(data)