#!/usr/bin/python3

import argparse
import lang.preprocesor as preprocesor
from lang.translator import MQLToPython


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='MQL Language parameters:')
    parser.add_argument('--translate', type=str, nargs='?', help='Translate MQL to Python 3.x')
    parser.add_argument('--lex', type=str, nargs='?', help='Lexer MQL')
    parser.add_argument('--preprocesor', type=str, nargs='?', help='Preprocesor MQL')
    args = parser.parse_args()
    if args.translate != None:
        filename = args.translate
        fileout = filename + 'p'
        with open(fileout, 'w') as pmql:
            preprocesor.start(filename, pmql)
        translator = MQLToPython()
        translator.translate(fileout)
    elif args.lex != None:
        import lang.mqllex as lex
        data = open(args.lex, 'r').read()
        lex.test_lex(data)
    elif args.preprocesor != None:
        with open(args.preprocesor + 'p', 'w') as pmql:
            preprocesor.start(args.preprocesor, pmql)
    else:
        import lang.mqlcmd as cmd
        cmd.runcmd()

