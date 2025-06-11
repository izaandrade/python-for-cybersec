from urllib import response
import requests
import json # importar  json transforma a resposta de string para dictionary, o que ajuda a filtrar o que é API e o que não é

category = 'money'
r = requests.get(f'https://api.chucknorris.io/jokes/random?category={category}')

r = r.json()
punchline = r['value']

print(f'I have a joke for you ... {punchline}') # dessa forma, é filtrado apenas o 'value' da API e importa para o código, não senod necessário construir do zero
