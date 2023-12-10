from infra.repository.repository_tool import RepositoryTool
from infra.entities.franquia import Franquia


class FranquiaRepository(RepositoryTool):
  def __init__(self):
    super().__init__(Franquia)