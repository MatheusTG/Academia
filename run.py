from infra.repository.treino_repository import TreinoRepository
from infra.repository.clientes_repository import CLienteRepository
from infra.repository.plano_repository import PlanoRepository

from infra.configs.base import Base
from infra.configs.connection import DBConnectionHandler

import infra.entities # Carrega as classes
from infra.entities import *

from flask import Flask, render_template

db = DBConnectionHandler()

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/planos.html')
def planos():
  return render_template('planos.html')

@app.route('/cadastro.html')
def cadastro():
  return render_template('cadastro.html')

@app.route('/treinos.html')
def treinos():
  return render_template('treinos.html')

if __name__ == '__main__':
  app.run(debug=True)