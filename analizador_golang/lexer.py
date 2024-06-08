# import re
# #lexer.py


# TOKEN_TYPES = {
#     'KEYWORD': 'keyword',
#     'IDENTIFIER': 'identifier',
#     'SYMBOL': 'symbol',
#     'NUMBER': 'number',
#     'STRING': 'string',
#     'OPERATOR': 'operator',
# }

# KEYWORDS = {'break', 'default', 'func', 'interface', 'select', 'case', 'defer', 'go', 'map', 'struct', 'chan', 'else', 'goto', 'package', 'switch', 'const', 'fallthrough', 'if', 'range', 'type', 'continue', 'for', 'import', 'return', 'var'}

# SYMBOLS = {'{', '}', '(', ')', '[', ']', ',', ';'}

# OPERATORS = {'+', '-', '*', '/', '%', '++', '--', '==', '!=', '<', '<=', '>', '>=', '=', '&&', '||', '!', '&', '|', '^', '<<', '>>', '&^'}

# TOKEN_REGEX = [
#     # (TOKEN_TYPES['KEYWORD'], r'\b(?:' + '|'.join(KEYWORDS) + r')\b'),
#     (TOKEN_TYPES['KEYWORD'], r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'), 
#     (TOKEN_TYPES['IDENTIFIER'], r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'),
#     (TOKEN_TYPES['NUMBER'], r'\b(0[xX][0-9a-fA-F]+|(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?)\b'),
#     (TOKEN_TYPES['STRING'], r'"(?:\\.|[^"\\])*"'),
#     (TOKEN_TYPES['OPERATOR'], r'|'.join(re.escape(op) for op in OPERATORS)),
#     (TOKEN_TYPES['SYMBOL'], r'|'.join(re.escape(sym) for sym in SYMBOLS)),
#     (None, r'//.*?$|/\*(?:.|\n)*?\*/'),
# ]

# def lex(code):
#     tokens = []
#     error_token = ''
#     while code:
#         match = None
#         for token_type, regex in TOKEN_REGEX:
#             match = re.match(regex, code)
#             if match:
#                 token = match.group(0)
#                 if token_type is None:  # Saltar comentarios
#                     code = code[len(token):]
#                     break
#                 tokens.append((token_type, token))
#                 code = code[len(token):]
#                 error_token = ''  # Restablecer el token de error
#                 break
#         if not match:
#             error_token += code[0]  # Agregar el carácter no reconocido al token de error
#             code = code[1:]
#     if error_token:
#         raise SyntaxError(f'Unexpected character: {error_token}')
#     return tokens









# lexer.py

# import ply.lex as lex

# # Definición de tokens
# tokens = (
#     'KEYWORD_PACKAGE', 'KEYWORD_IMPORT', 'KEYWORD_FUNC', 'IDENTIFIER', 
#     'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'STRING', 'SEMICOLON', 'EQ',
#     'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'NUMBER'
# )

# # Reglas de los tokens
# t_KEYWORD_PACKAGE = r'package'
# t_KEYWORD_IMPORT = r'import'
# t_KEYWORD_FUNC = r'func'
# t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z_0-9]*'
# t_LPAREN = r'\('
# t_RPAREN = r'\)'
# t_LBRACE = r'\{'
# t_RBRACE = r'\}'
# t_STRING = r'\".*?\"'
# t_SEMICOLON = r';'
# t_EQ = r'='
# t_PLUS = r'\+'
# t_MINUS = r'-'
# t_TIMES = r'\*'
# t_DIVIDE = r'/'
# t_NUMBER = r'\d+'

# t_ignore = ' \t'

# def t_newline(t):
#     r'\n+'
#     t.lexer.lineno += len(t.value)

# def t_error(t):
#     print(f"Illegal character '{t.value[0]}'")
#     t.lexer.skip(1)

# lexer = lex.lex()





# import ply.lex as lex

# # Definición de tokens
# tokens = (
#     'KEYWORD_PACKAGE', 'KEYWORD_IMPORT', 'KEYWORD_FUNC', 'IDENTIFIER', 
#     'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'STRING', 'SEMICOLON', 'EQ',
#     'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'NUMBER'
# )

# # Reglas de los tokens
# t_LPAREN = r'\('
# t_RPAREN = r'\)'
# t_LBRACE = r'\{'
# t_RBRACE = r'\}'
# t_STRING = r'\".*?\"'
# t_SEMICOLON = r';'
# t_EQ = r'='
# t_PLUS = r'\+'
# t_MINUS = r'-'
# t_TIMES = r'\*'
# t_DIVIDE = r'/'
# t_NUMBER = r'\d+'

# t_ignore = ' \t'

# # Definición de palabras clave
# keywords = {
#     'package': 'KEYWORD_PACKAGE',
#     'import': 'KEYWORD_IMPORT',
#     'func': 'KEYWORD_FUNC',
# }

# def t_IDENTIFIER(t):
#     r'[a-zA-Z_][a-zA-Z_0-9]*'
#     t.type = keywords.get(t.value, 'IDENTIFIER')  # Revisa si es una palabra clave, si no, es IDENTIFIER
#     return t

# def t_newline(t):
#     r'\n+'
#     t.lexer.lineno += len(t.value)

# def t_error(t):
#     print(f"Illegal character '{t.value[0]}'")
#     t.lexer.skip(1)

# lexer = lex.lex()











# lexer.py

# lexer.py

import ply.lex as lex

# Definición de tokens como una lista
tokens = [
    'KEYWORD_PACKAGE', 'KEYWORD_IMPORT', 'KEYWORD_FUNC', 'IDENTIFIER', 
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'STRING', 'SEMICOLON', 'EQ',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'NUMBER', 'DOT', 'COMMA',  
]

# Definición de las palabras clave reservadas
reserved = {
    'package': 'KEYWORD_PACKAGE',
    'import': 'KEYWORD_IMPORT',
    'func': 'KEYWORD_FUNC',
    # Agrega otras palabras clave aquí si es necesario
}

# Extender tokens con los valores de reserved
tokens.extend(reserved.values())

# Reglas de los tokens
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_STRING = r'\".*?\"'
t_SEMICOLON = r';'
t_EQ = r'='
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_DOT = r'\.'
t_NUMBER = r'\d+'
t_COMMA = r','

# Ignorar espacios en blanco y tabulaciones
t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'IDENTIFIER') if t.value != 'import' else 'IDENTIFIER'
    return t

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()
