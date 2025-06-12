# look more at the req and res objects 

import requests 

url = 'https://github.com/izaandrade/AGT0001'

response = requests.get(url)
code = response.status_code

if code == 200:
    print('everything worked out, the url is good!')
elif code == 404:
    print('authentication required')

# manipulating headers
# specific exceptions
# using authentication
# ignore SSL warnings
# using sessions
