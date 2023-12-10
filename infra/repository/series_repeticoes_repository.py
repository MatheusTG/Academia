from infra.repository.repository_tool import RepositoryTool
from infra.entities.series_repeticoes import SeriesRepeticoes


class SeriesRepeticoesRepository(RepositoryTool):
  def __init__(self):
    super().__init__(SeriesRepeticoes)