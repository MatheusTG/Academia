from infra.repository.repository_toll import RepositoryToll
from infra.entities.cliente import Cliente

class CLienteRepository(RepositoryToll):
  def __init__(self):
    super().__init__(Cliente)
