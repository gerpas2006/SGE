provincias = ["Sevilla", "Cádiz", "Huelva", "Málaga", "Granada", "Almería", "Córdoba", "Jaén"] 
provincias2 = ["Málaga","Málaga"]
contador = 0
elemento = 0

provincias.remove("Jaén")
print(provincias)

provincias.sort()
print(provincias)

provincias.insert(0,"Málaga")
print(provincias)

del provincias[3:5]
print(provincias)


provincias=provincias2+provincias
print(provincias)


for i in provincias:
    if i == "Málaga":
        contador+=1
print(contador)


del provincias[contador]
print(provincias)


provincias.reverse()
print(provincias)


del provincias[5:7]
print(provincias)





