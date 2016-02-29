import sys, logging

PYTHON_PATH = '/usr/bin/python3'
if sys.platform == 'win32':
    PYTHON_PATH = 'c:/python34/python.exe'

config = {'python': '#!%s' % PYTHON_PATH}

logging.basicConfig(handlers=[logging.FileHandler('mql.log'), logging.StreamHandler()],
                    level=logging.DEBUG)
