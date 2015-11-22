
import yacc.lex as lex


keywords = ('as', 
            'in', 
            'search', 
            'with',
            'foreach', 
            'end', 
            'return', 
            'continue', 
            'if', 
            'then',
            'else', 
            'def',  
            'outcsv', 
            'let', 
            'list',
            'import',
            'connect',
            'save')


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
   'UPDATE',
   'DBPROVIDER'
)

t_ignore = ' \t\x0c'

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
t_SELECT     = r'SELECT .*?(.|\n)*?;'
t_INSERT     = r'INSERT .*?(.|\n)*?;'
t_UPDATE     = r'UPDATE .*?(.|\n)*?;'
t_STRING     = r'\".*?\"'
t_FLOAT      = r'((\d*\.\d+)(E[\+-]?\d+)?|([1-9]\d*E[\+-]?\d+))'
t_DBPROVIDER = r'Oracle|PostgreSQL'


def t_error(t):
    print("Illegal character %s" % t.value[0])
    t.lexer.skip(1)


def t_DBID(t):
    r'[aA-zZ]*@[aA-zZ]*'
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


def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += 1


lex.lex(debug=False)
lexer = lex.lex()

	
def test_lex(data):
    lexer.input(data)
    
    # Tokenize
    while True:
        tok = lexer.token()
        if not tok: 
            break      # No more input
        print(tok)
    
