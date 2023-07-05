#
#   API done with repl
#   I uploaded a excel archive with data 
#
import pandas as pd
from flask import Flask, jsonify

#inicializando o flask
app = Flask(__name__)

#Funcionalidades
@app.route('/')
def homepage():
  return 'A API está funcionando'

@app.route('/pegar_vendas')
def pegarVendas():

  tabela = pd.read_csv('criandoAPI_python.csv')
  total_vendas = tabela['Vendas'].sum()
  resposta = total_vendas

  return jsonify(resposta)




# rodar a api
app.run(host='0.0.0.0')
