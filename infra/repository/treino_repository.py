from infra.repository.repository_tool import RepositoryTool
from infra.entities.treino import Treino

class TreinoRepository(RepositoryTool):
  def __init__(self):
    super().__init__(Treino)
