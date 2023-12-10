from infra.repository.repository_tool import RepositoryTool
from infra.entities.treino_diario import TreinoDiario


class TreinoDiarioRepository(RepositoryTool):
  def __init__(self):
    super().__init__(TreinoDiario)