from infra.repository.treino_repository import TreinoRepository
from infra.repository.clientes_repository import ClienteRepository
from infra.repository.plano_repository import PlanoRepository
from infra.repository.treino_diario_repository import TreinoDiarioRepository
from infra.repository.franquia_repository import FranquiaRepository
from infra.repository.exercicio_repository import ExercicioRepository

from infra.entities import *

# Consultas Matheus =============

# Matheus01 - Selecione o plano de todos os clientes da academia
response_matheus_01 = ClienteRepository() \
  .select(Cliente.nome, Plano.nome) \
  .join(Plano, Cliente.plano_id == Plano.plano_id) \
  .all()

# Matheus02 - Selecione o objetivo de todos os clientes que pesam mais de 80kg
response_matheus_02 = ClienteRepository() \
  .select(Cliente.nome, Treino.objetivo, Cliente.peso) \
  .join(Treino, Cliente.treino_id == Treino.treino_id) \
  .filter(Cliente.peso > 80) \
  .all()

# Matheus03 - Selecione o nome e cpf de todos os clientes que moram em Campo Mourão
# e ordene por ondem crescente de nome
response_matheus_03 = ClienteRepository() \
  .select(Cliente.nome, Cliente.cpf, Cidade.nome) \
  .join(Franquia, Cliente.franquia_id == Franquia.franquia_id) \
  .join(Cidade, Franquia.cidade_id == Cidade.cidade_id) \
  .filter(Cidade.nome == 'Campo Mourão') \
  .order_by(Cliente.nome) \
  .all()

# Consultas Roberto =============

# Roberto01 - Selecione o nome do cliente e o sobrenome do cliente, que tenha o plano semestral
response_roberto_01 = ClienteRepository() \
  .select(Cliente.nome, Cliente.sobrenome) \
  .join(Plano, Cliente.plano_id == Plano.plano_id)\
  .filter(Plano.nome == 'Semestral')\
  .order_by(Cliente.nome, Cliente.sobrenome).all()


# Roberto02 - Selecione o nome do proprietario da franquia/s localizada/s em Campo Mourão
response_roberto_02 = FranquiaRepository() \
  .select(Franquia.proprietario, Cidade.nome)\
  .join(Cidade, Franquia.cidade_id == Cidade.cidade_id)\
  .filter(Cidade.nome == 'Campo Mourão').all()
  
# Roberto03 - Selecione o nome, sobrenome, o objetivo do cliente que tenha o objetivo de 'ganhar massa muscular'
response_roberto_03 = ClienteRepository() \
    .select(Cliente.nome, Cliente.sobrenome, Treino.objetivo) \
    .join(Treino, Cliente.treino_id == Treino.treino_id) \
    .filter(Treino.objetivo == 'ganhar massa muscular') \
    .order_by(Cliente.nome, Cliente.sobrenome).all()

# Consultas Valmir =============

# Valmir01 - Retorne todos os clientes, junto com sua respectiva frequência de treino semanal.
response_valmir_01 = ClienteRepository() \
  .select(Cliente.nome, Treino.frequencia, Treino.objetivo) \
  .join(Treino, Cliente.treino_id == Treino.treino_id) \
  .all()

# Valmir02 - Retorne todos os clientes e se ele faz cardio ou não no seu primeiro treino da semana, juntamente com o seu objetivo de treino.
response_valmir_02 = ClienteRepository() \
  .select(Cliente.nome, TreinoDiario.cardio, Treino.objetivo) \
  .join(Treino, Cliente.treino_id == Treino.treino_id) \
  .join(TreinoDiario, Treino.treino_id == TreinoDiario.treino_id) \
  .all()

# Valmir03 - Retorne os exercícios cadastrados para um treino de Bíceps, ordenados por nome.
response_valmir_03 = ExercicioRepository() \
  .select(Exercicio.nome) \
  .join(GrupoMuscular, Exercicio.grupo_muscular_id == GrupoMuscular.grupo_muscular_id) \
  .filter(GrupoMuscular.nome == "biceps") \
  .order_by(Exercicio.nome).all()

# Consultas Natália

# Natália01 - Retorne o nome e peso das pessoas que pesam mais que 60kg. Ordene alfabeticamente.
response_natalia_01 = ClienteRepository()\
    .select(Cliente.nome, Cliente.peso)\
    .filter(Cliente.peso > 60)\
    .order_by(Cliente.nome).all()

# Natália02 - Retorne o nome e a cidade de cada frequentador da academia. Ordene em ordem alfabética contra.
response_natalia_02 = ClienteRepository()\
  .select(Cliente.nome, Cidade.nome)\
  .join(Franquia, Cliente.franquia_id == Franquia.franquia_id)\
  .join(Cidade, Franquia.cidade_id == Cidade.cidade_id)\
  .order_by(Cidade.nome.desc())\
  .all()

# Natália03 - Retorne o nome das pessoas que possuem como plano o "Mensal".
response_natalia_03 = ClienteRepository() \
    .select(Cliente.nome)\
    .join(Plano, Cliente.plano_id == Plano.plano_id)\
    .filter(Plano.nome == 'Mensal') \
    .all()

# Consultas Amanda

# Amanda01 - Selecione o nome, sobrenome de todos os clientes que tem o objetivo
# de perder peso
response_amanda_01 = ClienteRepository() \
  .select(Cliente.nome,Cliente.sobrenome, Treino.objetivo) \
  .join(Treino,Cliente.treino_id==Treino.treino_id) \
  .filter(Treino.objetivo=="perder peso").all()

# Amanda02 - Selecione todos os exercicios de gluteo em ordem crescente de nome
response_amanda_02 = ExercicioRepository() \
  .select(Exercicio.nome, GrupoMuscular.nome) \
  .join(GrupoMuscular, Exercicio.grupo_muscular_id == GrupoMuscular.grupo_muscular_id) \
  .filter(GrupoMuscular.nome == 'gluteos') \
  .order_by(Exercicio.nome) \
  .all()

# Amanda03 - Selecione o peso de todos os clientes que possuem o plano semestral
response_amanda_03 = ClienteRepository() \
  .select(Cliente.nome, Cliente.peso) \
  .join(Plano, Cliente.plano_id == Plano.plano_id) \
  .filter(Plano.nome == 'Semestral')

for tupla in response_amanda_03:
  print(tupla)