import logging

# conifigure logging
filename = 'example.log'

logging.basicConfig(filename=filename, filemode='a', level=logging.INFO, format='%(levelname)s - %(message)s - %(asctime)s')

# test
logging.info('this is an example log entry')

# debug, info, warning, error, critical

def fun():
    x = 'something'
    y = 5
    try:
        return x + y
    except: 
        logging.error('invalid number tried in fun function')
        exit()

number = fun()
logging.info('number created successfully')
