import lang.mqllex
import lang.mqlparse
import yacc.yacc as yacc
from pprint import pprint

class MQLToPython:
        
    def translate(self, input_mql, output_code):
        mql_source = open(input_mql, 'r').read()
        result = lang.mqlparse.parse(mql_source, debug=False, tracking=False)
        print()
        pprint(result)
        
        
    def get_runtime():
        pass
        
