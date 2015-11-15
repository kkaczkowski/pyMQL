#!/usr/bin/python3

import argparse
from lang.translator import MQLToPython


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='MQL Language parameters:')
    parser.add_argument('--translate', type=str, nargs='?', help='Translate MQL to Python 3.x')
    parser.add_argument('--lex', type=str, nargs='?', help='Lexer MQL')
    args = parser.parse_args()
    if args.translate != None:
        filename = args.translate
        translator = MQLToPython()
        translator.translate(filename)
    elif args.lex != None:
        import lang.mqllex as lex
        data = open(args.lex, 'r').read()
        lex.test_lex(data)
    else:
        import lang.mqlcmd as cmd
        cmd.runcmd()

