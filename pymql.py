
import lang.mqllex
import lang.mqlparse
import yacc.yacc as yacc

if __name__ == "__main__":
    while 1:
        try:
            s = input('mql > ')
        except EOFError:
            break
        if not s: continue
        result = lang.mqlparse.parse(s)
        print(result)

