musica = [("yellow submarine", "the beatles", 9.2),
          ("imagine", "john lennon", 8.5),
          ("let it be", "the beatles", 9.9),
          ("bohemian rhapsody", "queen", 7.8),
          ("stairway to heaven", "led zeppelin", 7.5)]

def buscar_cancion(nombre):
    for cancion in musica:
        if cancion[0] == nombre:
            return cancion
    return None

def buscar_por_artista(artista):
    canciones_artista = []
    for cancion in musica:
        if cancion[1] == artista:
            canciones_artista.append(cancion)
    return canciones_artista

print(buscar_cancion("bohemian rhapsody"))
# Print Output:
# ('bohemian rhapsody', 'queen', 7.8)
print(buscar_por_artista("the beatles"))
# Print Output:
#[('yellow submarine', 'the beatles', 9.2), ('let it be', 'the beatles', 9.9)]