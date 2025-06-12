# hiding sensitive information
import json

with open('credentials.json', 'r') as cred_file:
    data = json.load(cred_file)
    print(type(data))
    cred_file.close() 

email_credentials = data['email_credentials']
email = email_credentials['email']
password = email_credentials['password']
if data['print_settings']['everything_upper']:
    print(email.upper())
else: 
    print(email)