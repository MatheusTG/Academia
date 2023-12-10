from infra.repository.repository_tool import RepositoryTool
from infra.entities.plano import Plano

class PlanoRepository(RepositoryTool):
  def __init__(self):
    super().__init__(Plano)
