from django.shortcuts import render
import ply.yacc as yacc
from .forms import CodeForm
import re


# Lista de tokens
tokens = (
    'PR_INICIO',
    'PR_FIN',
    'PR_PROCESO',
    'PR_SI',
    'PR_VER',
    'PR_CADENA',
    'ID',
    'EQUALS',
    'SEMICOLON',
    'LEFT_PAREN',
    'RIGHT_PAREN',
    'LEFT_BRACE',
    'RIGHT_BRACE',
    'STRING',
    'NUMBER',
    'DOUBLE_EQUALS'
)

# Palabras reservadas
palabras_reservadas = {
    'inicio': 'PR_INICIO',
    'fin': 'PR_FIN',
    'proceso': 'PR_PROCESO',
    'si': 'PR_SI',
    'ver': 'PR_VER',
    'cadena': 'PR_CADENA'
}

# Analizador léxico
def analizar_lexico(codigo):
    tokens = []
    lineas = codigo.split('\n')
    for i, linea in enumerate(lineas, 1):
        palabras = re.findall(r'\b\w+\b|[=;(){}"]|==', linea)
        for palabra in palabras:
            if palabra in palabras_reservadas:
                tokens.append((palabras_reservadas[palabra], palabra, i))
            elif palabra.isidentifier():
                tokens.append(('ID', palabra, i))
            elif palabra.isdigit():
                tokens.append(('NUMBER', palabra, i))
            elif palabra in '=;(){}':
                tokens.append((palabra, palabra, i))
            elif palabra == '==':
                tokens.append(('DOUBLE_EQUALS', palabra, i))
            elif palabra.startswith('"') and palabra.endswith('"'):
                tokens.append(('STRING', palabra, i))
            else:
                tokens.append(('ERROR', palabra, i))
    return tokens

# Analizador sintáctico
def analizar_sintactico(tokens):
    errores = []
    estado = 'INICIO'
    pila_bloques = []
    
    for token in tokens:
        tipo, valor, linea = token
        
        if estado == 'INICIO':
            if tipo == 'PR_INICIO':
                estado = 'DECLARACIONES'
            else:
                errores.append(f"Error en línea {linea}: Se esperaba 'inicio'")
        
        elif estado == 'DECLARACIONES':
            if tipo == 'PR_PROCESO':
                estado = 'PROCESO'
            elif tipo == 'PR_CADENA':
                # Validar declaración de cadena
                if len(tokens) > tokens.index(token) + 3:
                    if tokens[tokens.index(token)+1][0] == 'ID' and \
                       tokens[tokens.index(token)+2][0] == '=' and \
                       (tokens[tokens.index(token)+3][0] in ['ID', 'NUMBER', 'STRING']):
                        pass
                    else:
                        errores.append(f"Error en línea {linea}: Declaración de cadena inválida")
                else:
                    errores.append(f"Error en línea {linea}: Declaración de cadena incompleta")
        
        elif estado == 'PROCESO':
            if tipo == 'PR_SI':
                pila_bloques.append('SI')
            elif tipo == '}':
                if pila_bloques and pila_bloques[-1] == 'SI':
                    pila_bloques.pop()
            elif tipo == 'PR_FIN':
                if not pila_bloques:
                    estado = 'FIN'
                else:
                    errores.append(f"Error en línea {linea}: Bloques no cerrados antes de 'fin'")
    
    if estado != 'FIN':
        errores.append("Error: El programa no termina con 'fin'")
    
    return len(errores) == 0, errores

# Analizador semántico
def analizar_semantico(tokens):
    errores = []
    variables = {}
    resultados = []
    
    for i, token in enumerate(tokens):
        tipo, valor, linea = token
        
        if tipo == 'PR_CADENA':
            if i+3 < len(tokens):
                var_name = tokens[i+1][1]
                var_value = tokens[i+3][1]
                variables[var_name] = var_value
        
        elif tipo == 'PR_SI':
            if i+2 < len(tokens):
                condicion = tokens[i+2][1]
                if '==' in condicion:
                    left, right = condicion.split('==')
                    left = left.strip()
                    right = right.strip()
                    if left in variables:
                        left = variables[left]
                    if right in variables:
                        right = variables[right]
                    if str(left) == str(right):
                        resultados.append(f"Condición cumplida en línea {linea}: {left} == {right}")
                elif '=' in condicion:
                    left, right = condicion.split('=')
                    left = left.strip()
                    right = right.strip()
                    if left in variables:
                        left = variables[left]
                    if right in variables:
                        right = variables[right]
                    if str(left) == str(right):
                        resultados.append(f"Condición cumplida en línea {linea}: {left} = {right}")
    
    return len(errores) == 0, errores, variables, resultados

def analizar_codigo(codigo):
    tokens = analizar_lexico(codigo)
    es_valido_sintactico, errores_sintacticos = analizar_sintactico(tokens)
    es_valido_semantico, errores_semanticos, variables, resultados = analizar_semantico(tokens)
    
    return tokens, es_valido_sintactico, errores_sintacticos, es_valido_semantico, errores_semanticos, variables, resultados

def home(request):
    tokens = None
    es_valido_sintactico = None
    errores_sintacticos = None
    es_valido_semantico = None
    errores_semanticos = None
    variables = None
    resultados = None
    
    if request.method == 'POST':
        form = CodeForm(request.POST)
        if form.is_valid():
            codigo = form.cleaned_data['code']
            tokens, es_valido_sintactico, errores_sintacticos, es_valido_semantico, errores_semanticos, variables, resultados = analizar_codigo(codigo)
    else:
        form = CodeForm()
        tokens = es_valido_sintactico = errores_sintacticos = es_valido_semantico = errores_semanticos = variables = resultados = None
    
    print("Resultados", resultados)
    
    return render(request, 'static/examen2.html', {
        'form': form,
        'tokens': tokens,
        'es_valido_sintactico': es_valido_sintactico,
        'errores_sintacticos': errores_sintacticos,
        'es_valido_semantico': es_valido_semantico,
        'errores_semanticos': errores_semanticos,
        'variables': variables,
        'resultados': resultados  # Asegúrate de incluir esto
    })