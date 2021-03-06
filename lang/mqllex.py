# -*- coding: utf-8 -*-

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
            'connect',
            'import',
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
   'LQPAREN',
   'RQPAREN',
   'COLON',
   'EQUALS',
   'LT',
   'LE',
   'GT',
   'GE',
   'NE',
   'IN',
   'RE',
   'COMMA',
   'ID',
   'DBID',
   'STRING',
   'SELECT',
   'INSERT',
   'UPDATE'
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
t_LQPAREN    = r'\['
t_RQPAREN    = r'\]'
t_COLON      = r'\:'
t_LT         = r'<'
t_LE         = r'<='
t_GT         = r'>'
t_GE         = r'>='
t_NE         = r'<>'
t_IN         = r'==>'
t_RE         = r'~='
t_COMMA      = r'\,'
t_SELECT     = r'SELECT .*?(.|\n)*?;'
t_INSERT     = r'INSERT .*?(.|\n)*?;'
t_UPDATE     = r'UPDATE .*?(.|\n)*?;'
t_STRING     = r'\".*?\"'


def t_error(t):
    print("Illegal character %s" % t.value[0])
    t.lexer.skip(1)


def t_DBID(t):
    r"""[aA-zZ]*@[aA-zZ_0-9]*"""
    if t.value in keywords:
        t.type = t.value
    return t


def t_ID(t):
    r"""[a-z][\w]*"""
    if t.value in keywords:
        t.type = t.value
    return t


def t_FLOAT(t):
    r"""(\d*\.\d+)"""
    t.value = float(t.value)
    return t


def t_INTEGER(t):
    r"""(\d+)"""
    t.value = int(t.value)
    return t


def t_COMMENT(t):
    r"""\#.*"""
    pass


def t_NEWLINE(t):
    r"""\n+"""
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
    
