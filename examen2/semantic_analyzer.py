# from lexer import tokenize
# class SemanticAnalyzer:
#     def __init__(self, tokens):
#         self.tokens = tokens
#         self.current_index = 0
#         self.current_token = tokens[0] if tokens else None

#     def analyze(self):
#         try:
#             self.program()
#             print("Análisis semántico exitoso.")
#         except SemanticError as e:
#             print(f'SemanticError: {e}')

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
#         left_operand = self.current_token
#         self.expression()
#         operator = self.current_token
#         self.match('EQUALITY')
#         right_operand = self.current_token
#         self.expression()
#         self.match('RPAREN')
#         self.match('LBRACE')
#         if left_operand.value == '2' and operator.value == '==' and right_operand.value == '5':
#             self.statements()
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

# # Ejemplo de uso para verificar el análisis semántico
# try:
#     tokens = tokenize(code)
#     semantic_analyzer = SemanticAnalyzer(tokens)
#     semantic_analyzer.analyze()
# except SyntaxError as e:
#     print(f'SyntaxError: {e}')
