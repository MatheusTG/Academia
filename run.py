from infra.repository.treino_repository import TreinoRepository
from infra.repository.clientes_repository import ClienteRepository
from infra.repository.plano_repository import PlanoRepository
from infra.repository.treino_diario_repository import TreinoDiarioRepository
from infra.repository.franquia_repository import FranquiaRepository

from infra.configs.base import Base
from infra.configs.connection import DBConnectionHandler

import infra.entities # Carrega as classes
from infra.entities import *

from flask import Flask, render_template, request

from random import randint

db = DBConnectionHandler()

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
    repo_cliente = ClienteRepository()

    repo_cliente.insert(
      cpf=request.args.get('cpf'),
      nome=request.args.get('nome'),
      sobrenome=request.args.get('sobrenome'),
      telefone=request.args.get('telefone'),
      email=request.args.get('email'),
      peso=request.args.get('peso'),
      senha=request.args.get('senha'),
      data_nasc=request.args.get('data-nasc'),
      plano_id=randint(1, len(PlanoRepository().select(Plano.plano_id).all())),
      franquia_id=randint(1, len(FranquiaRepository().select(Franquia.franquia_id).all())),
      treino_id=randint(1, len(TreinoRepository().select(Treino.treino_id).all())),
    )
  return render_template('cadastro.html')

@app.route('/login.html', methods=['GET', 'POST'])
def login():
  return render_template('login.html')

@app.route('/treinos.html')
def treinos():
  return render_template('treinos.html')

if __name__ == '__main__':
  app.run(debug=True)
