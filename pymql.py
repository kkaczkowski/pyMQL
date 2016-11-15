#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse
import os
import lang.preprocessor as preprocessor
from config.config import PYTHON_PATH
from lang.translator import MQLToPython

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='MQL Language parameters:')
    parser.add_argument('--run', type=str, nargs='?', help='Run MQL')
    parser.add_argument('--translate', type=str, nargs='?', help='Translate MQL to Python 3.x')
    parser.add_argument('--lex', type=str, nargs='?', help='Lexer MQL')
    parser.add_argument('--preprocessor', type=str, nargs='?', help='Preprocessor MQL')
    args = parser.parse_args()
    if args.translate is not None or args.run is not None:
        filename = args.translate
        if args.run is not None:
            filename = args.run

        preprocessor_out = filename + 'p'
        py_program = filename.replace('mql', 'py')

        with open(preprocessor_out, 'w') as pmql:
            preprocessor.start(filename, pmql)
            preprocessor.prepare_runtime(py_program)
        translator = MQLToPython()
        translator.translate(preprocessor_out, py_program)
        if args.run is not None:
            print("\n\nStart MQL Program (%s)..." % py_program)
            os.system('%s "%s" %s' % (PYTHON_PATH, py_program, args.run))
    elif args.lex is not None:
        import lang.mqllex as lex

        data = open(args.lex, 'r').read()
        lex.test_lex(data)
    elif args.preprocessor is not None:
        with open(args.preprocessor + 'p', 'w') as pmql:
            preprocessor.start(args.preprocessor, pmql)
    else:
        import lang.mqlcmd as cmd

        cmd.runcmd()
