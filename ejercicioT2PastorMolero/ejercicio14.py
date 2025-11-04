# 14. Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.

palindromo = str(input("Dime la palabra que quieres saber si es un palindromo "))

if palindromo == palindromo[::-1]:
    print("La palabra que has puesto es un palindromo")
else:
    print("La palabra que has dicho no es un palindromo")