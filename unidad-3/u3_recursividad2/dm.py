def permutaciones(lista):
    if len(lista) == 0:
        return [[]]  # Devuelve una lista que contiene una lista vacía como permutación base

    if len(lista) == 1:
        return [lista]  # Devuelve la lista original como permutación base

    resultados = []  # Lista para almacenar las permutaciones

    for i in range(len(lista)):
        m = lista[i]
        lista_remanente = lista[:i] + lista[i + 1:]
        for p in permutaciones(lista_remanente):
            resultados.append([m] + p)

    return resultados  # Devuelve la lista de permutaciones

nums = [1, 2, 3]
print(permutaciones(nums)) 
# Print Output:
# [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
# Variables:
