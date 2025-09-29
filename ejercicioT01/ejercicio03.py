iva = 21
precio = float(input("Diga el precio inicial "))
cant = int(input("¿Cuantos productos se va a llevar? "))
resultado = (precio + ((precio*iva)/100))*cant
print(f"El precio final es {resultado}")
print(f"Cant\tPrecio\tResultado\n{cant}\t{precio}\t{resultado}")
if cant > 3:
        print("Se va a llevar muchos produvtos")
else:
        print("Llevese más productos")