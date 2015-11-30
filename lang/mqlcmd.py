# -*- coding: utf-8 -*-

import lang.mqllex
import lang.mqlparse
import yacc.yacc as yacc
from pprint import pprint

def runcmd():
    while 1:
        try:
            s = input('mql > ')
        except EOFError:
            break
        if not s: continue
        result = lang.mqlparse.parse(s + '\n')
        pprint(result)
