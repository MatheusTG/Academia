from infra.repository.repository_tool import RepositoryTool
from infra.entities.cliente import Cliente


class ClienteRepository(RepositoryTool):
  def __init__(self):
    super().__init__(Cliente)
