#Pide un número al usuario y muestra su tabla de multiplicar (del 1 al 10) usando un bucle.
print("\t\t\tEJERCICIO 01")
numPedido = int(input("Dime un numero para que te haga la tabla de multiplicar "))
resultado=0
for i in range(0,11):
    resultado = numPedido*i
    print(f"{numPedido} x {i} = {resultado}")
    
#Cuenta cuántos números del 1 al 50 son múltiplos de 3 usando un bucle.
print("\t\t\tEJERCICIO 02")
contador =0
for i in range(1,50):
    if i % 3 == 0:
        contador+=1
print(f"Desde el numero 1 hasta el 50 hay {contador} numeros que son multiplos de 3")

#Pide al usuario un número y di si es positivo, negativo o cero.
print("\t\t\tEJERCICIO 03")
num = int(input("Dime un numero para saber si es positivo o negativo "))
if num < 0:
    print("El número es negativo")
elif num > 0:
    print("El número es positivo")
else:
    print("El número es el 0")

#Pide dos números al usuario y muestra cuál es mayor, menor o si son iguales.
print("\t\t\tEJERCICIO 04")
num1 = input("Dime un número")
num2 = input("Dime otro número")
if num1 > num2:
    print(f"El {num1} es mayor que el {num2}")
elif num2> num1:
    print(f"El {num2} es mayor que el {num1}")
else:
    print("Los dos número son iguales")

#Suma los números del 1 al N (N lo ingresa el usuario).
print("\t\t\tEJERCICIO 05")
n = input("Dime un número")
resultado=0 
for i in range (1,int(n)+1):
    resultado+= i
print(f"La suma desde el 1 hasta el {n} es {resultado}")

#Pide al usuario un número entero positivo N.
#Muestra por pantalla todos los números entre 1 y N que sean múltiplos de 7.
#Al final, muestra la suma de todos esos múltiplos.
print("\t\t\tEJERCICIO 06")

numeroEntero = int(input("Dame un número entero "))
suma =0
for i in range (i,numeroEntero+1):
    if i % 7 == 0:
        print(i)
        suma+= i
print(f"Esta es la suma de todos los multiplos de 7 desde el numero que me has dado {suma}")

#Imagina que quieres controlar tu ahorro semanal durante un número determinado de semanas.
#El programa debe pedir al usuario cuántas semanas quiere registrar.
#Luego, para cada semana, debe pedir cuánto dinero ahorró.
#Al final, el programa debe mostrar:

#El total ahorrado en todas las semanas.
#En cuántas semanas ahorraste más de 100 euros (o la moneda que prefieras).
#Cuál fue la semana en la que más ahorraste y cuánto fue ese ahorro.
print("\t\t\tEJERCICIO 07")
numeroDeSemanas = int(input("Dime el número de semanas que quieres calcular "))
sumaDeTodo = 0
contador = 1
for i in range(0,numeroDeSemanas):
    dineroAhorrado = int(input(f"Cuntos dinero has ahorrado la {i+1} semana "))
    sumaDeTodo+=dineroAhorrado
    if dineroAhorrado > 100:
        contador+=1
print(f"El total de todo el dinero que has ahorrado es {sumaDeTodo}")
print(f"Has ahorrado {contador} semanas mas de 100€")

#Imagina que quieres registrar tus gastos diarios. El programa debe:

#Pedir al usuario el gasto de cada día, uno por uno.
#Continuar pidiendo gastos hasta que el usuario escriba “0” (cero) para terminar.
#Al finalizar, el programa muestra:
#El gasto total.
#El número de días en que hubo gastos mayores a 50 euros.
#Cuál fue el mayor gasto registrado y en qué día ocurrió.
print("\t\t\tEJERCICIO 08")

print("Escriba 0 si quieres salir")
gastoDeDia = None
contador = 0
suma = 0
mayorRegistro = 0
while gastoDeDia !=0:
    gastoDeDia = int(input("Cuantos has gastado en el dia "))
    suma+=gastoDeDia
    if gastoDeDia > 50:
        contador+=1
    if mayorRegistro < gastoDeDia:
        mayorRegistro=gastoDeDia

print(f"En todos estos dias has gastado {suma}€")
print(f"Ha habido {contador} dias que has gastado mas de 50€")    
print(f"El dia que mas gastastes fue cuando gastastes {mayorRegistro}€")










