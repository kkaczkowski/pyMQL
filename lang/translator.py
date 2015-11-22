import lang.mqllex
import lang.mqlparse
import yacc.yacc as yacc
from pprint import pprint

class MQLToPython:
    
    INDENT_PLUS  =  ('if', 'else', 'foreach', 'def')
    INDENT_MINUS =  ('end', 'else')
    
    def __init__(self):
        self.indent = 0
    
        
    def translate(self, input_mql, output_code):
        mql_source = open(input_mql, 'r').read()
        AST = lang.mqlparse.parse(mql_source, debug=False, tracking=False)
        with open(output_code, 'a') as self.code:
            for node in AST:
                token = node[0]
                translator = getattr(self, 'token_%s' %token.lower())
                translator(self, node[1])


    def token_def(self, code, node):
        '''def %{name}s(%{params}s):'''
        print(self. token_def.__doc__)
        
        
    def token_print(self, code, node):
        '''print (%{params}s)'''
        print(self. token_def.__doc__)
        
        
    def token_return(self, code, node):
        '''return %{value}s'''
        print(self. token_def.__doc__)


    def token_end(self, code, node):
        print(self. token_def.__doc__)



