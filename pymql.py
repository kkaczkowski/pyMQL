#!/usr/bin/python3

import argparse
import lang.mqllex
import lang.mqlparse
import lang.translator as translator
import yacc.yacc as yacc

def translate():
    print("Translate")

class translate:
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='MQL Language parameters:')
    parser.add_argument('--translate', action = translator.MQLToPython, type=str, nargs='+', help='Translate MQL to Python 3.x')
    args = parser.parse_args()
    """
    while 1:
        try:
            s = input('mql > ')
        except EOFError:
            break
        if not s: continue
        result = lang.mqlparse.parse(s)
        print(result)
    """
