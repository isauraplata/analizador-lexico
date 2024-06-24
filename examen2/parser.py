# from lexer import tokenize
# class Parser:
#     def __init__(self, tokens):
#         self.tokens = tokens
#         self.current_index = 0
#         self.current_token = tokens[0] if tokens else None

#     def parse(self):
#         try:
#             self.program()
#             print("Análisis sintáctico exitoso.")
#         except SyntaxError as e:
#             print(f'SyntaxError: {e}')

#     def program(self):
#         self.match('INICIO')
#         self.declarations()
#         self.match('PROCESO')
#         self.statements()
#         self.match('FIN')
#         self.match('SEMICOLON')

#     def declarations(self):
#         while self.current_token.token_type == 'CADENA':
#             self.declaration()

#     def declaration(self):
#         self.match('CADENA')
#         self.match('IDENTIFIER')
#         self.match('EQUAL')
#         if self.current_token.token_type == 'STRING' or self.current_token.token_type == 'INTEGER':
#             self.advance()
#         self.match('SEMICOLON')

#     def statements(self):
#         while self.current_token and self.current_token.token_type in ['SI', 'VER']:
#             if self.current_token.token_type == 'SI':
#                 self.if_statement()
#             elif self.current_token.token_type == 'VER':
#                 self.print_statement()

#     def if_statement(self):
#         self.match('SI')
#         self.match('LPAREN')
#         self.expression()
#         self.match('RPAREN')
#         self.match('LBRACE')
#         self.statements()
#         self.match('RBRACE')

#     def print_statement(self):
#         self.match('VER')
#         self.match('STRING')
#         self.match('SEMICOLON')

#     def expression(self):
#         self.match('INTEGER')
#         self.match('EQUALITY')
#         self.match('INTEGER')

#     def match(self, expected_type):
#         if self.current_token.token_type == expected_type:
#             self.advance()
#         else:
#             raise SyntaxError(f'Expected {expected_type}, got {self.current_token.token_type}')

#     def advance(self):
#         self.current_index += 1
#         if self.current_index < len(self.tokens):
#             self.current_token = self.tokens[self.current_index]
#         else:
#             self.current_token = None

# # Ejemplo de uso para verificar el análisis sintáctico
# try:
#     tokens = tokenize(code)
#     parser = Parser(tokens)
#     parser.parse()
# except SyntaxError as e:
#     print(f'SyntaxError: {e}')
