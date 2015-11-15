
import ply.yacc as yacc
import pymqllex

tokens = pymqllex.tokens


precedence = (
   ('left', 'PLUS','MINUS'),
   ('left', 'MULTIPLY','DIVIDE'),
   ('left', 'POWER'),
   ('right','UMINUS')
)

    

def p_command_include(p):
	'''command : include STRING'''
	p[0] = ('include', p[2])
	
	
def p_command_outcsv(p):
	'''command : outcsv ID in STRING'''
	p[0] = ('outcsv', p[2], p[4])

	
def p_command_print_empty(p):
	'''command : print'''
	p[0] = ('print', None)

		
def p_command_print_expression(p):
	'''command : print expression'''
	p[0] = ('print', p[2])


def p_command_search(p):
	'''command : search ID as sql'''
	p[0] = ('search', p[2], p[4])


def p_sql(p):
    '''sql : SELECT 
           | INSERT
           | UPDATE'''
    if len(p)  == 2:
         p[0] = p[1]
    else:
		
         p[0] = None

def p_command_foreach(p):
	'''command : foreach ID in ID'''
	p[0] = ('foreach', p[2], p[4])
	

def p_command_end(p):
    '''command : end'''
    p[0] = ('end',)


def p_command_return(p):
    '''command : return'''
    p[0] = ('return',)
    

def p_command_continue(p):
    '''command : continue'''
    p[0] = ('continue',)


def p_command_if(p):
    '''command : if relexpression then'''
    p[0] = ('if',p[2])
    

def p_command_def_empty(p):
	'''command : def ID LPAREN RPAREN'''
	p[0] = ('DEF', p[2])

    
def p_command_def(p):
	'''command : def ID LPAREN parlist RPAREN'''
	p[0] = ('DEF', p[2], p[4])


def p_command_let(p):
	'''command : let ID EQUALS expression'''
	p[0] = ('let', p[2], p[4])
    
    
def p_command_let_command(p):
	'''command : let ID EQUALS command'''
	p[0] = ('let', p[2], p[4])
  
##########################################  
#### Arithmetic expressions
##########################################

def p_expression_variable(p):
    '''expression : variable'''
    p[0] = ('VAR',p[1])


def p_expression_number(p):
    '''expression : INTEGER
                  | FLOAT'''
    p[0] = ('NUM',p[1])


def p_expression_string(p):
	'''expression : STRING'''
	p[0] = ('STR', p[1])


def p_expression_unary(p):
    '''expression : MINUS expression %prec UMINUS'''
    p[0] = ('UNARY','-',p[2])


def p_expression_group(p):
    '''expression : LPAREN expression RPAREN'''
    p[0] = ('GROUP',p[2])


def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression MULTIPLY expression
                  | expression DIVIDE expression
                  | expression POWER expression
    '''
    p[0] = ('BINOP',p[2],p[1],p[3])



########################################## 
#### Relational expressions
########################################## 

def p_relexpression(p):
    '''relexpression : expression LT expression
                     | expression LE expression
                     | expression GT expression
                     | expression GE expression
                     | expression EQUALS expression
                     | expression NE expression
    '''
    p[0] = ('RELOP',p[2],p[1],p[3])



########################################## 
#### Variables
########################################## 

def p_variable(p):
    '''variable : ID
                | ID LPAREN expression RPAREN
                | DBID
                '''
    if len(p) == 2:
       p[0] = (p[1],None,None)
    elif len(p) == 5:
       p[0] = (p[1],p[3],None)
    else:
       p[0] = (p[1],p[3],p[5])


def p_parlist(p):
    '''parlist : parlist COMMA ID
               | ID'''
    if len(p) > 2:
       p[0] = p[1]
       p[0].append(p[3])
    else:
       p[0] = [p[1]]
       


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

while True:
   try:
       s = input('draco > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)
