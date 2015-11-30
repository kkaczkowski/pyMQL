#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse, os
import lang.preprocesor as preprocesor
from config.config import PYTHON_PATH
from lang.translator import MQLToPython


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='MQL Language parameters:')
    parser.add_argument('--run', type=str, nargs='?', help='Run MQL')
    parser.add_argument('--translate', type=str, nargs='?', help='Translate MQL to Python 3.x')
    parser.add_argument('--lex', type=str, nargs='?', help='Lexer MQL')
    parser.add_argument('--preprocesor', type=str, nargs='?', help='Preprocesor MQL')
    args = parser.parse_args()
    if args.translate != None or args.run != None:
        filename = args.translate
        if args.run != None:
            filename = args.run
            
        preprocesorout = filename + 'p'
        pyprogram = filename.replace('mql', 'py')
        with open(preprocesorout, 'w') as pmql:
            preprocesor.start(filename, pmql)
            preprocesor.prepare_runtime(pyprogram)
        translator = MQLToPython()
        translator.translate(preprocesorout, pyprogram)
        if args.run != None:
            print("\n\nStart MQL Program (%s)..." %pyprogram)
            os.system('%s "%s"' %(PYTHON_PATH, pyprogram))
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

