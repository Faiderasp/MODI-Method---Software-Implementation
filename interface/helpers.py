import logging

from pprint import pprint as pp
logging.basicConfig(
    level=logging.INFO,
    format='[%(levelname)s] %(message)s'
)

def h_alert(data: str):
    logging.critical(data)

def h_info(data: str):
    logging.info(data)

def h_error(data: str):
    logging.error(data)

def h_warning(data: str):
    logging.warning(data)

def printer(data):
    pp(data)
