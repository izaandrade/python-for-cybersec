# send an email with content from an API
# implement logging
# make sure that email credentials are NOT in the scrit - external json file
# PROPERLY handle all exceptions specifically

# logging, requests, smtplib, json
import requests
import json
import smtplib
import logging
from email.message import EmailMessage

URL = 'https://v2.jokeapi.dev/joke/Programming?blacklistFlags=nsfw,religious,political,racist,sexist,explicit'

with open('creds.json', 'r') as f:
    creds = json.load(f)
    f.close()

LOGFILE = 'email_send.log'
EMAIL = creds['email']
PASSWORD = creds['password']
RECEPIENT = creds['recepient']

logging.basicConfig(filemode='a', filename=LOGFILE, level=logging.INFO, format='%(levelname)s - %(asctime)s - %(message)s')

def send_email(joke):  
    try:
        s = smtplib.SMTP('smtp.gmail.com', 587) #SPECIFIC TO GMAIL!!! - objeto que starta o socket do email
        s.starttls() # starta a encriptação
    except smtplib.SMTPConnectError: # não foi possivem estabelecer uma conexão com o servidor do email
        logging.error('couldnt connect to the email server') # transformei de print para log
        exit()
    try:
        s.login(EMAIL, PASSWORD) # loga no email
    except smtplib.SMTPAuthenticationError: # trata erro de autenticação (senha, login)
        logging.error('auth failure')
        exit()
    try:
        msg = EmailMessage()
        msg['From'] = EMAIL
        msg['To'] = RECEPIENT
        msg['Subject'] = 'Vou te contar uma piada de programação kkkkk'
        msg.set_content(joke)
        s.send_message(msg)
    except smtplib.SMTPException:
        logging.error('unable to send email due to error')
        exit()
    s.quit()
    
def get_joke_content():
    response = requests.get(URL)
    # print(response.json()) # roda essa função para extrair as informações contidas no json da API
    result = response.json()

    if result['error']:
        logging.error('something went wrong with the request to the API')
        return None    
    if result['type'] == 'twopart':
        # extract a setup and a delivery
        setup = result['setup']
        delivery = result['delivery']
        return f'{setup}\n\n{delivery})'
    else:
        # extract a joke
        joke = result['joke']
        return f'joke: {joke}'

# start pf the actual program exe    
joke = get_joke_content()
logging.info('joke retrieved successfully')
if joke is not None:
    send_email(joke)
    logging.info('email successfully sent')
