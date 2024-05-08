# from django.shortcuts import render
# import ply.lex as lex

# # Definición de tokens
# tokens = (
#     'FOR',
#     'IF',
#     'DO',
#     'WHILE',
#     'ELSE',
#     'LPAREN',
#     'RPAREN',
#     'COMMA',
#     'ID',  # Token para identificadores
# )

# # Expresiones regulares para tokens simples
# t_FOR = r'for'
# t_IF = r'if'
# t_DO = r'do'
# t_WHILE = r'while'
# t_ELSE = r'else'
# t_LPAREN = r'\('
# t_RPAREN = r'\)'
# t_COMMA = r','
# t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'  # Identificadores (variables)

# # Ignorar espacios y tabulaciones
# t_ignore = ' \t'

# # Función para capturar errores de token
# def t_error(t):
#     print("Carácter ilegal '%s'" % t.value[0])
#     t.lexer.skip(1)

# # Construir el lexer
# lexer = lex.lex()

# # Función para analizar el código ingresado
# def analizar_codigo(codigo):
#     lexer.input(codigo)
#     tokens = []
#     while True:
#         tok = lexer.token()
#         if not tok:
#             break
#         tokens.append(tok)
#     return tokens

# # Vista de Django
# def home(request):
#     tokens = None
    
#     if request.method == 'POST':
#         archivo = request.FILES.get('archivo')  # Obtener el archivo si se cargó uno
#         codigo = request.POST.get('codigo', '')  # Obtener el código del formulario
        
#         if archivo:  # Si se cargó un archivo, leer su contenido
#             codigo = archivo.read().decode('utf-8')
        
#         tokens = analizar_codigo(codigo)  # Analizar el código
        
#     return render(request, 'static/index.html', {'tokens': tokens})




from django.shortcuts import render
import ply.lex as lex

# Definición de tokens
tokens = (
    'FOR',
    'IF',
    'DO',
    'WHILE',
    'ELSE',
    'LPAREN',
    'RPAREN',
    'COMMA',
    'ID',  # Token para identificadores
)

# Expresiones regulares para tokens simples
t_FOR = r'for'
t_IF = r'if'
t_DO = r'do'
t_WHILE = r'while'
t_ELSE = r'else'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'  # Identificadores (variables)

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Función para capturar errores de token
def t_error(t):
    print("Carácter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()

# Función para analizar el código ingresado
# Función para analizar el código ingresado
def analizar_codigo(codigo):
    lexer.input(codigo)
    tokens = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        # Mapear el tipo de token a una descripción legible
        token_descriptions = {
            'FOR': '<Reservada For>',
            'IF': '<Reservada If>',
            'DO': '<Reservada Do>',
            'WHILE': '<Reservada While>',
            'ELSE': '<Reservada Else>',
            'LPAREN': '<Parentesis de apertura>',
            'RPAREN': '<Parentesis de cierre>',
            'COMMA': '<Coma>',
            'ID': '<Identificador>',
        }
        symbol = token_descriptions.get(tok.type, tok.type)
        # Crear la cadena de salida en el formato deseado
        token_info = f"Línea {tok.lineno}\t\tSimbolo\n{symbol}\t\t\t{tok.value}\n"
        tokens.append(token_info)
    return tokens


# Vista de Django
def home(request):
    tokens = None
    
    if request.method == 'POST':
        archivo = request.FILES.get('archivo')  # Obtener el archivo si se cargó uno
        codigo = request.POST.get('codigo', '')  # Obtener el código del formulario
        
        if archivo:  # Si se cargó un archivo, leer su contenido
            codigo = archivo.read().decode('utf-8')
        
        tokens = analizar_codigo(codigo)  # Analizar el código
        
    return render(request, 'static/index.html', {'tokens': tokens})
