#Crear diccionario
puntajes = {
    "juan": 95,
    "maria": 87,
    "pedro": 78,
    "ana":92
}

#Acceder a los valores por clave
print(puntajes["maria"])
# Print Output:
# 87

#Modificar valores
puntajes["pedro"] = 82
print(puntajes)
# Print output
# {'juan': 95, 'maria': 87, 'pedro': 82, 'ana': 92}

#Agregar nuevmos elementos
puntajes["carlos"] = 88
print(puntajes)
# Print output
#{'juan': 95, 'maria': 87, 'pedro': 82, 'ana': 92, 'carlos': 88}

del puntajes["ana"]
print(puntajes) #{'juan': 95, 'maria': 87, 'pedro': 82, 'carlos': 88}