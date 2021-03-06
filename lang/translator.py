# -*- coding: utf-8 -*-

import lang.mqllex
import lang.mqlparse
import yacc.yacc as yacc
import lang.runtime
from pprint import pprint


class MQLToPython:
    def __init__(self):
        self.indent = 0
        self.setindent = 0
        self.builtin = dir(__builtins__)

    def translate_file(self, input_file_mql: str, output_file_py: str):
        mql_source = open(input_file_mql, 'r').read()
        AST = lang.mqlparse.parse(mql_source, debug=False, tracking=False)

        if AST is None:
            print('\n')
            return

        pprint(AST)

        print('\n\nStart translate AST:')
        with open(output_file_py, 'a') as code:
            for node in AST:
                print('[T] %s' % str(node))
                scode = self.token(node)
                if scode is not None:
                    if not isinstance(scode, tuple):
                        scode = (scode,)
                    for line in scode:
                        print('    %s' % line)
                        code.write(' ' * self.indent)
                        code.write(line)
                        code.write('\n')
                self.indent += self.setindent
                self.setindent = 0


    def translate_string(self, input_mql: str):
        result = ""
        AST = lang.mqlparse.parse(input_mql, debug=False, tracking=False)

        if AST is None:
            print('\n')
            return

        for node in AST:
            print('[T] %s' % str(node))
            scode = self.token(node)
            if scode is not None:
                if not isinstance(scode, tuple):
                    scode = (scode,)
                for line in scode:
                    print('    %s' % line)
                    result += ' ' * self.indent
                    result += line
                    result +='\n'
            self.indent += self.setindent
            self.setindent = 0
        return result


    def token(self, node):
        token = node[0]
        translator = getattr(self, 'token_%s' % str(token), None)
        scode = None
        if translator is not None:
            scode = translator(node)
        else:
            print('-- E R R O R --')
            print('Unknown token: %s' % str(token))
            scode = self.token_fun(node)
        return scode

    def token_binop(self, node):
        etype = node[0]
        if etype in ['float', 'int']:
            return str(node[1])
        elif etype == 'group':
            return "(%s)" % self.token_binop(node[1])
        elif etype == 'unary':
            if node[1] == '-': return "-" + str(node[2])
        elif etype == 'binop':
            return '%s %s %s' % (self.token_binop(node[2]), node[1], self.token_binop(node[3]))
        elif etype == 'var':
            return self.token_var(node)
        elif etype == 'dbvar':
            return self.token_dbvar(node)
        elif etype == 'str':
            return self.token_str(node)
        elif etype == 'fun':
            return self.token_fun(node)
        elif etype == 'slice':
            return self.token_slice(node)

    def token_relop(self, node):
        if node[1] == '==>':
            return '%s in %s' % (self.token_binop(node[2]), self.token_binop(node[3]))
        elif node[1] == '~=':
            return 're.findall(%s, %s)' % (self.token(node[2]), self.token(node[3]))
        else:
            return '%s %s %s' % (self.token_binop(node[2]), node[1], self.token_binop(node[3]))

    def token_fun(self, node):
        args = node[1][1]
        values = []
        if node[0] == 'fun':
            for param in args:
                values.append(str(self.token(param)))
            return '%s(%s)' % (node[1][0], ','.join(values))
        return '%s(%s)' % (node[1][0], self.token(args[0]))

    def token_def(self, node):
        self.setindent += 3
        values = []
        print(node)
        for param in node[2]:
            values.append(param[1][0])
        return 'def %s(%s):' % (node[1], ','.join(values))

    def token_return(self, node):
        return 'return %s' % self.token(node[1])

    def token_end(self, node):
        self.setindent -= 3
        return 'pass\n'

    def token_int(self, node):
        return node[1]

    def token_float(self, node):
        return node[1]

    def token_var(self, node):
        return node[1][0]

    def token_dbvar(node):
        return '%s["%s"]' % tuple(node[1][0].split('@'))

    def token_str(self, node):
        return node[1]

    def token_if(self, node):
        self.setindent += 3
        return 'if %s:' % self.token(node[1])

    def token_else(self, node):
        self.indent -= 3
        self.setindent += 3
        return 'else:'

    def token_let(self, node):
        return '%s=%s' % (node[1], self.token(node[2]))

    def token_foreach(self, node):
        self.setindent += 3
        return 'for %s in %s:' % (node[1], node[2])

    def token_foreach2(self, node):
        self.setindent += 3
        return 'for %s, %s in enumerate(%s):' % (node[1], node[2], node[3])

    def token_list(self, node):
        values = []
        print(node)
        for param in node[2]:
            values.append(str(self.token(param)))
        return '%s = [%s]' % (node[1], ','.join(values))

    def token_slice(self, node):
        args = node[1]

        if len(args) == 2:
            return '%s[%s]' % (args[0], self.token(args[1]))
        elif len(args) == 3:
            if args[1] == ":":
                return '%s[:%s]' % (args[0], self.token(args[2]))
            else:
                return '%s[%s:]' % (args[0], self.token(args[1]))
        elif len(args) == 4:
            return '%s[%s:%s]' % (args[0], self.token(args[1]), self.token(args[3]))

    def token_connect(self, node):
        return '%s = %s' % (node[1], self.token(node[2]))

    def token_search(self, node):
        dataset = ('%s = DataSet()' % node[1],
                   '%s.connection = %s' % (node[1], node[2]),
                   '%s.query = """%s"""' % (node[1], node[3]),
                   '\n')
        return dataset

    def token_save(self, node):
        return '%s.save(%s)' % (node[2], node[1])

    def token_outcsv(self, node):
        return '%s = OutCSV(%s)' % (node[1], node[2])
