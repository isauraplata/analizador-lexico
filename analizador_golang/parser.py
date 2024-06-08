# #parse.py

# class Parser:

#     def __init__(self, tokens):
#         self.tokens = tokens
#         self.pos = 0
#         self.errors = []  # Inicializa la lista de errores

#     def parse(self):
#         while self.pos < len(self.tokens):
#             token_type, token = self.tokens[self.pos]
#             if token_type == 'keyword':
#                 self.parse_keyword(token)
#             elif token_type == 'symbol' and token == 'import':
#                 self.parse_import()
#             else:
#                 self.pos += 1

#     def parse_import(self):
#         self.pos += 1  # Saltar la palabra 'import'
#         if self.pos < len(self.tokens) and self.tokens[self.pos][0] != 'string':
#             self.errors.append(f"Error en la importación: se esperaba una cadena de texto en la posición {self.pos}")

#     def parse_keyword(self, token):
#         if token == 'func':
#             self.parse_function()
#         else:
#             self.pos += 1
    
#     # def parse_keyword(self, token):
#     #     if token in KEYWORDS: 
#     #         return# Check if token is a valid keyword
#     #     # Handle valid keyword logic here
#     #     else:
#     #         self.errors.append(f"Unexpected keyword: {token} at position {self.pos}")
#     #         self.pos += 1  # Skip the unexpected token



#     def parse_function(self):
#         # Aquí puedes agregar la lógica para parsear una función en Go
#         self.pos += 1  # Saltar la palabra clave 'func'
#         # Ejemplo: func main() {}
#         if self.pos < len(self.tokens) and self.tokens[self.pos][0] == 'identifier':
#             self.pos += 1  # Saltar el nombre de la función
#         if self.pos < len(self.tokens) and self.tokens[self.pos][1] == '(':
#             self.pos += 1  # Saltar '('
#         if self.pos < len(self.tokens) and self.tokens[self.pos][1] == ')':
#             self.pos += 1  # Saltar ')'
#         if self.pos < len(self.tokens) and self.tokens[self.pos][1] == '{':
#             self.pos += 1  # Saltar '{'
#             while self.pos < len(self.tokens) and self.tokens[self.pos][1] != '}':
#                 self.pos += 1
#             if self.pos < len(self.tokens) and self.tokens[self.pos][1] == '}':
#                 self.pos += 1  # Saltar '}'




#parser.py
# parser.py
import ply.yacc as yacc
from .lexer import tokens  # Importación absoluta

# Precedencia de operadores, de menor a mayor
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

# Define la lista de errores
errors = []

def p_program(p):
    '''program : package_statement import_statements function_declarations'''
    p[0] = (p[1], p[2], p[3])

def p_package_statement(p):
    '''package_statement : KEYWORD_PACKAGE IDENTIFIER SEMICOLON'''
    p[0] = ('package', p[2])

def p_import_statements(p):
    '''import_statements : import_statement import_statements
                         | empty'''
    if len(p) == 3:
        p[0] = [p[1]] + p[2]
    else:
        p[0] = []

def p_import_statement(p):
    '''import_statement : KEYWORD_IMPORT STRING SEMICOLON'''
    p[0] = ('import', p[2])

def p_function_declarations(p):
    '''function_declarations : function_declaration function_declarations
                             | empty'''
    if len(p) == 3:
        p[0] = [p[1]] + p[2]
    else:
        p[0] = []

def p_function_declaration(p):
    '''function_declaration : KEYWORD_FUNC IDENTIFIER LPAREN RPAREN LBRACE statements RBRACE'''
    p[0] = ('func', p[2], p[6])

def p_statements(p):
    '''statements : statement statements
                  | empty'''
    if len(p) == 3:
        p[0] = [p[1]] + p[2]
    else:
        p[0] = []

def p_statement(p):
    '''statement : assignment_statement SEMICOLON
                 | function_call_statement SEMICOLON'''
    p[0] = p[1]

def p_assignment_statement(p):
    '''assignment_statement : IDENTIFIER EQ expression'''
    p[0] = ('assign', p[1], p[3])

def p_function_call_statement(p):
    '''function_call_statement : IDENTIFIER LPAREN expression_list RPAREN'''
    p[0] = ('call', p[1], p[3])

def p_expression_list(p):
    '''expression_list : expression
                       | expression COMMA expression_list'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_expression(p):
    '''expression : NUMBER
                  | STRING'''
    p[0] = p[1]

def p_empty(p):
    '''empty :'''
    pass

def p_error(p):
    global errors
    if p:
        errors.append(f"Syntax error at '{p.value}'")
    else:
        errors.append("Syntax error at EOF")

parser = yacc.yacc()

# Función para obtener los errores
def get_errors():
    global errors
    return errors
