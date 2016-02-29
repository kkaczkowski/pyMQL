# -*- coding: utf-8 -*-

import lang.mqllex as mqllex
import yacc.yacc as yacc
from lang.mqllex import tokens

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE'),
    ('left', 'POWER'),
    ('right', 'UMINUS')
)


def p_program(p):
    """program : program command
               | command
    """
    if len(p) == 2:
        if not p[0]: p[0] = []
        p[0].append(p[1])
    elif len(p) == 3:
        p[0] = p[1]
        if not p[0]: p[0] = []
        if p[2]:
            p[0].append(p[2])


def p_program_function(p):
    """program : program function
               | function
    """
    if len(p) == 2 and p[1]:
        p[0] = [['fun']]
        p[0][0].append(p[1])
    elif len(p) == 3:
        p[0] = p[1]
        if not p[0]: p[0] = [['fun']]
        if p[2]:
            p[0].append(['fun', p[2]])


def p_program_error(p):
    """program : error"""
    print('Program error: %s' % p[1])
    p[0] = None
    p.parser.error = 1


def p_command_import(p):
    """command : import STRING"""
    p[0] = ('import', p[2])


def p_command_outcsv(p):
    """command : outcsv ID in STRING"""
    p[0] = ('outcsv', p[2], p[4])


def p_command_save(p):
    """command : save ID in ID"""
    p[0] = ('save', p[2], p[4])


def p_command_save_list(p):
    """command : save LPAREN parlist RPAREN in ID"""
    p[0] = ('save', p[3], p[6])


def p_command_search(p):
    """command : search ID with ID as sql"""
    p[0] = ('search', p[2], p[4], p[6])


def p_command_foreach(p):
    """command : foreach ID in ID"""
    p[0] = ('foreach', p[2], p[4])


def p_command_foreach_enum(p):
    """command : foreach ID COMMA ID in ID"""
    p[0] = ('foreach2', p[2], p[4], p[6])


def p_command_end(p):
    """command : end"""
    p[0] = ('end', None)


def p_command_return(p):
    """command : return"""
    p[0] = ('return', None)


def p_command_return_expr(p):
    """command : return expression"""
    p[0] = ('return', p[2])


def p_command_continue(p):
    """command : continue"""
    p[0] = ('continue', None)


def p_command_if(p):
    """command : if relexpression then"""
    p[0] = ('if', p[2])


def p_command_else(p):
    """command : else"""
    p[0] = ('else', None)


def p_command_def_empty(p):
    """command : def ID LPAREN RPAREN"""
    p[0] = ('def', p[2], [])


def p_command_def(p):
    """command : def ID LPAREN parlist RPAREN"""
    p[0] = ('def', p[2], p[4])


def p_command_connect(p):
    """command : connect ID EQUALS expression"""
    p[0] = ('connect', p[2], p[4])


def p_command_let(p):
    """command : let ID EQUALS expression"""
    p[0] = ('let', p[2], p[4])


def p_command_let_command_error(p):
    """command : let error"""
    p[0] = 'Invalid let command.'


def p_command_list(p):
    """command : list ID EQUALS LPAREN parlist RPAREN"""
    p[0] = ('list', p[2], p[5])


def p_sql(p):
    """sql : SELECT
           | INSERT
           | UPDATE"""
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = None


##########################################  
#### Arithmetic expressions
##########################################

def p_expression_variable(p):
    """expression : variable"""
    p[0] = ('var', p[1])


def p_expression_dbvariable(p):
    """expression : dbvariable"""
    p[0] = ('dbvar', p[1])


def p_expression_float(p):
    """expression : FLOAT"""
    p[0] = ('float', p[1])


def p_expression_integer(p):
    """expression : INTEGER"""
    p[0] = ('int', p[1])


def p_expression_string(p):
    """expression : STRING"""
    p[0] = ('str', p[1])


def p_expression_function(p):
    """expression : function"""
    p[0] = ('fun', p[1])


def p_expression_slice(p):
    """expression : slice"""
    p[0] = ('slice', p[1])


def p_expression_unary(p):
    """expression : MINUS expression %prec UMINUS"""
    p[0] = ('unary', '-', p[2])


def p_expression_group(p):
    """expression : LPAREN expression RPAREN"""
    p[0] = ('group', p[2])


def p_expression_binop(p):
    """expression : expression PLUS expression
                  | expression MINUS expression
                  | expression MULTIPLY expression
                  | expression DIVIDE expression
                  | expression POWER expression
    """
    p[0] = ('binop', p[2], p[1], p[3])


def p_relexpression(p):
    """relexpression : expression LT expression
                     | expression LE expression
                     | expression GT expression
                     | expression GE expression
                     | expression EQUALS expression
                     | expression NE expression
                     | expression IN expression
                     | expression RE expression
    """
    p[0] = ('relop', p[2], p[1], p[3])


##########################################
#### Functions
########################################## 

def p_function(p):
    """function : ID LPAREN parlist RPAREN
                | ID LPAREN RPAREN"""
    if len(p) == 4:
        p[0] = (p[1], '')
    else:
        p[0] = (p[1], p[3])


########################################## 
#### Slice
########################################## 
def p_slice(p):
    """slice : ID LQPAREN expression COLON expression RQPAREN
             | ID LQPAREN COLON expression RQPAREN
             | ID LQPAREN expression COLON RQPAREN
             | ID LQPAREN expression RQPAREN"""
    if len(p) == 5:
        p[0] = (p[1], p[3])
    elif len(p) == 6:
        p[0] = (p[1], p[3], p[4])
    elif len(p) == 7:
        p[0] = (p[1], p[3], p[4], p[5])


########################################## 
#### Variables
########################################## 


def p_variable(p):
    """variable : ID"""
    if len(p) == 2:
        p[0] = (p[1], None, None)
    elif len(p) == 5:
        p[0] = (p[1], p[3], None)
    else:
        p[0] = (p[1], p[3], p[5])


def p_dbvariable(p):
    """dbvariable : DBID"""
    if len(p) == 2:
        p[0] = (p[1], None, None)
    elif len(p) == 5:
        p[0] = (p[1], p[3], None)
    else:
        p[0] = (p[1], p[3], p[5])


def p_parlist(p):
    """parlist : parlist COMMA expression
               | expression"""
    if len(p) > 2:
        p[0] = p[1]
        p[0].append(p[3])
    else:
        p[0] = [p[1]]


# Error rule for syntax errors
def p_error(p):
    if hasattr(p, 'lexer'):
        numline = len(p.lexer.lexdata[0:p.lexer.lexpos].split('\n'))
        print('Syntax error in input! Line : %s' % numline)
        print('>>> %s' % p.lexer.lexdata.split('\n')[numline - 1])


def parse(data, debug=False, tracking=False):
    mqlparser.error = 0
    p = mqlparser.parse(data, debug=debug, tracking=tracking)
    if mqlparser.error: return None
    return p


mqlparser = yacc.yacc()
