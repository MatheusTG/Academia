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

import json

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

    treino_cliente = ClienteRepository() \
    .select(Cliente.nome, Treino.objetivo, Treino.frequencia) \
    .join(Treino, Cliente.treino_id == Treino.treino_id) \
    .filter(Cliente.cpf == request.args.get('cpf')) \
    .all()

    nome = treino_cliente[0][0]
    objetivo = treino_cliente[0][1]
    frequencia = treino_cliente[0][2]

    user_dados = {
      'nome': nome,
      'objetivo': objetivo,
      'frequencia': frequencia,
    }     

    with open('data/user.json', 'w') as file:
      json.dump(user_dados, file)

    return render_template('treinos.html', nome=nome, objetivo=objetivo.capitalize(), frequencia=frequencia)
  return render_template('cadastro.html')

@app.route('/login.html', methods=['GET', 'POST'])
def login():
  if request.method == 'GET':
    data_cliente = ClienteRepository() \
      .select(Cliente.nome, Cliente.email, Cliente.senha, Treino.objetivo, Treino.frequencia) \
      .join(Treino, Cliente.treino_id == Treino.treino_id) \
      .filter(Cliente.email == request.args.get('email')) \
      .all()

    print(data_cliente)
    if data_cliente:
      if data_cliente[0][2] == request.args.get('senha'):
        nome = data_cliente[0][0]
        objetivo = data_cliente[0][3]
        frequencia = data_cliente[0][4]

        data_cliente_dict = {
          'nome':nome,
          'objetivo': objetivo,
          'frequencia': frequencia,
        }

        with open('data/user.json', 'w') as file:
          json.dump(data_cliente_dict, file)
        return render_template('treinos.html', nome=nome, objetivo=objetivo.capitalize(), frequencia=frequencia)

  return render_template('login.html')

@app.route('/treinos.html')
def treinos():
  with open('data/user.json', 'r') as file:
    user_dados = json.load(file)
  
  nome = user_dados['nome']
  objetivo = user_dados['objetivo']
  frequencia = user_dados['frequencia']

  return render_template('treinos.html', nome=nome, objetivo=objetivo.capitalize(), frequencia=frequencia)

if __name__ == '__main__':
  app.run(debug=True)
