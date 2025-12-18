# 9. Define una función mas_procrastina(diccionario_horas) que reciba un diccionario con pares {nombre: horas_procrastinando} y devuelva el 
# nombre de la persona que más horas ha procrastinado. 
# Si el diccionario está vacío, devuelve None. 

def mas_procrastina(diccionario_horas):
    for i in diccionario_horas.values():
        if i> 0:
            mayor =i
    return mayor


diccionario_horas ={"pedro":12,
                    "Alejandro":14}

print(mas_procrastina(diccionario_horas))