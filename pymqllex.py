
import ply.lex as lex


keywords = ('print', 'as', 'in', 'search', 'each', 'end', 'return', 'continue', 'if', 'then', 'def', 'include', 'outcsv', 'count', 'of', 'let')


tokens = keywords + (
   'FLOAT',
   'INTEGER',
   'PLUS',
   'MINUS',
   'MULTIPLY',
   'DIVIDE',
   'POWER',
   'LPAREN',
   'RPAREN',
   'EQUALS',
   'LT',
   'LE',
   'GT',
   'GE',
   'NE',
   'COMMA',
   'ID',
   'DBID',
   'STRING',
   'SELECT',
   'INSERT',
   'UPDATE'
)

t_ignore = ' \t'

t_EQUALS     = r'='
t_PLUS       = r'\+'
t_MINUS      = r'-'
t_MULTIPLY   = r'\*'
t_DIVIDE     = r'/'
t_POWER      = r'\^'
t_LPAREN     = r'\('
t_RPAREN     = r'\)' 
t_LT         = r'<'
t_LE         = r'<='
t_GT         = r'>'
t_GE         = r'>='
t_NE         = r'<>'
t_COMMA      = r'\,'
t_SELECT     = r'SELECT .*?;'
t_INSERT     = r'INSERT .*?;'
t_UPDATE     = r'UPDATE .*?;'
t_STRING     = r'\".*?\"'
t_FLOAT      = r'((\d*\.\d+)(E[\+-]?\d+)?|([1-9]\d*E[\+-]?\d+))'




def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character %s" % t.value[0])
    t.lexer.skip(1)
    
def t_DBID(t):
    r'[a-z]*@[a-z]*'
    if t.value in keywords:
        t.type = t.value
    return t
    
def t_ID(t):
    r'[a-z][a-z0-9_]*'
    if t.value in keywords:
        t.type = t.value
    return t
    
def t_INTEGER(t):
    r'\d+'
    t.value = float(t.value)    
    return t
    
def t_COMMENT(t):
    r'\#.*'
    pass

lex.lex(debug=0)
lexer = lex.lex()


if __name__ == '__main__':
	data = '''
	#Test wyrazenia
	print 2+3*3+address@street
	'''
	
	lexer.input(data)
	
	# Tokenize
	while True:
	    tok = lexer.token()
	    if not tok: 
	        break      # No more input
	    print(tok)
	
