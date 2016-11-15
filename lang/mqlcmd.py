# -*- coding: utf-8 -*-

import lang.mqllex
import lang.mqlparse
import yacc.yacc as yacc
from pprint import pprint
from lang.translator import MQLToPython


def runcmd():
    while 1:
        try:
            s = input('mql > ')
        except EOFError:
            break
        if not s:
            continue
        translator = MQLToPython()
        pprint(translator.translate_string(s))
