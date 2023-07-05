import requests

link = 'https://minhaapi--felipetkgti.repl.co/pegar_vendas'

requisicao = requests.get(link)

dicionario = requisicao.json()

print(dicionario['total_vendas'])
