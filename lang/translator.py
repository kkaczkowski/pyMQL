import lang.mqllex
import lang.mqlparse
import yacc.yacc as yacc
from pprint import pprint

class MQLToPython:
        
    def translate(self, filename):
        mql_source = open(filename, 'r').read()
        result = lang.mqlparse.parse(mql_source, debug=False, tracking=False)
        print()
        pprint(result)
        
