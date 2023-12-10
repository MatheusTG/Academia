from infra.repository.repository_tool import RepositoryTool
from infra.entities.cliente import Cliente

class CLienteRepository(RepositoryTool):
  def __init__(self):
    super().__init__(Cliente)
