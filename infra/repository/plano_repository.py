from infra.repository.repository_toll import RepositoryToll
from infra.entities.plano import Plano

class PlanoRepository(RepositoryToll):
  def __init__(self):
    super().__init__(Plano)
