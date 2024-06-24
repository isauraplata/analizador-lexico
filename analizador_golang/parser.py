# Analizador sintáctico
def parser(tokens):
    index = 0
    length = len(tokens)
    errors = []

    def expect(expected_type):
        nonlocal index
        if index < length and tokens[index][0] == expected_type:
            index += 1
        else:
            if index < length:
                errors.append(f"Expected {expected_type}, but found {tokens[index][0]}")
            else:
                errors.append(f"Expected {expected_type}, but found EOF")
            # Detener el análisis en caso de error
            raise SyntaxError("Parsing stopped due to error")

    # Reglas de gramática
    def parse_program():
        parse_package()
        parse_import()
        parse_function()

    def parse_package():
        expect('KEYWORD_PACKAGE')
        expect('IDENTIFIER')
        expect('NEWLINE')

    def parse_import():
        expect('KEYWORD_IMPORT')
        expect('STRING')
        expect('NEWLINE')

    def parse_function():
        expect('KEYWORD_FUNC')
        expect('IDENTIFIER')
        expect('LPAREN')
        expect('RPAREN')
        expect('LBRACE')
        parse_statements()
        expect('RBRACE')

    def parse_statements():
        parse_statement()

    def parse_statement():
        expect('IDENTIFIER')
        expect('DOT')
        expect('IDENTIFIER')
        expect('LPAREN')
        expect('STRING')
        expect('RPAREN')
        expect('NEWLINE')

    try:
        parse_program()
    except SyntaxError:
        pass

    return errors
