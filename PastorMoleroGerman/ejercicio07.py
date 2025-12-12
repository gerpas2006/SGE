# 7. Implementa una función modo_avion(texto, activar=True) que reciba una cadena y un booleano. - Si activar es
# True, devuelve la cadena "[MODO AVIÓN] " seguida del texto. - Si activar es False, devuelve solo el texto original. 

def modo_avion(texto,activado):
    if activado:
        print(f"[MODO AVIÓN], {texto}")
    else:
        print(f"{texto}")

texto = "El modo avión esta desactivado"
activado = False

modo_avion(texto,activado)