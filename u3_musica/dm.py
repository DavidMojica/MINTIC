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

print(buscar_cancion("bohemian rhapsody"))
# Print Output:
# ('bohemian rhapsody', 'queen', 7.8)