import requests
import json # importar  json transforma a resposta de string para dictionary, o que ajuda a filtrar o que é API e o que não é

base_url = 'https://www.thecocktaildb.com/api/json/v1/1/search.php?s='
query = input('Please enter a drink to search>> ')

r = requests.get(f'{base_url}{query}')

result = r.json()['drinks']
instructions = result[0]['strInstructions']

print(f'Instructions: {instructions}') 

r.json()['drinks'][0]['strInstructions']