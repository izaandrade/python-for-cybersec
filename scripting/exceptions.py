# look more at the req and res objects 
# manipulating headers
# specific exceptions ~

import requests 
from request.exceptions import ConnectionError, HTTPError, Timeout, TooManyRedirects # type: ignore


url = 'https://github.com/'

try:
    response = requests.get(url)
except ConnectionError:
    print('DNS, refused connection - not due to network issue')
except HTTPError:
    print('this is due to a response code being 4xx or 5xx')
except Timeout:
    print('the conection timed out, slow server or slow connection')
except TooManyRedirects:
    print('there were more redirects than what you allowed')

# using authentication
# ignore SSL warnings
# using sessions