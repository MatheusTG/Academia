from infra.repository.treino_repository import TreinoRepository
from infra.repository.clientes_repository import CLienteRepository
from infra.repository.plano_repository import PlanoRepository

from infra.configs.base import Base
from infra.configs.connection import DBConnectionHandler

import infra.entities # Carrega as classes
from infra.entities import *

from flask import Flask, render_template, request

db = DBConnectionHandler()

# repo_treino = TreinoRepository()
# repo_treino.insert(
#   treino_id=1,
#   frequencia=5,
#   objetivo='Gnhar massa'
# )

# repo_plano = PlanoRepository()
# repo_plano.insert(
#   plano_id=1,
#   duracao=1,
#   preco='R$ 89,90',
#   nome='mensal',
# )

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
  if request.method == 'GET':
    user = request.args.get('frequencia')
  return render_template('index.html')

@app.route('/planos.html')
def planos():
  return render_template('planos.html')

@app.route('/cadastro.html', methods=['GET', 'POST'])
def cadastro():
  if request.method == 'GET' and request.args:
    repo_cliente = CLienteRepository()

    repo_cliente.insert(
      cpf=request.args.get('cpf'),
      nome=request.args.get('nome'),
      sobrenome=request.args.get('sobrenome'),
      telefone=request.args.get('telefone'),
      email=request.args.get('email'),
      peso=request.args.get('peso'),
      senha=request.args.get('senha'),
      data_nasc=request.args.get('data-nasc'),
      plano_id=1,
      treino_id=1,
    )
  return render_template('cadastro.html')

@app.route('/treinos.html')
def treinos():
  return render_template('treinos.html')

if __name__ == '__main__':
  app.run(debug=True)
