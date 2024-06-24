# import re
# from django.shortcuts import render
# import ply.yacc as yacc
# from .forms import CodeForm

# # Lista de tokens
# tokens = (
#     'PR_PACKAGE',
#     'PR_IMPORT',
#     'PR_FUNC',
#     'ID',
#     'STRING',
#     'LEFT_PAREN',
#     'RIGHT_PAREN',
#     'LEFT_BRACE',
#     'RIGHT_BRACE',
#     'DOT',
# )

# # Palabras reservadas y librerías predefinidas
# PALABRAS_RESERVADAS = {'package', 'import', 'func'}
# LIBRERIAS_PREDEFINIDAS = {'fmt'}

# # Reglas de gramática
# def p_program(p):
#     '''program : PR_PACKAGE ID
#                | PR_IMPORT STRING
#                | PR_FUNC ID LEFT_PAREN RIGHT_PAREN LEFT_BRACE statement RIGHT_BRACE'''

# def p_statement(p):
#     '''statement : ID DOT ID LEFT_PAREN STRING RIGHT_PAREN'''

# def p_error(p):
#     print("Error de sintaxis en la entrada!")

# # Parser
# parser = yacc.yacc()

# def validar_sintaxis(codigo):
#     # Verificar la coincidencia de llaves, corchetes y paréntesis
#     stack = []
#     for char in codigo:
#         if char in ('{', '[', '('):
#             stack.append(char)
#         elif char in ('}', ']', ')'):
#             if not stack:
#                 return False
#             opening = stack.pop()
#             if (char == '}' and opening != '{') or \
#                (char == ']' and opening != '[') or \
#                (char == ')' and opening != '('):
#                 return False
#     return not stack  # La pila debe estar vacía al final

# def validar_semantica(codigo):
#     # Verificar si el código contiene la función main
#     return "func main()" in codigo

# def validar_palabras_reservadas(codigo):
#     # Verificar si se utilizan palabras reservadas
#     palabras_usadas = re.findall(r'\b(PR_[A-Z]+|ID)\b', codigo)
#     for palabra in palabras_usadas:
#         if palabra.lower() in PALABRAS_RESERVADAS:
#             return False
#     return True

# def validar_librerias_importadas(codigo):
#     # Verificar si se importan librerías predefinidas
#     librerias_importadas = re.findall(r'PR_IMPORT\s+STRING\s+(\w+)', codigo)
#     for libreria in librerias_importadas:
#         if libreria not in LIBRERIAS_PREDEFINIDAS:
#             return False
#     return True

# def analyze_code(request):
#     tokens = None
#     errors = None
#     is_valid = None

#     if request.method == 'POST':
#         form = CodeForm(request.POST)
#         if form.is_valid():
#             code = form.cleaned_data['code']

#             # Realiza el análisis léxico y sintáctico
#             try:
#                 parser.parse(code)
#             except Exception as e:
#                 errors = [str(e)]

#             # Validar sintaxis
#             is_valid_sintaxis = validar_sintaxis(code)

#             # Validar palabras reservadas
#             is_valid_palabras_reservadas = validar_palabras_reservadas(code)

#             # Validar librerías importadas
#             is_valid_librerias_importadas = validar_librerias_importadas(code)

#             # Validar semántica
#             is_valid_semantica = validar_semantica(code)

#             # Verificar si el código es válido
#             is_valid = is_valid_sintaxis and is_valid_palabras_reservadas and is_valid_librerias_importadas and is_valid_semantica

#             # Prepara los datos para pasar al template
#             context = {
#                 'code': code,
#                 'tokens': tokens,
#                 'errors': errors,
#                 'is_valid': is_valid,
#             }
#             return render(request, 'static/go.html', context)
#     else:
#         form = CodeForm()

#     return render(request, 'static/go.html', {'form': form})








import re
from django.shortcuts import render
import ply.yacc as yacc
from .forms import CodeForm

# Lista de tokens
tokens = (
    'PR_PACKAGE',
    'PR_IMPORT',
    'PR_FUNC',
    'ID',
    'STRING',
    'LEFT_PAREN',
    'RIGHT_PAREN',
    'LEFT_BRACE',
    'RIGHT_BRACE',
    'DOT',
)

# Palabras reservadas y librerías predefinidas
PALABRAS_RESERVADAS = {'package', 'import', 'func','main', 'Println', 'fmt'}
LIBRERIAS_PREDEFINIDAS = {'fmt'}
USOS_FMT = {'Println'}

# Reglas de gramática
def p_program(p):
    '''program : PR_PACKAGE ID
               | PR_IMPORT STRING
               | PR_FUNC ID LEFT_PAREN RIGHT_PAREN LEFT_BRACE statement RIGHT_BRACE'''

