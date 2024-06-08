# from django.shortcuts import render
# from .lexer import lex
# from .parser import Parser

# def analyze_code(request):
#     context = {}
#     if request.method == 'POST':
#         code = request.POST.get('code', '')
#         try:
#             tokens = lex(code)
#             parser = Parser(tokens)
#             parser.parse()
#             context = {
#                 'tokens': tokens,
#                 'code': code,
#                 'errors': parser.errors,
#                 'is_valid': len(parser.errors) == 0  # Verifica si hay errores
#             }
#         except SyntaxError as e:
#             context = {
#                 'tokens': [],
#                 'code': code,
#                 'errors': [str(e)],
#                 'is_valid': False
#             }
#     return render(request, 'static/go.html', context)








# # views.py
# from django.shortcuts import render
# from .lexer import lexer
# from .parser import Parser

# def analyze_code(request):
#     if request.method == 'POST':
#         code = request.POST.get('code', '')

#         # Lexer para obtener tokens
#         lexer.input(code)
#         tokens = []
#         while True:
#             tok = lexer.token()
#             if not tok:
#                 break
#             tokens.append((tok.type, tok.value))

#         # Analizador para obtener errores y verificar la validez
#         parser_instance = Parser(code)
#         parser_instance.parse()
        
#         # Lógica de análisis sintáctico (asegúrate de tener la función analisis_sintactico definida)
#         syntactic_analysis = analisis_sintactico(code)

#         context = {
#             'code': code,
#             'tokens': tokens,
#             'errors': parser_instance.errors,
#             'is_valid': len(parser_instance.errors) == 0,
#             'syntactic_analysis': syntactic_analysis
#         }
#         return render(request, 'static/go.html', context)
#     return render(request, 'static/go.html')

# def analisis_sintactico(codigo):
#     resultado = []
#     palabras_clave = {'package', 'import', 'func', 'main'}  # Palabras reservadas de Go para la sintaxis
#     lineas = codigo.split('\n')
#     for numero_linea, linea in enumerate(lineas, start=1):
#         linea_sin_espacios = linea.strip()
#         tokens = linea_sin_espacios.split()
#         for token in tokens:
#             if token in palabras_clave:
#                 resultado.append((numero_linea, token.capitalize(), True))
#             elif any(palabra in token for palabra in palabras_clave):
#                 # Añade una comprobación para 'main()'
#                 if token == 'main()':
#                     resultado.append((numero_linea, token.capitalize(), True))
#                 else:
#                     resultado.append((numero_linea, token.capitalize(), False))
#                 break
#     return resultado



from django.shortcuts import render
from .lexer import lexer

from .parser import parser, get_errors

def analyze_code(request):
    if request.method == 'POST':
        code = request.POST.get('code', '')

        # Realiza el análisis sintáctico
        parser.parse(code)

        # Obtén los errores del parser
        errors = get_errors()

        context = {
            'code': code,
            'errors': errors,
            'is_valid': len(errors) == 0,
        }
        return render(request, 'static/go.html', context)
    return render(request, 'static/go.html')

