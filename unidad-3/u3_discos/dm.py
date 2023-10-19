discos = [
    {"nombre": "Abbey Road", "artista": "The beatles",
     "canciones": [("Come Together", 260), ("Something", 182), ("Octopus Garden", 167)],
     "stock": 5
     },
    {"nombre": "Imagine", "artista": "John Lennon",
     "canciones": [("Imagine", 181), ("Cripped Inside", 231), ("It's so hard", 122)],
     "stock": 3
     },
]

def buscar_disco(discos, nombre=None, artista=None):
    resultados = []
    for disco in discos:
        if nombre and disco["nombre"] == nombre:
            resultados.append(disco)
        if artista and disco["artista"] == artista:
            resultados.append(disco)
    return resultados

def buscar_cancion(discos, nombre):
    resultados = []
    for disco in discos:
        for cancion in disco["canciones"]:
            if cancion[0] == nombre:
                resultados.append((cancion, disco["nombre"], disco["artista"]))
    return resultados

def comprar_disco(discos, nombre):
    for disco in discos:
        if disco["nombre"] == nombre and disco["stock"] > 0:
            disco["stock"] -= 1
            print(f"Has comprado {nombre}. Quedan {disco['stock']} en stock")
            return
    print(f"No se pudo completar la compra de {nombre}.")
        
def bubble_sort_discos(discos):
    n = len(discos)
    for i in range(n):
        for j in range(0, n-i-1):
            if discos[j]["nombre"] > discos[j+1]["nombre"]:
                discos[j], discos[j+1] = discos[j+1], discos[j]  
                
def buscar_disco_parcial(discos, nombre_parcial, indice=0):
    if indice == len(discos):
        return None
    if nombre_parcial in discos[indice]["nombre"]:
        return discos[indice]
    return buscar_disco_parcial(discos, nombre_parcial, indice+1)  

print(buscar_disco(discos, nombre="Imagine"))
print(buscar_cancion(discos, "Come Together"))
comprar_disco(discos, "Imagine")
print(buscar_disco_parcial(discos, "i"))

# Print Output:
# [{'nombre': 'Imagine', 'artista': 'John Lennon', 'canciones': [('Imagine', 181), ('Cripped Inside', 231), ("It's so hard", 122)], 'stock': 3}]
# [(('Come Together', 260), 'Abbey Road', 'The beatles')]
# Has comprado Imagine. Quedan 2 en stock
# {'nombre': 'Imagine', 'artista': 'John Lennon', 'canciones': [('Imagine', 181), ('Cripped Inside', 231), ("It's so hard", 122)], 'stock': 2}