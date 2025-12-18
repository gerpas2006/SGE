# 6. Escribe una función filtrar_calorias (lista_comidas, max_calorias) que reciba una lista de tuplas
# (nombre_comida, calorías) y devuelva una nueva lista solo con las comidas cuya cantidad de calorías
# sea menor o igual que max_calorias. Si la lista está vacía, devuelve una lista vacía.

def filtarCalorias(lista_comidas,max_calorias):
    listaNueva = []
    if not lista_comidas:
        return []      
    for i in lista_comidas:
        if i[1] <= max_calorias:
                listaNueva.append(i)
    return listaNueva




lista_comidas = [
        ('Arroz', 130),
        ('Puchero', 450),
        ('Sushi', 200),
        ('Ensalada', 50)
]

print(filtarCalorias(lista_comidas,150))