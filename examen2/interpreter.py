# class Interpreter:
#     def __init__(self, tokens):
#         self.tokens = tokens
#         self.current_token_index = 0
#         self.current_token = tokens[0]
#         self.symbol_table = {}

#     def advance(self):
#         self.current_token_index += 1
#         if self.current_token_index < len(self.tokens):
#             self.current_token = self.tokens[self.current_token_index]
#         else:
#             self.current_token = None

#     def interpret(self):
#         self.program()

#     def program(self):
#         self.match('INICIO')
#         self.declarations()
#         self.match('PROCESO')
#         self.statements()
#         self.match('FIN')

#     def declarations(self):
#         while self.current_token.token_type == 'CADENA':
#             self.declaration()

#     def declaration(self):
#         self.match('CADENA')
#         identifier = self.current_token.value
#         self.match('IDENTIFIER')
#         self.match('EQUAL')
#         integer_value = self.current_token.value
#         self.match('INTEGER')
#         self.match('SEMICOLON')
#         self.match('UNDERSCORE')
#         string_value = self.current_token.value
#         self.match('STRING')
#         self.symbol_table[identifier] = string_value.strip('"')

#     def statements(self):
#         while self.current_token and self.current_token.token_type in ['SI', 'VER']:
#             self.statement()

#     def statement(self):
#         if self.current_token.token_type == 'SI':
#             self.if_statement()
#         elif self.current_token.token_type == 'VER':
#             self.print_statement()

#     def if_statement(self):
#         self.match('SI')
#         self.match('LPAREN')
#         condition = self.expression()
#         self.match('RPAREN')
#         self.match('LBRACE')
#         if condition:
#             self.statements()
#         else:
#             # Skip the block
#             while self.current_token.token_type != 'RBRACE':
#                 self.advance()
#         self.match('RBRACE')

#     def print_statement(self):
#         self.match('VER')
#         string_value = self.current_token.value
#         self.match('STRING')
#         self.match('SEMICOLON')
#         print(string_value.strip('"'))

#     def expression(self):
#         left = self.current_token.value
#         self.match('IDENTIFIER')
#         self.match('EQUALITY')
#         right = self.current_token.value
#         self.match('STRING')
#         return self.symbol_table.get(left) == right.strip('"')

#     def match(self, token_type):
#         if self.current_token.token_type == token_type:
#             self.advance()
#         else:
#             raise SyntaxError(f'Expected {token_type}, got {self.current_token.token_type}')
