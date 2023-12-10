from infra.repository.repository_tool import RepositoryTool
from infra.entities.financeiro import Financeiro


class FinanceiroRepository(RepositoryTool):
  def __init__(self):
    super().__init__(Financeiro)