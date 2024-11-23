from logger import logging
def add(a,b):
    logging.debug('The addition opertion take place')
    return a+b


logging.debug('The addition function   call')
add(10,3)