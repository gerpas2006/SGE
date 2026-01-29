
from datetime import datetime

def buscarInmueble(listaInmuebles, precioReferente):    
    listaBuscada = []
    año_actual = datetime.now().year
    
    for inmueble in listaInmuebles:
        antiguedad = año_actual - inmueble['año']
        
        garaje_valor = 15000 if inmueble['garaje'] else 0
        precio_base = (inmueble['metros'] * 1000 + 
                      inmueble['habitaciones'] * 5000 + 
                    garaje_valor)
        
        if inmueble['zona'] == 'A':
            precio = precio_base * (1 - antiguedad / 100)
        elif inmueble['zona'] == 'B':
            precio = precio_base * (1 - antiguedad / 100) * 1.5
        
        if precio <= precioReferente:
            inmueble_con_precio = inmueble.copy()
            inmueble_con_precio['precio'] = round(precio, 2)
            listaBuscada.append(inmueble_con_precio)
    
    return listaBuscada 

inmuebles = [{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
{'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
{'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
{'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
{'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]   

presupuesto = 100000
resultados = buscarInmueble(inmuebles, presupuesto)
print(f"Inmuebles con precio <= {presupuesto}€:")
for inmueble in resultados:
    print(f"Año: {inmueble['año']}, Metros: {inmueble['metros']}, "
        f"Habitaciones: {inmueble['habitaciones']}, Garaje: {inmueble['garaje']}, "
        f"Zona: {inmueble['zona']}, Precio: {inmueble['precio']}€")

