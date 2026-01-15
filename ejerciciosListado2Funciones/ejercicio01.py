def descuento(descuento, precio):
    resul = (descuento*precio)/100
    return precio-resul

def IVA(precio,iva):
    resul = (precio*iva)/100
    return precio+resul

def calcularPrecioCesta(diccionarioCesta,iva_funcion,iva_porcentaje):
    total = 0
    for precio in diccionarioCesta.values():
        total += precio
    return iva_funcion(total,iva_porcentaje)


cesta = {
    "pan": 1.20,
    "leche": 0.90,
    "queso": 3.50
}

print(calcularPrecioCesta(cesta,IVA,21))