from infra.repository.repository_tool import RepositoryTool
from infra.entities.exercicio import Exercicio


class ExercicioRepository(RepositoryTool):
  def __init__(self):
    super().__init__(Exercicio)
