import re
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

def analizar_codigo(codigo):
    reservadas = ["programa", "int", "read", "printf", "end"]
    operadores = ["+", "-", "*", "/"]
    parentesis_abre = ["(", "{", "["]
    parentesis_cierra = [")", "}", "]"]
    punto_coma = [";"]
    coma = [","]
    errores = []
    tokens_totales = []
    lineas = codigo.split("\n")

    for i, linea in enumerate(lineas, start=1):  
        linea_tokens = []

        for token in reservadas:
            matches = re.findall(r"\b{}\b".format(token), linea)
            for match in matches:
                linea_tokens.append((i, match, "Reservada", "", ""))

        for token in operadores:
            matches = linea.count(token)
            for _ in range(matches):
                linea_tokens.append((i, token, "Operador", "", ""))

        for token in parentesis_abre:
            matches = linea.count(token)
            for _ in range(matches):
                linea_tokens.append((i, token, "Paréntesis", "", ""))

        for token in parentesis_cierra:
            matches = linea.count(token)
            for _ in range(matches):
                linea_tokens.append((i, token, "Paréntesis", "", ""))

        for token in punto_coma:
            matches = linea.count(token)
            for _ in range(matches):
                linea_tokens.append((i, token, "Punto y coma", "", ""))

        for token in coma:
            matches = linea.count(token)
            for _ in range(matches):
                linea_tokens.append((i, token, "Coma", "", ""))

        identificadores = re.findall(r"\b[a-zA-Z][a-zA-Z0-9_]*\b", linea)
        for identificador in identificadores:
            print("Identificador encontrado:", identificador.lower())
            for keyword in ["suma", "resta", "multiplicacion", "division"]:
                if keyword.startswith(identificador.lower()):
                    if identificador.lower() != keyword:
                        print("Palabra clave incompleta encontrada:", identificador.lower())
                        errores.append((i, identificador, "Error", "Palabra incorrecta", ""))
                        break
                    else:
                        print("Palabra clave encontrada:", identificador.lower())
                        linea_tokens.append((i, identificador, "Identificador", "", ""))
                        break
            else:
                linea_tokens.append((i, identificador, "Identificador", "", ""))

        tokens_totales.extend(linea_tokens)

    errores_sintacticos = analizar_sintaxis(lineas)

    return tokens_totales, errores, errores_sintacticos

def analizar_sintaxis(lineas):
    errores_sintacticos = []
    pila_llaves = []

    for i, linea in enumerate(lineas, start=1):
        if 'for' in linea:
            if not re.match(r'\s*for\s*\(.*;.*;.*\)\s*\{', linea):
                errores_sintacticos.append((i, linea, "Error Sintáctico", "Estructura de bucle for incorrecta"))

        if 'system.out.print' in linea:
            if not re.match(r'.*system\.out\.print(l?n?)\s*\(.*\)\s*;', linea):
                errores_sintacticos.append((i, linea, "Error Sintáctico", "Estructura de system.out.print incorrecta"))

        if not linea.strip().endswith(';') and not linea.strip().endswith('{') and not linea.strip().endswith('}') and 'for' not in linea:
            errores_sintacticos.append((i, linea, "Error Sintáctico", "Falta ';'"))

        for char in linea:
            if char == '{':
                pila_llaves.append('{')
            elif char == '}':
                if pila_llaves and pila_llaves[-1] == '{':
                    pila_llaves.pop()
                else:
                    errores_sintacticos.append((i, linea, "Error Sintáctico", "Llave de cierre '}' sin llave de apertura correspondiente"))

    if pila_llaves:
        for j in range(len(pila_llaves)):
            errores_sintacticos.append((i, "Llave de apertura '{' sin llave de cierre correspondiente"))

    return errores_sintacticos

@csrf_exempt
def index(request):
    codigo = ""
    if request.method == 'POST':
        codigo = request.POST.get('codigo', '')
        tokens_totales, errores, errores_sintacticos = analizar_codigo(codigo)

        if not tokens_totales:
            return render(request, 'analyzer/home.html', {'error': "No se encontraron tokens en el código", 'codigo': codigo})

        total_reservadas = sum(1 for token in tokens_totales if token[2] == "Reservada")
        total_identificadores = sum(1 for token in tokens_totales if token[2] == "Identificador")
        total_simbolos = sum(1 for token in tokens_totales if token[2] in ["Paréntesis", "Punto y coma", "Coma"])
        total_operadores = sum(1 for token in tokens_totales if token[2] == "Operador")
        total_tokens = len(tokens_totales)

        context = {
            'tokens': tokens_totales,
            'total_reservadas': total_reservadas,
            'total_identificadores': total_identificadores,
            'total_simbolos': total_simbolos,
            'total_operadores': total_operadores,
            'total_tokens': total_tokens,
            'codigo': codigo,
            'errores': errores,
            'errores_sintacticos': errores_sintacticos
        }

        return render(request, 'static/index.html', context)

    return render(request, 'static/index.html', {'codigo': codigo})
