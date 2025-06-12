# look more at the req and res objects 
# manipulating headers ~

import requests 

url = 'https://github.com/'

h = {
    'User-agent' : 'Mozilla/5.0' # serve para "mascarar" quem está solicitando a informação, somos python, mas a url acha que somos MFirefox
}

response = requests.get(url)

code = response.status_code
print(response.headers)


# specific exceptions
# using authentication
# ignore SSL warnings
# using sessions