def p_statement(p):
    '''statement : ID DOT ID LEFT_PAREN STRING RIGHT_PAREN'''

def p_error(p):
    print("Error de sintaxis en la entrada!")

# Parser
parser = yacc.yacc()

def validar_sintaxis(codigo):
    # Verificar la coincidencia de llaves, corchetes y paréntesis
    stack = []
    for char in codigo:
        if char in ('{', '[', '('):
            stack.append(char)
        elif char in ('}', ']', ')'):
            if not stack:
                return False
            opening = stack.pop()
            if (char == '}' and opening != '{') or \
               (char == ']' and opening != '[') or \
               (char == ')' and opening != '('):
                return False
    return not stack  # La pila debe estar vacía al final

def validar_semantica(codigo):
    # Verificar si el código contiene la función main
    return "func main()" in codigo

def validar_palabras_reservadas(codigo):
    # Verificar si las palabras reservadas están correctamente escritas
    for palabra in PALABRAS_RESERVADAS:
        if palabra not in codigo:
            return False
    return True

# def validar_librerias_importadas(codigo):
#     # Verificar si se importan librerías predefinidas
#     librerias_importadas = re.findall(r'import\s+"(\w+)"', codigo)
#     for libreria in librerias_importadas:
#         if libreria not in LIBRERIAS_PREDEFINIDAS:
#             return False
#     return True

def verificar_importaciones_no_utilizadas(codigo):
    librerias_importadas = re.findall(r'import\s+"(\w+)"', codigo)
    for libreria in librerias_importadas:
        if libreria not in LIBRERIAS_PREDEFINIDAS:
            print(f"Advertencia: La librería '{libreria}' está importada pero no utilizada.")

def validar_uso_printf_en_lugar_de_println(codigo):
    # Verificar el uso de fmt.Printf en lugar de fmt.Println
    if "fmt.Printf" in codigo:
        print("Error: Usa fmt.Println en lugar de fmt.Printf para imprimir cadenas sin formato explícito")
        return False
    return True

def validar_librerias_importadas(codigo):
    # Verificar si se importan librerías predefinidas
    librerias_importadas = re.findall(r'import\s+"(\w+)"', codigo)
    for libreria in librerias_importadas:
        if libreria not in LIBRERIAS_PREDEFINIDAS:
            return False
    return True

def validar_uso_librerias(codigo):
    # Verificar si las librerías predefinidas importadas se utilizan correctamente
    librerias_importadas = re.findall(r'import\s+"(\w+)"', codigo)
    usos_fmt = re.findall(r'fmt\.(\w+)', codigo)
    for uso in usos_fmt:
        if uso not in USOS_FMT:
            return False
    if 'fmt' not in librerias_importadas and usos_fmt:
        return False
    return True

def analyze_code(request):
    tokens = None
    errors = []
    is_valid = None

    if request.method == 'POST':
        form = CodeForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']

            # Realiza el análisis léxico y sintáctico
            try:
                tokens = parser.parse(code)
            except Exception as e:
                errors.append(str(e))

            # Validar sintaxis
            is_valid_sintaxis = validar_sintaxis(code)
            if not is_valid_sintaxis:
                errors.append("Error de sintaxis: Paréntesis, corchetes o llaves no coinciden.")

            # Validar palabras reservadas
            is_valid_palabras_reservadas = validar_palabras_reservadas(code)
            if not is_valid_palabras_reservadas:
                errors.append("Error de sintaxis: Palabra reservada mal escrita.")

            # Validar librerías importadas
            is_valid_librerias_importadas = validar_librerias_importadas(code)
            if not is_valid_librerias_importadas:
                errors.append("Error de sintaxis: Librería no importada o usada.")

            # Validar uso de librerías importadas
            is_valid_uso_librerias = validar_uso_librerias(code)
            if not is_valid_uso_librerias:
                errors.append("Error de sintaxis: Uso incorrecto de librería.")

            # Validar semántica
            is_valid_semantica = validar_semantica(code)
            if not is_valid_semantica:
                errors.append("Error semántico: Falta la función main.")

            # Verificar si el código es válido
            is_valid = is_valid_sintaxis and is_valid_palabras_reservadas and is_valid_librerias_importadas and is_valid_uso_librerias and is_valid_semantica

            # Prepara los datos para pasar al template
            context = {
                'code': code,
                'tokens': tokens,
                'errors': errors,
                'is_valid': is_valid,
            }
            return render(request, 'static/go.html', context)
    else:
        form = CodeForm()

    return render(request, 'static/go.html', {'form': form})