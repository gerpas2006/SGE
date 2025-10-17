print("Bienvenido al programa")

salir = True
sueldoFijo=float(1525.5)
precioHorasExtrasCategoria1=float(40.0)
precioHorasExtrasCategoria2=float(50.0)
precioHorasExtrasCategoria3=float(75.0)
resultado = sueldoFijo
while salir:
    print("0. Salir\n1. Calcular sueldo categoria 1\n2. Calcular sueldo categoria 2\n3. Calcular sueldo categoria 3\n4. Calcular sueldo categoria 4")
    eleccion = int(input("Elige una opcion "))
    match eleccion:
      case 0:
        print("Saliendo....")
        salir=False
      case 1:
          horasExtras= float(input("¿Cuántas horas extras has hecho?"))
          if horasExtras>=30:
             resultado = sueldoFijo+(float(30)* float(precioHorasExtrasCategoria1))
          else:
             resultado = (sueldoFijo+(float(horasExtras)* float(precioHorasExtrasCategoria1)))
          antiguedad = float(input("¿Cuántos años de antiguedad tienes?"))
          if antiguedad % 3 == 0:
            resultado +=((resultado*2)/100)
          else: 
             resultado
          anoTrabajados = int(input("¿Cuántos años tienes trabajados?"))
          if(anoTrabajados==25):
             resultado+=((resultado*4)/100)
          else:
             resultado
          print(f"El sueldo del empleado de la categoria 1 es {resultado}€")
      case 2:
          horasExtras= float(input("¿Cuántas horas extras has hecho?"))
          if horasExtras>=30:
             resultado = sueldoFijo+(float(30)* float(precioHorasExtrasCategoria2))
          else:
             resultado = (sueldoFijo+(float(horasExtras)* float(precioHorasExtrasCategoria2)))
          antiguedad = float(input("¿Cuántos años de antiguedad tienes?"))
          if antiguedad % 3 == 0:
            resultado +=((resultado*2)/100)
          else:
             resultado
          anoTrabajados = int(input("¿Cuántos años tienes trabajados?"))
          if(anoTrabajados==25):
             resultado+=((resultado*4)/100)
          else:
             resultado
          print(f"El sueldo del empleado de la categoria 1 es {resultado}€")

      case 3:
          horasExtras= float(input("¿Cuántas horas extras has hecho?"))
          if horasExtras>=30:
             resultado = sueldoFijo+(float(30)* float(precioHorasExtrasCategoria3))
          else:
             resultado = (sueldoFijo+(float(horasExtras)* float(precioHorasExtrasCategoria3)))
          antiguedad = float(input("¿Cuántos años de antiguedad tienes?"))
          if antiguedad % 3 == 0:
            resultado +=((resultado*2)/100)
          else: 
             resultado
          anoTrabajados = int(input("¿Cuántos años tienes trabajados?"))
          if(anoTrabajados==25):
             resultado+=((resultado*4)/100)
          else:
             resultado
          print(f"El sueldo del empleado de la categoria 3 es {resultado}€")
      case 4:
          antiguedad = float(input("¿Cuántos años de antiguedad tienes?"))
          if antiguedad % 3 == 0:
             resultado +=((resultado*2)/100)
          else:
             resultado
          anoTrabajados = int(input("¿Cuántos años tienes trabajados?"))
          if(anoTrabajados==25):
             resultado+=((resultado*4)/100)
          else:
             resultado
          print(f"Este es el sueldo del empleado de la categoria 4 con todos los plus {resultado}€")
      case _:
          print("Elige una opción correcta")


print("Gracias por utilizar mi programa")
          




 
    

   
    
