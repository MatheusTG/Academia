from infra.repository.repository_tool import RepositoryTool
from infra.entities.grupo_muscular import GrupoMuscular


class GrupoMuscularRepository(RepositoryTool):
  def __init__(self):
    super().__init__(GrupoMuscular)