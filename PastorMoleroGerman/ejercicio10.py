# 10. Implementa generar_password(base="1234", repeticiones=3) que devuelva una contraseña formada por la cadena base repetida el número de 
# veces indicado y seguida de "!" al final. 
# Ejemplo: generar_password("abc", 2) → "abcabc!". 

def generar_password(base="1234", repeticiones=3):
    print(f"{base*repeticiones}!")

generar_password("1234",2)