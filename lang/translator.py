import lang.mqllex
import lang.mqlparse
import yacc.yacc as yacc
import lang.runtime
from pprint import pprint

class MQLToPython:
    
    INDENT_PLUS  =  ('if', 'else', 'foreach', 'def')
    INDENT_MINUS =  ('end', 'else')
    
    def __init__(self):
        self.indent = 0
        self.builtin = dir (__builtins__)
    
        
    def translate(self, input_mql, output_code):
        mql_source = open(input_mql, 'r').read()
        AST = lang.mqlparse.parse(mql_source, debug=False, tracking=False)
        pprint(AST)
        print('\n\nStart translate AST:')
        with open(output_code, 'a') as code:
            for node in AST:
                print ('[T] %s' %node)
                scode = self.token(node)
                print ('    %s' %scode)
                code.write(scode)
                code.write('\n')
                
                
    def token(self, node):
        token = node[0]
        translator = getattr(self, 'token_%s' %str(token), None)
        scode = None
        if translator != None:
            scode = translator(node)
        else:
            print('Unknown token: %s' %str(token))
            scode = self.token_fun(node)
        return scode


    def token_binop(self, node):
        etype = node[0]
        if etype == 'num': return str(node[1])
        elif etype == 'group': return "(%s)" % self.token_binop(node[1])
        elif etype == 'unary':
            if node[1] == '-': return "-"+str(node[2])
        elif etype == 'binop':
            return "%s %s %s" % (self.token_binop(node[2]),node[1],self.token_binop(node[3]))
        elif etype == 'var':
            return self.var_str(node[1])
        elif etype == 'fun':
            print("--- fun ---")
            print(node)
            return self.token_fun(node)


    def token_fun(self, node):
        args = node[1][1]
        values = []
        if node[0] == 'fun':
            for param in args:
                values.append(str(self.token(param)))
            return '%s(%s)' %(node[1][0], ','.join(values))
        return '%s(%s)' %(node[1][0], self.token(args[0]))


    def token_def(self, node):
        '''def %{name}s(%{params}s):'''
        print(self. token_def.__doc__)


    def token_return(self, node):
        '''return %{value}s'''
        print(self. token_def.__doc__)


    def token_end(self, node):
        print(self. token_def.__doc__)
        
    
    def token_num(self, node):
        return node[1]


    def token_var(self, node):
        print(node)
        return node[1][0]

