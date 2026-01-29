import math
def calculadora_cientifica_trigonometrica():
    print("Seleccione la función a aplicar:")
    print("1. Seno")
    print("2. Coseno")
    print("3. Tangente")
    print("4. Exponencial")
    print("5. Logaritmo neperiano")
    
    opcion = int(input("Ingrese el número de la función (1-5): "))
    valor = int(input("Ingrese un valor entero positivo: "))
    
    print(f"\nTabla de resultados para la función seleccionada hasta {valor}:\n")
    print(f"{'Número'}\t\t{'Resultado'}")
    
    for i in range(1, valor + 1):
        if opcion == 1:
            resultado = math.sin(i)
        elif opcion == 2:
            resultado = math.cos(i)
        elif opcion == 3:
            resultado = math.tan(i)
        elif opcion == 4:
            resultado = math.exp(i)
        elif opcion == 5:
            resultado = math.log(i)
        else:
            print("Opción no válida.")
            return
        
        print(f"{i}\t\t{resultado}")
calculadora_cientifica_trigonometrica()

