from infra.repository.treinos_repository import TreinosRepository
from infra.repository.clientes_repository import CLienteRepository
from infra.repository.plano_repository import PlanoRepository

from infra.configs.base import Base
from infra.configs.connection import DBConnectionHandler

import infra.entities # Carrega as classes
from infra.entities import *

from infra.entities.cliente import Cliente

db = DBConnectionHandler()

repo_cliente = CLienteRepository()

repo_plano = PlanoRepository()

repo_plano.insert(
  plano_id=2,
  duracao=6,
  preco='R$ 89,90',
  nome='Semestral'
)

# repo_plano.delete(plano.Plano.plano_id, '2')
repo_plano.update(plano.Plano.plano_id, '2', {'nome': 'Valmir', 'duracao': 1})
 