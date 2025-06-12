# look more at the req and res objects 

import requests 

url = 'https://github.com/'

c = {
    'test_cookie' : 'say something random'
}

h = {
    'User-agent' : 'Mozilla'
}

response = requests.get(
    url, 
    cookies=c, 
    headers=h   
    )

code = response.status_code
print(code)

# manipulating headers
# specific exceptions
# using authentication
# ignore SSL warnings
# using sessions
