from django.shortcuts import render
import ply.lex as lex


def calcular_total(productos):
    iva = 0.16  # 16% de IVA
    resultados = []

    for nombre_producto, precio in productos:
        iva_monto = precio * iva
        total = precio + iva_monto
        resultado = {
            'nombre': nombre_producto,
            'precio': precio,
            'iva': iva_monto,
            'total': total
        }
        resultados.append(resultado)

    return resultados


def examen(request):
    resultado = []

    if request.method == 'POST':
        productos = []
        for nombre in request.POST.getlist('nombre'):
            precio_str = request.POST.get(f'precio_{len(productos)}')
            if precio_str:
                precio = float(precio_str)
                productos.append((nombre, precio))

        print("prodcutos: ", productos)
        resultado = calcular_total(productos)
        print("resultado: ", resultado)

    return render(request, 'static/examen.html', {'resultados': resultado})