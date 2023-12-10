from infra.repository.repository_tool import RepositoryTool
from infra.entities.cidade import Cidade


class CidadeRepository(RepositoryTool):
  def __init__(self):
    super().__init__(Cidade)
