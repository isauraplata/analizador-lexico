import ply.yacc as yacc
from .lexer import tokens

def p_expression_for(p):
    'expression : FOR LPAREN INT ID EQUALS NUMBER SEMICOLON ID LE NUMBER SEMICOLON ID PLUSPLUS RPAREN LBRACE ID EQUALS NUMBER SEMICOLON RBRACE'
    pass

def p_error(p):
    print("Syntax error in input!")

parser = yacc.yacc()
